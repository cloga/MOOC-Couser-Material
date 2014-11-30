# !/Library/Frameworks/Python.framework/Versions/2.7/bin/Python
# -*- coding: utf-8 -*-

__author__ = "Cloga Chen(Cloga0216@gmail.com)"
__copyright__ = "Copyright (c) 2014 Cloga Chen"
__createtime__ = "2014-11-22 10:23:57"
__modifytime__ = "2014-11-22 10:23:59"

import pylab
import math 
import random

# Problem 4
class Location(object):

    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist ** 2 + yDist ** 2) ** 0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'


class Field(object):

    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        # use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


import random


class Drunk(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'This drunk is named ' + self.name


class UsualDrunk(Drunk):

    def takeStep(self):
        stepChoices =\
            [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


class ColdDrunk(Drunk):

    def takeStep(self):
        stepChoices =\
            [(0.0, 0.9), (0.0, -1.03), (1.03, 0.0), (-1.03, 0.0)]
        return random.choice(stepChoices)


class EDrunk(Drunk):

    def takeStep(self):
        ang = 2 * math.pi * random.random()
        length = 0.5 + 0.5 * random.random()
        return (length * math.sin(ang), length * math.cos(ang))


class PhotoDrunk(Drunk):

    def takeStep(self):
        stepChoices =\
            [(0.0, 0.5), (0.0, -0.5),
             (1.5, 0.0), (-1.5, 0.0)]
        return random.choice(stepChoices)

class DDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.85, 0.85), (-0.85, -0.85),
                     (-0.56, 0.56), (0.56, -0.56)] 
        return random.choice(stepChoices)


def walkVector(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(f.getLoc(d).getX() - start.getX(),
           f.getLoc(d).getY() - start.getY())

# Suppose we use a Monte Carlo simulation to simulate a random walk of a
# class of drunk, returning a collection of actual distances from the
# origin for a set of trials.

def simWalks(numSteps, numTrials, dClass):
    homer = dClass('Homer')
    origin = Location(0, 0)
    position = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        position.append(walkVector(f, homer, numSteps))
    x_axis = [p[0] for p in position]
    y_axis = [p[1] for p in position]
    pylab.scatter(x_axis, y_axis)
    pylab.title(dClass.__name__ + 'position')
    pylab.xlabel('x axis')
    pylab.ylabel('y axis')
    pylab.show()


simWalks(100, 1000, UsualDrunk)
simWalks(100, 1000, ColdDrunk)
simWalks(100, 1000, EDrunk)
simWalks(1000, 10000, PhotoDrunk)
simWalks(100, 1000, DDrunk)


### Problem 5

def sampleQuizzes():
    output = 0
    for _ in range(10000):
        score = 0
        midterm1 = random.uniform(50, 80)
        midterm2 = random.uniform(60, 90)
        final = random.uniform(55, 95)
        score = 0.25 * midterm1 + 0.25 * midterm2 + 0.5 * final
        if score >= 70 and score <= 75:
            output = output + 1
    return output / 10000.0



def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of 
    the three exams, then calculates the final score and
    appends it to a list of scores.
    
    Returns: A list of numTrials scores.
    """
    scores = []
    for _ in range(numTrials):
        score = 0
        midterm1 = random.uniform(50, 80)
        midterm2 = random.uniform(60, 90)
        final = random.uniform(55, 95)
        score = 0.25 * midterm1 + 0.25 * midterm2 + 0.5 * final
        scores.append(score)
    return scores



def plotQuizzes():
    scores = generateScores(10000)
    pylab.hist(scores, 7)
    pylab.title('Distribution of Scores')
    pylab.ylabel('Number of Trials')
    pylab.xlabel('Final Score')
    pylab.show()

# Problem 6

def probTest(limit):
    if limit >= 1:
        return 0
    p = 1
    n = 0
    while p >= limit:
        n += 1
        p = 1 / 6.0 * (5 / 6.0) ** (n - 1)
    return n


# Problem 7

def generate_balls(num):
    ball_list = []
    for _ in range(num):
        if random.random() >= 0.5:
            ball_list.append(0)
        else:
            ball_list.append(1)
    return ball_list

ball_list = generate_balls(1000)

def LV():
    black = 0
    n = 0
    while not black:
        black = random.choice(ball_list)
        n += 1
    return n

def MC():
    index = random.choice(range(len(ball_list)))
    n = 1
    while not ball_list[index]:
        if index == len(ball_list):
            index = random.choice(range(len(ball_list)))
        index += 1
        n += 1
    return n





histogram = [ 0 for i in range(1,1000)]  # intialize the list to be all zeros
for i in range(1000):
    result = LV()
    histogram[ result ] += 1
plot( histogram )
    


histogram = [ 0 for i in range(1,1000)]  # intialize the list to be all zeros

for i in range(1000):

    result = MC()

    histogram[ result ] += 1

plot( histogram )
