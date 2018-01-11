#!/usr/bin/env python

import re
from os.path import abspath, dirname, join
from setuptools import setup, find_packages


CURDIR = dirname(abspath(__file__))

CLASSIFIERS = '''
Development Status :: 4 - Beta
License :: OSI Approved :: Apache Software License
Operating System :: POSIX
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3 :: Only
Topic :: Software Development :: Testing
Framework :: Robot Framework
Framework :: Robot Framework :: Library
'''.strip().splitlines()
with open(join(CURDIR, 'src', 'REST', '__init__.py')) as f:
    VERSION = re.search("\n__version__ = '(.*)'", f.read()).group(1)
with open(join(CURDIR, 'README.md')) as f:
    DESCRIPTION = f.read()
with open(join(CURDIR, 'requirements.txt')) as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name             = 'RESTinstance',
    version          = VERSION,
    description      = 'JSON API testing library for Robot Framework',
    long_description = DESCRIPTION,
    author           = 'Anssi Syrjäsalo',
    author_email     = 'anssi.syrjasalo@gmail.com',
    url              = 'https://github.com/asyrjasalo/RESTinstance',
    license          = 'Apache License 2.0',
    keywords         = 'robotframework REST HTTP JSON API testing library',
    classifiers      = CLASSIFIERS,
    install_requires = REQUIREMENTS,
    package_dir      = {'': 'src'},
    packages         = find_packages('src')
)
