import os

from set_env import setEnv  

src = 'C:\Program Files\Java\jdk1.8.0_333'
dst = 'C:\opt\jdk'

if not 'JAVA_HOME' in os.environ:
    setEnv(keyname='JAVA_HOME', keyvalue='C:\opt\jdk')
    os.symlink(src, dst)
else:
    os.symlink(src, dst)

print('Enlace creado')
