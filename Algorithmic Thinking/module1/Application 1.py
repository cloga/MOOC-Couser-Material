'''
Application1 code about Algorithmic Thinking
'''
# !/Library/Frameworks/Python.framework/Versions/2.7/bin/Python
# -*- coding: utf-8 -*-

__author__ = "Cloga Chen(Cloga0216@gmail.com)"
__copyright__ = "Copyright (c) 2014 Cloga Chen"
__createtime__ = "2014-08-28 17:40:24"
__modifytime__ = "2014-08-28 22:07:22"

# Question1
import pandas as pd
import numpy as np
from Project1 import in_degree_distribution, compute_in_degrees,\
                        make_complete_graph
from ggplot import *
import random


CIT_GRAPH = {}
with open('alg_phys-cite.txt', 'r') as FILE:
    for line in FILE:
        papers = line.split()
        CIT_GRAPH[papers[0]] = set(papers[1:])


def generate_in_degree_dist_plot(directed_graph, log_log=True):
    '''
    generate In_degree_distribution_log_log_plot
    '''
    in_degrees_dis = pd.DataFrame(
        in_degree_distribution(directed_graph).items(),\
        columns=['in_degree', '#']
    )
    in_degrees_dis['%'] = in_degrees_dis['#'] / in_degrees_dis['#'].sum()
    in_degrees_dis['log(%)'] = np.log(in_degrees_dis['%'])
    in_degrees_dis['log(in_degree)'] = np.log(in_degrees_dis['in_degree'])
    if log_log:
        print ggplot(in_degrees_dis, aes('log(in_degree)', 'log(%)')) + \
            geom_point(colour='blue') +\
            ggtitle("In-degree distribution log/log plot")
    else:
        print ggplot(in_degrees_dis, aes('in_degree', '%')) + \
            geom_point(colour='blue') + ggtitle("In-degree distribution")

# Question2

def generate_rand_di_graph_er(notes_number, probability):
    '''
    Takes the number of nodes nodes_number and probability returns a dictionary
    corresponding to a directed graph with the specified number of nodes.

    Parameters
    ----------
    notes_number : int
    Return graph node number

    probability: float < 1

    Returns
    -------
    graph : dict
    '''
    if  (type(notes_number) != int) | (notes_number <= 0) | (probability > 1):
        return {}
    directed_graph = {}
    nodes = range(notes_number)
    for node in nodes:
        start = node
        ends = nodes
        ends.remove(start)
        for end in ends:
            if random.random() > probability:
                directed_graph[start] = \
                directed_graph.get(start, set()).union(set([end]))
    return directed_graph

# Question3

from alg_dpa_trial import DPATrial

def dpa_digraph_gen(target_node, step_node):
    '''
    generate digraph use DPA Algorithm

    Parameters
    ----------
    target_node : int
    step_node : int

    Returns
    -------
    graph : dict
    '''
    DPA_GRAPH = DPATrial(step_node)
    directed_graph = make_complete_graph(step_node)
    for i in range(step_node, target_node):
        directed_graph[i] = DPA_GRAPH.run_trial(i)
    return directed_graph

    
# GRAPH = dpa_digraph_gen(27768, 13)
generate_in_degree_dist_plot(GRAPH, log_log=True)
# CIT_GRAPH_DF = pd.DataFrame({node:len(indegree) for node, indegree in CIT_GRAPH.items()}.items(), columns=['node', 'in_degree'])