#!/usr/bin/python
# -*- coding: utf-8 -*-

# question

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


#from random import choice
class Question(object):
    text = ""
    correctAnswer = ""
    package = None
    type = ""
    points = 1
    
    def __init__(self,package=None):
        
        self.package = package
        self.generate()
    
    def generate(self):
        """
        Will need to be overwritten in subclasses
        @return: None
        """
        self.text = ""
        self.correctAnswer = ""
        
    def getCorrectAnswer(self):
        """
        get correct answer of this quesiton
        @return: depends on the subclass
        """
        return self.correctAnswer
    
    def getText(self):
        """
        get text of the question.
        @return: string
        """
        return self.text
    
    def setPackage(self,package):
        """
        set's package for this question.
        you should probably call generate function
        after this.
        
        @param package: pyalpm.package object
        @return: None
        """
        self.package = package
        
class definition(Question):
    
    def __init__(self,package = None):
        Question.__init__(self,package)
        self.type = "definition"    
    def generate(self):
        self.text = "What is " + str(self.package.name)
        self.correctAnswer = str(self.package.desc)
        
class depends(Question):
    def __init__(self,package = None):
        Question.__init__(self,package)
        self.type = "depends"
        self.points = 2
    
    def generate(self):
        self.text = "Which one of the following does " + self.package.name + " (" + self.package.desc + ") depend on?"
        self.correctAnswer = self.package.depends
            
class requiredBy(Question):
    def __init__(self,package = None):
        Question.__init__(self,package)
        self.type = "requiredBy"
        self.points = 3
    
    def generate(self):
        
        self.text = self.package.name + "(" + self.package.desc + ")" + " is required by which one of the following packages?"
        self.correctAnswer = self.package.compute_requiredby()
        
#class installedSize(Question):
#    def __init__(self,package = None):
#        Question.__init__(self,package)
#        self.points = 6
#        self.type = "installedSize"
#        
#    def generate(self):
#        
#        self.text = "How much is the installed size of " + self.package.name + " (in kilobytes)"
#        self.correctAnswer = self.package.isize

#class packager(Question):
#    
#    def __init__(self,package = None):
#        Question.__init__(self,package)
#        self.type = "maintainer"
#        self.points = 6
#        
#    def generate(self):
#        
#        self.text = "Who is the packager of " + self.package.name
#        self.correctAnswer = self.package.packager
        
#class fileOwner(Question):
#    
#    def __init__(self,package = None):
#        Question.__init__(self,package)
#        self.type = "fileOwner"
#        self.points = 3
#    
#    def generate(self):
#        
#        file = choice(self.package.files)
#        while file.endswith("/"):
#            file = choice(self.package.files)
#        self.text = "Which package installed this file: " + file
#        self.correctAnswer = self.package.name
    
    
    