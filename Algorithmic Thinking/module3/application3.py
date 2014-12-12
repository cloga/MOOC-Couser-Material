'''
application3
'''
# !/Library/Frameworks/Python.framework/Versions/2.7/bin/Python
# -*- coding: utf-8 -*-

__author__ = "Cloga Chen(Cloga0216@gmail.com)"
__copyright__ = "Copyright (c) 2014 Cloga Chen"
__createtime__ = "2014-10-02 19:35:04"
__modifytime__ = "2014-10-02 19:35:07"

import random
import alg_cluster
import time
import alg_project3_solution
import pandas as pd
from ggplot import *

def gen_random_clusters(num_clusters):
    '''creates a list of clusters where each cluster in this list corresponds
    to one randomly generated point in the square with corners (±1,±1). Use
    this function and your favorite Python timing code to compute the running
    times of the functions slow_closest_pairs and fast_closest_pair for lists
    of clusters of size 2 to 200.
    '''
    clusters_list = []
    for _ in range(num_clusters):
        x_axis = random.random()
        y_axis = random.random()
        cluster = alg_cluster.Cluster(set(), x_axis, y_axis, '', '')
        clusters_list.append(cluster)
    return clusters_list

TIMES = []
for num in range(2, 200):
    fun_time = {}
    clusters = gen_random_clusters(num)
    time_start = time.time()
    alg_project3_solution.slow_closest_pairs(clusters)
    time_end = time.time()
    time_spent = time_end - time_start
    fun_time['number of initial clusters'] = num
    fun_time['slow_closest_pairs'] = time_spent
    time_start = time.time()
    alg_project3_solution.fast_closest_pair(clusters)
    time_end = time.time()
    time_spent = time_end - time_start
    fun_time['fast_closest_pair'] = time_spent
    TIMES.append(fun_time)
    ITMES_DF = pd.DataFrame(TIMES)

ax = ITMES_DF[['slow_closest_pairs', 'fast_closest_pair']].plot(title='running time of different functions')
ax.set_ylabel('running time')
ax.set_xlabel('number of initial clusters')