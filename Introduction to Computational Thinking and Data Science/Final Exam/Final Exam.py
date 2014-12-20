# -*- coding: utf-8 -*-
# !/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# !/usr/bin/python


__author__ = "Cloga Chen(Cloga0216@gmail.com)"
__copyright__ = "Copyright (c) 2014 Cloga Chen"
__createtime__ = "2014-12-18 21:54:55"
__modifytime__ = "2014-12-18 21:54:56"

# PROBLEM 2-2  

A =  [0,1,2,3,4,5,6,7,8]

B = [5,10,10,10,15]

C = [0,1,2,4,6,8]

D = [6,7,11,12,13,15]

E = [9,0,0,3,3,3,6,6]

def get_variance(item_list):
    avg = mean(item_list)
    variance = 0.0
    for i in item_list:
        variance += (i - avg) ** 2
    return variance / len(item_list)

for l in [A, B, C, D, E]:
    print mean(l), get_variance(l)

# PROBLEM 2-3  

def possible_mean(L):
    return sum(L)/len(L)

def possible_variance(L):
    mu = possible_mean(L)
    temp = 0
    for e in L:
        temp += (e-mu)**2
    return temp / len(L)

for l in [A, B, C, D, E]:
    print possible_variance(l)
