# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in custom_bom/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('custom_bom/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

setup(
	name='custom_bom',
	version=version,
	description='To Genrate and change bom material in sales order item table',
	author='techerp@gmail.com',
	author_email='techerp@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
