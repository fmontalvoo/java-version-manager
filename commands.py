import os

import click

from set_env import setEnv
from manage_config import read_config, write_config

JAVA_HOME = 'JAVA_HOME'

JDK_DST = 'C:\opt\jdk'

def add_jdk(jdk_src):
    version_name = jdk_src.split('\\')[-1]
    config_file = read_config()
    if version_name in config_file:
        click.secho('Ya existe una version con ese nombre', fg='yellow')
    else:
        config_file[version_name] = jdk_src
        write_config(config_file)
        click.secho('JDK agregado', fg='green')

def list_jdk():
    config = read_config()
    for key, _ in config.items():
        if key == 'current':
            continue
        if 'current' in config and config['current'] == key:
            click.secho(f'* {key} (actual)', fg='green')
        else:
            click.echo(f'  {key}')

def use_jdk(jdk):
    config_file = read_config()
    if jdk in config_file:
        jdk_path = config_file[jdk]
        if not JAVA_HOME in os.environ:
            setEnv(keyname=JAVA_HOME, keyvalue=JDK_DST)
            os.symlink(jdk_path, JDK_DST)
        elif not os.path.islink(JDK_DST):
            os.symlink(jdk_path, JDK_DST)
        else:
            os.unlink(JDK_DST)
            os.symlink(jdk_path, JDK_DST)
        
        config_file['current'] = jdk
        write_config(config_file)
        click.secho(f'Usando {jdk}', fg='blue')
    else:
        click.secho('No existe el jdk', fg='red')

def delete_jdk(jdk):
    config_file = read_config()
    if jdk in config_file:
        if jdk == config_file['current']:
            click.secho('No puedes eliminar la version actual', fg='yellow')
        else:
            del config_file[jdk]
            write_config(config_file)
            click.secho(f'Eliminado {jdk}', fg='green')
    else:
        click.secho('No existe el jdk', fg='red')

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
    




