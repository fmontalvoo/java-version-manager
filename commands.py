import os

import click

from set_env import setEnv

JAVA_HOME = 'JAVA_HOME'

JDK_DST = 'C:\opt\jdk'

def add_jdk(jdk_src):
    print(jdk_src)

def list_jdk():
    print('Listando jdk')

def use_jdk(jdk):
    if not JAVA_HOME in os.environ:
        setEnv(keyname=JAVA_HOME, keyvalue=JDK_DST)
        os.symlink(jdk, JDK_DST)
        click.echo('1.JDK modificado')
    elif not os.path.islink(JDK_DST):
        os.symlink(jdk, JDK_DST)
        click.echo('2.JDK modificado')
    else:
        os.unlink(JDK_DST)
        os.symlink(jdk, JDK_DST)
        click.echo('3.JDK modificado')

def delete_jdk(jdk):
    print(jdk)

@click.command()
@click.option('-a','--add', type=str, help='Agrega la ruta al sdk de java; ejemplo: -a "path:\\to\\jdk"')
@click.option('-l','--list', is_flag=True, help='Lista los jdk disponibles')
@click.option('-u','--use', type=str, help='Usa un jdk')
@click.option('-d','--delete',type=str, help='Elimina un jdk')
@click.version_option(package_name='java-version-manager')
def cli(add, list, use, delete):
    if add:
        add_jdk(add)
    elif list:
        list_jdk()
    elif use:
        use_jdk(use)
    elif delete:
        delete_jdk(delete)
    




