# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map(mapFilename):            
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    # TODO
    map_graph = WeightedDigraph()
    with open(mapFilename, 'r') as mapfile:
        for line in mapfile:
            items = line.split()
            src = Node(items[0])
            dest = Node(items[1])
            total = round(float(items[2]),1)
            outdoor = round(float(items[3]),1)
            if not map_graph.hasNode(src):
                map_graph.addNode(src)
            if not map_graph.hasNode(dest):
                map_graph.addNode(dest)
            edge = WeightedEdge(src, dest, total, outdoor)
            map_graph.addEdge(edge)
    print "Loading map from file..."
    return map_graph
        

#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize total dist and dist outdoor
# and what the constraints are valid path less than maxTotalDist maxDistOutdoors
#

def get_all_valid_path(digraph, start, end):
    '''
    use depth-first to find all valid path
    find all possible path from start, parent > children,
    if chidren of node is end, add to valid_path, delete from queue
    if all children of node is already in path, delete from queue
    '''
    queue = []
    valid_path = []
    queue.append([start])
    while queue:
        current_path = queue.pop(-1)
        if current_path[-1] == end:
            valid_path.append(current_path)
        current_node = current_path[-1]
        current_children = digraph.childrenOf(Node(current_node))
        for node in current_children:
            if str(node) not in current_path: #avoid cycles
                newpath = current_path + [str(node)]
                queue.append(newpath)
    return valid_path



def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    all_valid_path = get_all_valid_path(digraph, start, end)
    shortest_path = []
    shortest_dist = float('inf')
    for path in all_valid_path:
        total_dist = 0
        outdoor_dist = 0
        for index, n in enumerate(path[:-1]):
            for dest, (total, outdoor) in digraph.edges[Node(n)]:
                if str(dest) == path[index+1]:
                    total_dist += total
                    outdoor_dist += outdoor
                    break
        if (total_dist <= maxTotalDist) & (outdoor_dist <= maxDistOutdoors) & (total_dist <= shortest_dist):
            shortest_path = path
            shortest_dist = total_dist
    if not shortest_path:
        raise ValueError
    return shortest_path

#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#


def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
    not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    queue = []
    shortest_path = []
    shortest_dist = float('inf')
    queue.append([[start], 0, 0])
    edges = digraph.edges
    while queue:
        # print 'queue', queue
        current_path_object = queue.pop(-1)
        current_path = current_path_object[0]
        current_node = current_path[-1]
        current_edges = digraph.edges[Node(current_node)]
        # print 'current_edges', current_edges
        for edge in current_edges:
            # print 'current_edge', edge
            total_dist = current_path_object[1]
            outdoor_dist = current_path_object[2]
            # print current_node, '>' , edge[0]
            if str(edge[0]) not in current_path: #avoid cycles
                newpath = current_path + [str(edge[0])]
                total_dist += edge[1][0]
                outdoor_dist += edge[1][1]
                # print 'current_path', current_path
                # print 'newpath', newpath
                # print 'total_dist', total_dist
                # print 'outdoor_dist', outdoor_dist
                # calculate new edges dist
                # if total_dist, outdoor_dist exceed constain or total_dist exceed shortest_dist
                # break
                if (total_dist > maxTotalDist) | (outdoor_dist > maxDistOutdoors) | (total_dist > shortest_dist):
                    continue
                queue.append([newpath, total_dist, outdoor_dist])
                if str(edge[0]) == end:
                    shortest_path = newpath
                    shortest_dist = total_dist
    if not shortest_path:
        raise ValueError
    return shortest_path

map5 = WeightedDigraph()
map5.addNode(Node('1'))
map5.addNode(Node('2'))
map5.addNode(Node('3'))
map5.addNode(Node('4'))
map5.addNode(Node('5'))
map5.addEdge(WeightedEdge(Node('1'), Node('2'), 5, 2))
map5.addEdge(WeightedEdge(Node('3'), Node('5'), 6, 3))
map5.addEdge(WeightedEdge(Node('2'), Node('3'), 20, 10))
map5.addEdge(WeightedEdge(Node('2'), Node('4'), 10, 5))
map5.addEdge(WeightedEdge(Node('4'), Node('3'), 2, 1))
map5.addEdge(WeightedEdge(Node('4'), Node('5'), 20, 10))

directedDFS(map5, "1", "3", 17, 8)

# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####

# Test cases
# mitMap = load_map("mit_map.txt")
# print isinstance(mitMap, Digraph)
# print isinstance(mitMap, WeightedDigraph)
# print 'nodes', mitMap.nodes
# print 'edges', mitMap.edges


# LARGE_DIST = 1000000

# # Test case 1
# print "---------------"
# print "Test case 1:"
# print "Find the shortest-path from Building 32 to 56"
# expectedPath1 = ['32', '56']
# brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
# dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
# print "Expected: ", expectedPath1
# print "Brute-force: ", brutePath1
# print "DFS: ", dfsPath1
# print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

# # Test case 2
# print "---------------"
# print "Test case 2:"
# print "Find the shortest-path from Building 32 to 56 without going outdoors"
# expectedPath2 = ['32', '36', '26', '16', '56']
# brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
# dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
# print "Expected: ", expectedPath2
# print "Brute-force: ", brutePath2
# print "DFS: ", dfsPath2
# print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

# # Test case 3
# print "---------------"
# print "Test case 3:"
# print "Find the shortest-path from Building 2 to 9"
# expectedPath3 = ['2', '3', '7', '9']
# brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
# dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
# print "Expected: ", expectedPath3
# print "Brute-force: ", brutePath3
# print "DFS: ", dfsPath3
# print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

# # Test case 4
# print "---------------"
# print "Test case 4:"
# print "Find the shortest-path from Building 2 to 9 without going outdoors"
# expectedPath4 = ['2', '4', '10', '13', '9']
# brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
# dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
# print "Expected: ", expectedPath4
# print "Brute-force: ", brutePath4
# print "DFS: ", dfsPath4
# print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

# # Test case 5
# print "---------------"
# print "Test case 5:"
# print "Find the shortest-path from Building 1 to 32"
# expectedPath5 = ['1', '4', '12', '32']
# brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
# dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
# print "Expected: ", expectedPath5
# print "Brute-force: ", brutePath5
# print "DFS: ", dfsPath5
# print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

# # Test case 6
# print "---------------"
# print "Test case 6:"
# print "Find the shortest-path from Building 1 to 32 without going outdoors"
# expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
# brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
# dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
# print "Expected: ", expectedPath6
# print "Brute-force: ", brutePath6
# print "DFS: ", dfsPath6
# print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

# # Test case 7
# print "---------------"
# print "Test case 7:"
# print "Find the shortest-path from Building 8 to 50 without going outdoors"
# bruteRaisedErr = 'No'
# dfsRaisedErr = 'No'
# try:
#     bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
# except ValueError:
#     bruteRaisedErr = 'Yes'

# try:
#     directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
# except ValueError:
#     dfsRaisedErr = 'Yes'

# print "Expected: No such path! Should throw a value error."
# print "Did brute force search raise an error?", bruteRaisedErr
# print "Did DFS search raise an error?", dfsRaisedErr

# # Test case 8
# print "---------------"
# print "Test case 8:"
# print "Find the shortest-path from Building 10 to 32 without walking"
# print "more than 100 meters in total"
# bruteRaisedErr = 'No'
# dfsRaisedErr = 'No'
# try:
#     bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
# except ValueError:
#     bruteRaisedErr = 'Yes'

# try:
#     directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
# except ValueError:
#     dfsRaisedErr = 'Yes'

# print "Expected: No such path! Should throw a value error."
# print "Did brute force search raise an error?", bruteRaisedErr
# print "Did DFS search raise an error?", dfsRaisedErr
