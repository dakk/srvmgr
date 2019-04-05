# -*- coding: utf-8 -*-
# Copyright (C) 2019 Davide Gessa

from setuptools import find_packages
from setuptools import setup

setup(name='srvmgr',
	version=0.1,
	description='A pluggable server manager for all your needs',
	author=['Davide Gessa'],
	setup_requires='setuptools',
	author_email=['gessadavide@gmail.com'],
	packages=[
		'srvmgr',
		'srvmgr.plugins'
	],
	entry_points={
		'console_scripts': [
			'srvmgr=srvmgr.srvmgr:main'
		],
	},
	install_requires=open ('requirements.txt', 'r').read ().split ('\n')
)
