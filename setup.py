# run `pip install -e .` inside individual folder

from setuptools import setup, find_packages

setup(
    name='java-version-manager',
    version='1.0.0-rc',
     packages=find_packages()
)