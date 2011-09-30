#!/usr/bin/python
# -*- coding: utf-8 -*-

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


import pyalpm
from pycman import config
import question as q
from random import choice, randint
from sys import modules

config.init_with_config("/etc/pacman.conf")
localdb = pyalpm.get_localdb()
#questionTypes= (q.definition,q.depends,
#                q.fileOwner,q.installedSize,
#                q.packager)

types = [getattr(q, t) for t in dir(q) if str(type(getattr(q, t))) == "<class 'type'>"]
questionTypes = [qtype for qtype in types if (issubclass(qtype, q.Question) and qtype is not q.Question)]
del(types)

def getRandomQuestion(package=None, numWrongAnswers=3):
    """Returns a tuple with size of 3, first question text,
    second correct answer, third  list of wrong answers
     @param package: A pyalpm.package type
     @param numWrongAnswers: integer
     @return: tuple
    """
    qToReturn = None
    if package == None:
            package = getRandomPackage()
    
    global questionTypes
    
    while not qToReturn:
        
        qtype = choice(questionTypes)
        question = qtype(package)
        func = getattr(modules[__name__], "_" + question.type)

        qToReturn = func(question, numWrongAnswers)
        
    return qToReturn


def getRandomPackage(exception=[]):
    """
    Return a random package
    @ param exception: list of packages as an exception
    @ return: a package
    """
    global localdb

    package = choice(localdb.pkgcache)
    if len(exception) == 0:
        return package
    else:
        while package.name in exception:
            package = choice(localdb.pkgcache)
        return package

def qgenerator(function):
    def generate(question, numWrongAnswers=3):
        if question.correctAnswer is None:
            return None


        if isinstance(question.correctAnswer, list):
            if len(question.correctAnswer) > 0:
                correct_answer = choice(question.correctAnswer)
            else:
                return None
        else:
            correct_answer = question.correctAnswer

        wrong_answers = []

        while len(wrong_answers) < numWrongAnswers:
            answer = function(question, numWrongAnswers)
            if answer not in wrong_answers and answer is not None:
                wrong_answers.append(answer)

        return (question.text, correct_answer, wrong_answers,question.points)

    return generate


@qgenerator
def _definition(question, numWrongAnswers=3):

    return getRandomPackage([question.package.name]).desc


@qgenerator
def _depends(question, numWrongAnswers=3):
    pkg = getRandomPackage([question.correctAnswer])
    return pkg.name + "(" + pkg.desc + ")"


def _requiredBy(question, numWrongAnswers=3):
    global localdb
    if len(question.correctAnswer) > 0:
        correct_answer_name = choice(question.correctAnswer)
        correct_answer_package = localdb.get_pkg(correct_answer_name)
        correct_answer = correct_answer_name + "(" + correct_answer_package.desc + ")"
    else:
        return None
        
    wrong_answers = []
    
    while len(wrong_answers) < numWrongAnswers:
        pkg = getRandomPackage([pkg for pkg in question.correctAnswer])
        answer = pkg.name + "(" + pkg.desc + ")"
        if answer not in wrong_answers and answer is not None:
            wrong_answers.append(answer)

    return (question.text, correct_answer, wrong_answers,question.points)

#@qgenerator
#def _installedSize(question, numWrongAnswers=3):
#    (type(question.correctAnswer))
#    while True:
#        rand = randint(int(question.correctAnswer * 0.1), int(question.correctAnswer * 1.9))
#        (rand)
#        (type(rand))
#        if rand != question.correctAnswer:
#            return rand
#
#@qgenerator
#def _maintainer(question, numWrongAnswers=3):
#    while True:
#        rand_pack = getRandomPackage()
#        if rand_pack.packager != question.correctAnswer:
#            return rand_pack.packager
#        
#@qgenerator
#def _fileOwner(question, numWrongAnswers=3):
#    
#    return getRandomPackage([question.correctAnswer]).name

if __name__ == "__main__":
    (getRandomQuestion())
