# see http://networkx.lanl.gov/ for a tutorial on NetworkX
import networkx as nx

# your GML file
filename = 'LadaFacebookAnon.gml'

# read in the graph using networkX
G = nx.read_gml(filename,relabel=True)

# check out the functions number_of_nodes, number_of_edges,
# connected_component_subgraphs, degree_centrality,number_connected_components
# to answer the hw 1 questions about your network

# for example to get the number of nodes:
num_nodes = G.number_of_nodes()
print 'number of nodes: ' + str(num_nodes)
largestCC = nx.connected_component_subgraphs(G)[0]

largestCC.number_of_nodes()

max(nx.degree(G).values())