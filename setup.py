# run `pip install -e .` inside individual folder

from setuptools import setup, find_packages

setup(
    name='java-version-manager',
    version='0.0.1',
     packages=find_packages()
)