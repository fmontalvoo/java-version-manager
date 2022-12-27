import os

from set_env import setEnv  

JAVA_HOME = 'JAVA_HOME'

src = 'C:\Program Files\Java\jdk1.8.0_333'
dst = 'C:\opt\jdk'

if not JAVA_HOME in os.environ:
    setEnv(keyname=JAVA_HOME, keyvalue=dst)
    os.symlink(src, dst)
    print('1.Enlace creado')
elif not os.path.islink(dst):
    os.symlink(src, dst)
    print('2.Enlace creado')
else:
    print('3.El enlace ya existe')
    os.unlink(dst)
