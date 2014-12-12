'''
Algorithmic Thinking Application 2
'''
# !/Library/Frameworks/Python.framework/Versions/2.7/bin/Python
# -*- coding: utf-8 -*-

__author__ = "Cloga Chen(Cloga0216@gmail.com)"
__copyright__ = "Copyright (c) 2014 Cloga Chen"
__createtime__ = "2014-09-17 16:05:47"
__modifytime__ = "2014-09-21 23:33:41"

import urllib2
import random
from alg_upa_trial import UPATrial
from project2 import compute_resilience
import pandas as pd
from ggplot import *
import time
from alg_application2_provided import targeted_order

NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    print "Loaded graph with", len(graph_lines), "nodes"
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))
    return answer_graph


def generate_rand_undigraph_er(notes_number, probability):
    '''
    Takes the number of nodes nodes_number and probability returns a dictionary
    corresponding to a un-directed graph with the specified number of nodes.

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
    undirected_graph = {node : set()for node in range(notes_number)}
    nodes = range(notes_number)
    for node in nodes:
        start = node
        ends = nodes
        ends.remove(start)
        for end in ends:
            if random.random() < probability:
                undirected_graph[start] = \
                undirected_graph.get(start, set()).union(set([end]))
                undirected_graph[end] = \
                undirected_graph.get(end, set()).union(set([start]))
    return undirected_graph

def make_complete_graph(num_nodes):
    '''
    Takes the number of nodes num_nodes and returns a dictionary corresponding
    to a complete graph with the specified number of nodes.

    Parameters
    ----------
    num_nodes : int
        Return graph node number

    Returns
    -------
    graph : dictionary
    '''

    graph = {}
    if  (type(num_nodes) != int) | (num_nodes <= 0):
        return {}
    for start in range(num_nodes):
        endnodes = set(range(num_nodes)) - set([start])
        graph[start] = endnodes
    return graph

def upa_undigraph_gen(node_num, step_node):
    '''
    generate un-digraph use UPA Algorithm

    Parameters
    ----------
    node_num : int
    step_node : int

    Returns
    -------
    graph : dict
    '''
    UPAGraph = UPATrial(step_node)
    graph = make_complete_graph(step_node)
    for i in range(step_node, node_num):
        neighbors = UPAGraph.run_trial(step_node) 
        graph[i] = neighbors
        for nei in neighbors:
            graph[nei] = graph.get(nei, set()).union({i})
    return graph

def get_random_order(graph):
    '''
    given a graph return random nodes order

    Parameters
    ----------
    graph : dict, representation of graph using adjacent list

    Returns
    -------
    order : list
    '''
    nodes = graph.keys()
    return random.sample(nodes, len(nodes))

def fast_targeted_order(ugraph):
    '''
    given a ugraph return node order based dec degree

    Parameters
    ----------
    ugraph : dict, representation of un-direct graph using adjacent list

    Returns
    -------
    order : list
    '''
    ugraph = UGRAPH10
    degree_set = {degree:set() for degree in range(len(ugraph.keys()))}
    for node in ugraph.keys():
        degree_set[len(ugraph[node])] = \
        degree_set.get(len(ugraph[node])).union({node})
    order = []
    for k in ugraph.keys()[::-1]:
        while degree_set.get(k, None):
            for node in degree_set[k]:
                degree_set[k].remove(node)
                break
            for neighbor in ugraph[node]:
                degree = len(ugraph.get(neighbor, set()))
                if neighbor in degree_set[degree]:
                    degree_set[degree].remove(neighbor)
                if degree > 0:
                    degree_set[degree-1] = degree_set[degree-1].union({neighbor})
            order.append(node)
            del ugraph[node]
    return order

def get_run_time(nlist, mlist, graphfun):
    '''
    calculate time spend
    '''
    time_spend = []
    for node_num in nlist:
        for step in mlist:
            ugraph = graphfun(node_num, step)
            to_start = time.time()
            targeted_order(ugraph)
            to_end = time.time()
            to_time_spend = to_end - to_start
            time_spend.append({
                'n': node_num, 'm': step, 'type': 'targeted order',
                'time spend': to_time_spend
                })
            fto_start = time.time()
            fast_targeted_order(ugraph)
            fto_end = time.time()
            fto_time_spend = fto_end - fto_start
            time_spend.append({
                'n': node_num, 'm': step, 'type': 'fast targeted order',
                'time spend': fto_time_spend
                })
    return time_spend


TIMES = get_run_time(range(10, 1000, 10), [5], upa_undigraph_gen)
UGRAPH10 = upa_undigraph_gen(10, 5)
ORDER = fast_targeted_order(UGRAPH10)

FTO_ORDER = fast_targeted_order(ER_UNDI_GRAPH)

# Generate Graphs
COMPUTERNETWORK = load_graph(NETWORK_URL)
# sum(map(len, COMPUTERNETWORK.values()))/2
# average(map(len, COMPUTERNETWORK.values()))
PROB = 0.00171*3
NODES_NUM = 1347
ER_UNDI_GRAPH = generate_rand_undigraph_er(NODES_NUM, PROB)
# sum(map(len, ER_UNDI_GRAPH.values()))/2
UPA_GRAPH = upa_undigraph_gen(1347, 3)
# sum(map(len, UPA_GRAPH.values()))/2

# generate random order
ORDER_CN = get_random_order(COMPUTERNETWORK)
ORDER_ER = get_random_order(ER_UNDI_GRAPH)
ORDER_UPA = get_random_order(UPA_GRAPH)

# Q1
CN_RE = compute_resilience(COMPUTERNETWORK, ORDER_CN)
ER_RE = compute_resilience(ER_UNDI_GRAPH, ORDER_ER)
UPA_RE = compute_resilience(ER_UNDI_GRAPH, ORDER_ER)

RESILIENCE_DF = pd.DataFrame(
    {'COMPUTERNETWORK': CN_RE, 'ER_GRAPH(p=0.00513)': ER_RE,
    'UPA_GRAPH(m=3)':UPA_RE, 'nodes_removed': range(1348)})
RESILIENCE_DF_R = pd.melt(RESILIENCE_DF, id_vars=['nodes_removed'], 
    value_vars=['COMPUTERNETWORK', 'ER_GRAPH(p=0.00513)', 'UPA_GRAPH(m=3)'],
    var_name='graph_type', value_name='size_of_the_largest_connect_component')

print ggplot(RESILIENCE_DF_R, aes(y='size_of_the_largest_connect_component', x='nodes_removed', color='graph_type')) + \
            geom_point() +\
            ggtitle("The resilience of three graphs")