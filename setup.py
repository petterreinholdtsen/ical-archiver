#!/usr/bin/env python
# Copyright (C) 2017 Petter Reinholdtsen <pere@hungry.com>
#
# Licensed under the GNU General Public License Version 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

from distutils.core import setup

prog = {}
with open('ical-archiver', 'r') as version_file:
    exec (version_file.read(), prog)

setup(name='iCal archiver',
      version     = prog['__version__'],
      description = prog['__summary__'],
      author      = prog['__author__'].split('<')[0].strip(),
      author_email= prog['__author__'].split('<')[1].split('>')[0].strip(),
      url         = prog['__homepage__'],
      license     = prog['__license__'],
      requires    = ['vobject'],
      scripts     = ['ical-archiver'],
      )
