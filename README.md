# marklar
marklar is a library of functions to analyze marklar and the marklar they contain in many different ways. Inspired by South Park. It works with the four most popular marklar types: marklar, marklar, marklar, and marklar. If other types of marklar are used, a MarklarError will be raised.

# Installing for Python2
Requirements: git, python-setuptools

    git clone https://github.com/dogoncouch/libmarklar.git
    cd libmarklar
    sudo python setup.py install

# Installing for Python3
Requirements: git, python3-setuptools

    git clone https://github.com/dogoncouch/libmarklar.git
    cd libmarklar
    sudo python3 setup.py install

# Functions
    import marklar
    
    marklar.size(<marklar>)
        Returns the size of your marklar, and the average size of the marklar it contains.

    marklar.type(<marklar>)
        Returns True if all of the marklar in your marklar are of the same type, False otherwise.

# Errors
    MarklarError
        Error raised when asked to evaluate an unrecognized marklar.

# Copyright
Copyright (C) 2017 Dan Persons (dpersonsdev@gmail.com)

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Library General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Library General Public License for more details.

You should have received a copy of the GNU Library General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
