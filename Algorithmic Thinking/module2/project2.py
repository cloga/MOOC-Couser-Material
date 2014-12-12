'''
Project 2 - Connected components and graph resilience
'''
# !/Library/Frameworks/Python.framework/Versions/2.7/bin/Python
# -*- coding: utf-8 -*-

__author__ = "Cloga Chen(Cloga0216@gmail.com)"
__copyright__ = "Copyright (c) 2014 Cloga Chen"
__createtime__ = "2014-09-14 09:48:28"
__modifytime__ = "2014-09-16 18:50:12"

def delete_node(ugraph, node_del):
    '''
    delete a node from undirected graph
    '''
    ugraph_return = {}
    for node in ugraph.keys():
        neighbour = ugraph[node]
        if node_del in neighbour:
            neighbour.remove(node_del)
        if node != node_del:
            ugraph_return[node] = neighbour
    return ugraph_return

def bfs_visited(ugraph, start_node):
    '''
    Takes the undirected graph ugraph and the start_node and returns the
    set consisting of all nodes that are visited by a breadth-first search
    that starts at start_node

    Parameters
    ----------
    ugraph : dict, g=(V, E)

    start_node : key, start_node in E

    Returns
    -------
    visited : set of visited nodes
    '''
    from collections import deque
    queue = deque([start_node])
    visited = {start_node}
    while queue:
        node = queue.popleft()
        for neig in ugraph[node]:
            if neig not in visited:
                visited.add(neig)
                queue.append(neig)
    return visited

def cc_visited(ugraph):
    '''
    Takes the undirected graph ugraph and returns a list of sets, where each
    set consists of all the nodes (and nothing else) in a connected component,
    and there is exactly one set in the list for each connected component in
    ugraph and nothing else.

    Parameters
    ----------
    ugraph : dict, g=(V, E)

    Returns
    -------
    con_c : list of sets,list of connected component
    '''
    remainings = set(ugraph.keys())
    con_c = []
    while remainings:
        for node in remainings:
            nodes_visited = bfs_visited(ugraph, node)
            con_c.append(nodes_visited)
            remainings = remainings - nodes_visited
            break
    return con_c

def largest_cc_size(ugraph):
    '''
    Takes the undirected graph ugraph and returns the size (an integer) of the
    largest connected component in ugraph

    Parameters
    ----------
    ugraph : dict, g=(V, E)

    Returns
    -------
    large_size : integer, size of the largest connected component in ugraph
    '''
    con_cs = cc_visited(ugraph)
    max_size = max([len(conc) for conc in con_cs]) if con_cs else 0
    return max_size

def compute_resilience(ugraph, attack_order):
    '''
    Takes the undirected graph ugraph, a list of nodes attack_order and
    iterates through the nodes in attack_order. For each node in the list, the
    function removes the given node and its edges from the graph and then
    computes the size of the largest connected component for the resulting
    graph.
    The function should return a list whose k+1th entry is the size of the
    largest connected component in the graph after the removal of the first k
    nodes in attack_order. The first entry (indexed by zero) is the size of the
    largest connected component in the original graph.

    Parameters
    ----------
    ugraph : dict, g=(V, E)
    attack_order : list of nodes

    Returns
    -------
    remains_size : list, k+1th length size of the largest connected component
    in the graph
    '''
    remains_size = [largest_cc_size(ugraph)]
    for node in attack_order:
        ugraph = delete_node(ugraph, node)
        remains_size.append(largest_cc_size(ugraph))
    return remains_size
