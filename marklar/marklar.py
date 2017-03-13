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

class MarklarError(Exception):
    pass

# To Do: Add 'marklar complexity' (depth)

def size(marklar):
    """Returns the number of marklar in your marklar, and the average marklar size"""
    try:
        if marklar.split('\n')[1]:
            l = [ 0 + len(m) for m in marklar.split('\n') ]
            return len(marklar), l/len(marklar)
        elif marklar.split(' ')[1]:
            l = [ 0 + len(m) for m in marklar.split(' ') ]
            return len(marklar), l/len(marklar)
        elif marklar.split('.')[1]:
            l = [ 0 + len(m) for m in marklar.split('.') ]
            return len(marklar), l/len(marklar)
        elif marklar.split(',')[1]:
            l = [ 0 + len(m) for m in marklar.split(',') ]
            return len(marklar), l/len(marklar)
        else: return len(marklar), 1
    except AttributeError: pass
    
    try:
        marklar = marklar + []
        try:
            l = [ 0 + m for m in marklar ]
            return len(marklar), l/len(marklar)
        except TypeError: pass
        try:
            l = [ 0 + len(m) for m in marklar ]
            return len(marklar), l/len(marklar)
        except TypeError: pass
    except TypeError: pass
    
    try:
        marklar.update({})
        l = [ 0 + len(marklar[m]) for m in marklar ]
        return len(marklar), l/len(marklar)
    except AttributeError: pass

    try:
        if marklar * marklar != False:
            return marklar, 1
    except TypeError: pass
    
    raise MarklarError('Unrecognized marklar')

def type(marklar):
    """Checks if all the marklar in your marklar are the same marklar type"""
    try:
        marklar = marklar + ''
        if marklar.isalpha(): return True
        elif marklar.isnumeric(): return True
        elif marklar.isspace(): return True
        else: return False
    except TypeError: pass

    try:
        x = marklar ** 2
        return True
    except TypeError: pass 
    
    try:
        marklar = marklar + []
        try:
            x = sum(m for m in marklar)
            return True
        except TypeError: return False
        try:
            x = [ ' ' + m for m in marklar ]
            return True
        except TypeError: return False
        try:
            x = [ [] + m for m in marklar ]
            return True
        except TypeError: return False
        try:
            x = [ {} + m for m in marklar ]
            return True
        except TypeError: return False
    except TypeError: pass

    try:
        marklar = marklar + {}
        try:
            x = sum(marklar[m] for m in marklar)
            return True
        except TypeError: return False
        try:
            x = [ ' ' + marklar[m] for m in marklar ]
            return True
        except TypeError: return False
        try:
            x = [ [] + marklar[m] for m in marklar ]
            return True
        except TypeError: return False
        try:
            x = [ {} + marklar[m] for m in marklar ]
            return True
        except TypeError: return False
    except TypeError: pass

    raise MarklarError('Unrecognized marklar')
