#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

__version__ = '0.2.0'

import os
from setuptools import setup

py_version = sys.version_info[:2]

if py_version < (2, 6):
    raise RuntimeError(
        'On Python 2, supervisor-stdout requires Python 2.6 or later')
elif (3, 0) < py_version < (3, 2):
    raise RuntimeError(
        'On Python 3, supervisor-stdout requires Python 3.2 or later')

setup(
    name = 'supervisor-stdout',
    version = __version__,
    py_modules = ['supervisor_stdout'],
    author = 'Taylor Jones',
    author_email = 'taylorjonesdev@gmail.com',
    description = 'Relay child process output to supervisor\'s stdout',
    install_requires = ['supervisor >= 3.0a6'],
    long_description = open('README.rst').read(),
    license = 'BSD',
    keywords = 'supervisor',
    url = 'https://github.com/taylor-jones/supervisor-stdout',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    entry_points = {
        'console_scripts': [
            'supervisor_stdout = supervisor_stdout:main',
        ]
    },
    zip_safe = False
)
