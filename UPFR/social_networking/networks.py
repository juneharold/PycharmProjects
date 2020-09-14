import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import numpy as np

G = nx.karate_club_graph()
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
plt.savefig("karate_graph.pdf")


N = 20
p = 0.2

# Create empty graph
# add all N nodes in the graph
# loop over all nodes and add an edge with probability p

def er_graph(N, p):
    """generate an ER graph"""
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p) == 1:
                G.add_edge(node1, node2)
    return G


nx.draw(er_graph(50, 0.08), node_size=40, node_color="gray")
plt.savefig("er1.pdf")


def plot_degree_distribution(G):
    degree_sequence = [d for n, d in G.degree()]
    plt.hist(degree_sequence, histtype="step")
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree Distribution")


G1 = er_graph(500, 0.08)
plot_degree_distribution(G1)
G2 = er_graph(500, 0.08)
plot_degree_distribution(G2)
G3 = er_graph(500, 0.08)
plot_degree_distribution(G3)
plt.savefig("hist_3.pdf")


A1 = np.loadtxt("/Users/harold/PycharmProjects/UPFR/social_networking/adj_allVillageRelationships_vilno_1.csv", delimiter=",")
A2 = np.loadtxt("/Users/harold/PycharmProjects/UPFR/social_networking/adj_allVillageRelationships_vilno_2.csv", delimiter=",")

G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)


def basic_net_stats(G):
    print("Number of nodes: %d" % G.number_of_nodes())
    print("Number of edges: %d" % G.number_of_edges())
    degree_sequence = [d for n, d in G.degree()]
    print("Average degree: %.2f" % np.mean(degree_sequence))


plot_degree_distribution(G1)
plot_degree_distribution(G2)
plt.savefig("village_hist.pdf")


gen = (G1.subgraph(c) for c in nx.connected_components(G1))

G1_LCC = max((G1.subgraph(c) for c in nx.connected_components(G1)), key=len)
G2_LCC = max((G2.subgraph(c) for c in nx.connected_components(G2)), key=len)

G1_LCC.number_of_nodes() / G1.number_of_nodes()
G2_LCC.number_of_nodes() / G2.number_of_nodes()


plt.figure()
nx.draw(G1_LCC, node_color="red", edge_color="gray", node_size=20)
plt.savefig("village1.pdf")

plt.figure()
nx.draw(G2_LCC, node_color="green", edge_color="gray", node_size=20)
plt.savefig("village2.pdf")


