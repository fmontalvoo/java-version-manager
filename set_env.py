# -*- coding: utf-8 -*-

# https://stackoverflow.com/questions/71253807/how-to-set-windows-environment-variable-from-python
# https://github.com/Descent098/pystall/blob/799ec3927da74fde192bac0da208f7acc4274e51/pystall/core.py#L121-L166

import winreg
import ctypes

PATH='PATH'
ENV='Environment'

def appendEnv(keyname, regdir=ENV):
    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as root:
            with winreg.OpenKey(root, regdir, 0, winreg.KEY_ALL_ACCESS) as key:
                existing_path_value = getEnv(PATH)
                new_path_value = existing_path_value + ';' + f'%{keyname}%\\bin' + ';' + f'%{keyname}%\\jre' + ';'
                winreg.SetValueEx(key, PATH, 0, winreg.REG_EXPAND_SZ, new_path_value)

            HWND_BROADCAST = 0xFFFF
            WM_SETTINGCHANGE = 0x1A
            SMTO_ABORTIFHUNG = 0x0002
            result = ctypes.c_long()
            SendMessageTimeoutW = ctypes.windll.user32.SendMessageTimeoutW
            SendMessageTimeoutW(HWND_BROADCAST, WM_SETTINGCHANGE, 0, regdir, SMTO_ABORTIFHUNG, 5000, ctypes.byref(result),)
            
def setEnv(keyname, keyvalue, regdir=ENV):
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, regdir) as _:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, regdir, 0, winreg.KEY_WRITE) as key:
            winreg.SetValueEx(key, keyname, 0, winreg.REG_SZ, keyvalue)
            appendEnv(keyname)
        

def getEnv(keyname, regdir=ENV):
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, regdir) as accessRegistryDir:
        value, _ = winreg.QueryValueEx(accessRegistryDir, keyname)
        return(value)
