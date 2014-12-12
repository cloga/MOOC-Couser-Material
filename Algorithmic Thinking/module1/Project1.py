'''
Project1 code about Algorithmic Thinking
'''
# !/Library/Frameworks/Python.framework/Versions/2.7/bin/Python
# -*- coding: utf-8 -*-

__author__ = "Cloga Chen(Cloga0216@gmail.com)"
__copyright__ = "Copyright (c) 2014 Cloga Chen"
__createtime__ = "2014-08-28 13:29:40"
__modifytime__ = "2014-08-28 14:32:32"

EX_GRAPH0 = {0: {1, 2}, 1: set(), 2: set()}
EX_GRAPH1 = {0: {1, 4, 5}, 1: {2, 6}, 2: {3}, 3: {0}, 4: {1}, 5: {2}, 6: set()}
EX_GRAPH2 = {
    0: {1, 4, 5}, 1: {2, 6}, 2: {3, 7}, 3: {7}, 4: {1}, 5: {2}, 6: set(),
    7: {3}, 8: {1, 2}, 9: {0, 3, 4, 5, 6, 7}}

def make_complete_graph(num_nodes):
    '''
    Takes the number of nodes num_nodes and returns a dictionary corresponding
    to a complete directed graph with the specified number of nodes.

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


def compute_in_degrees(digraph):
    '''
    Takes a directed graph digraph (represented as a dictionary) and computes
    the in-degrees for the nodes in the graph. The function should return a
    dictionary with the same set of keys (nodes) as digraph whose corresponding
    values are the number of edges whose head matches a particular node.

    Parameters
    ----------
    digraph : dict

    Returns
    -------
    graph_in_degrees : dictionary
    '''
    graph_in_degrees = {node : 0 for node in digraph}
    for ends in digraph.values():
        for end in ends:
            graph_in_degrees[end] = graph_in_degrees.get(end, 0) + 1
    return graph_in_degrees

def in_degree_distribution(digraph):
    '''
    Takes a directed graph digraph (represented as a dictionary) and computes
    the unnormalized distribution of the in-degrees of the graph. The function
    should return a dictionary whose keys correspond to in-degrees of nodes in
    the graph. The value associated with each particular in-degree is the number
    of nodes with that in-degree. In-degrees with no corresponding nodes in the
    graph are not included in the dictionary.

    Parameters
    ----------
    digraph : dict

    Returns
    -------
    in_degrees_dis : dictionary
    '''
    in_degrees_dis = {}
    graph_in_degrees = compute_in_degrees(digraph)
    for value in graph_in_degrees.values():
        in_degrees_dis[value] = in_degrees_dis.get(value, 0) + 1
    return in_degrees_dis

