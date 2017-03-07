#!/usr/bin/env python

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

class MarklarError(Exception):
    pass

def marklar(marklar):
    """Returns the number of marklar in your marklar, and the average marklar size"""
    try:
        marklar = marklar + []
        l = 0
        try:
            marklar = marklar + 1 - 1
            for m in marklar:
                l = l + m
            return len(marklar), l/len(marklar)
        except TypeError:
            for m in marklar:
                l = l + len(m)
            return len(marklar), l/len(marklar)
    except TypeError: pass
    
    try:
        if marklar.split('\n')[1]:
            l = 0
            for m in marklar.split('\n'):
                l = l + len(m)
            return len(marklar), l/len(marklar)

        elif marklar.split(' ')[1]:
            l = 0
            for m in marklar.split(' '):
                l = l + len(m)
            return len(marklar), l/len(marklar)

        elif marklar.split('.')[1]:
            l = 0
            for m in marklar.split('.'):
                l = l + len(m)
            return len(marklar), l/len(marklar)
        elif marklar.split(',')[1]:
            l = 0
            for m in marklar.split(','):
                l = l + len(m)
            return len(marklar), l/len(marklar)

    except AttributeError: pass
    
    try:
        marklar.update({})
        l = 0
        for m in marklar:
            l = l + len(marklar[m])
        return len(marklar), l/len(marklar)

    except AttributeError: pass
    
    raise MarklarError("Unrecognized marklar")
