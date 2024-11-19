import networkx as nx
import matplotlib.pyplot as plt

# Create a sample graph
G = nx.Graph()

# Add edges (creates nodes automatically)
G.add_edges_from([
    (1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (5, 6), (5, 7), (6, 7)
])

# Degree Centrality
degree_centrality = nx.degree_centrality(G)
print("Degree Centrality:", degree_centrality)

# In-Degree Centrality
try:
    in_degree_centrality = nx.in_degree_centrality(G)
    print("In-Degree Centrality:", in_degree_centrality)
except:
    print("In-Degree Centrality is not available for undirected graphs.")

# Betweenness Centrality
betweenness_centrality = nx.betweenness_centrality(G)
print("Betweenness Centrality:", betweenness_centrality)

# Closeness Centrality
closeness_centrality = nx.closeness_centrality(G)
print("Closeness Centrality:", closeness_centrality)

# Eigenvector Centrality
eigenvector_centrality = nx.eigenvector_centrality(G)
print("Eigenvector Centrality:", eigenvector_centrality)

# PageRank (for directed graphs, but works for undirected too)
pagerank = nx.pagerank(G)
print("PageRank:", pagerank)


# Visualize the graph
pos = nx.spring_layout(G)  # Layout for visualization
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=15)
plt.show()