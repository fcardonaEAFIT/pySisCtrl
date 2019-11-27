# -*- coding: utf-8 -*-

from setuptools import setup, find_packages_namespaces

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='PySisCtrl',
    version="0.1.1",
    description='Read a yaml file an create a network of processes implements automatons.',
    long_description=readme,
    author="Juan Francisco Cardona Mc'Cormick",
    author_email='fcardona@eafit.edu.co',
    url='https://github.com/fcardonaEAFIT/pySisCtrl',
    license=license,
    package_dir={'': 'src'},
    packages=find_packages_namespaces(where='src'),
    entry_points={
        'console_scripts': [
            'pysisctrl = pysisctrl.main:main_func'
        ]
    }
)