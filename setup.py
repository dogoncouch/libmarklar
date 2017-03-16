#!/usr/bin/env python3

#_    Copyright (C) 2017 Dan Persons (dpersonsdev@gmail.com)
#_
#_    This library is free software; you can redistribute it and/or
#_    modify it under the terms of the GNU Library General Public
#_    License as published by the Free Software Foundation; either
#_    version 2 of the License, or (at your option) any later version.
#_
#_    This library is distributed in the hope that it will be useful,
#_    but WITHOUT ANY WARRANTY; without even the implied warranty of
#_    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#_    Library General Public License for more details.
#_
#_    You should have received a copy of the GNU Library General Public
#_    License along with this library; if not, write to the Free Software
#_    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

from setuptools import setup
from os.path import join
from sys import prefix
from marklar import __version__

ourdata = [(join(prefix, 'share/man/man3'), ['doc/marklar.3']),
        (join(prefix, 'share/doc/marklar'), ['README.md', 'LICENSE'])]

setup(name = 'marklar', version = str(__version__),
        description = 'Evaluate marklar and the marklar they contain',
        long_description = open('README.md').read(),
        author = 'Dan Persons', author_email = 'dpersonsdev@gmail.com',
        py_modules = ['marklar'],
        data_files = ourdata,
        classifiers = ["Development Status :: 3 :: Alpha",
            "Environment :: Other Environment",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU Lesser General Public " +
            "License v2 or later (LGPLv2+)",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Topic :: Software Development :: Libraries :: Python Modules"])
