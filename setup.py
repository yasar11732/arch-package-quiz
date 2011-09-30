#!/usr/bin/env python

"""
Copyright 2011 Yaşar Arabacı


This file is part of packagequiz.
packagequiz is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from distutils.core import setup


setup(   name = "package-quiz",
         version = "0.1",
         description = "A fun quiz about installed package",
         author = "Yaşar Arabacı",
         author_email = "yasar11732@gmail.com",
         url = "http://archlinuxpackag.sourceforge.net/",
         license = "GPLv3",
         packages = ["packagequiz"],
         scripts = ['pquiz'],
         data_files = [("/usr/share/locale/tr",["translations/tr/pquiz.mo"])]
         
         )
