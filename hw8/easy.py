#!/usr/bin/env python3
"""
easy.py

Task: Write a Python function that takes a NetworkX graph as input and returns
the number of nodes in the graph.

Include the ChatGPT prompt used as a comment below.
"""

# ChatGPT prompt used:
# "Write a Python function that takes a NetworkX graph as input and returns
#  the number of nodes in the graph. Include a short example showing the
#  function in use."

import sys

try:
    import networkx as nx
except Exception as e:
    print("Missing dependency:", e)
    print("Install into your virtualenv with: python -m pip install networkx")
    sys.exit(1)


def count_nodes(G):
    """
    Return the number of nodes in NetworkX graph G.

    Args:
        G (networkx.Graph or networkx.DiGraph): graph instance

    Returns:
        int: number of nodes
    """
    return G.number_of_nodes()


# Example usage: build a small graph if run as a script
if __name__ == "__main__":
    # If an edges.txt file exists in the same folder with lines like "a,b,1",
    # you can uncomment the file-loading code below. Otherwise we build a small sample graph.
    #
    # import os
    # p = os.path.join(os.path.dirname(__file__), "edges.txt")
    # if os.path.exists(p):
    #     G = nx.DiGraph()
    #     with open(p) as f:
    #         for line in f:
    #             a, b, w = line.strip().split(",")
    #             G.add_edge(a, b, weight=float(w))
    # else:
    #     G = nx.path_graph(5)  # sample undirected graph with 5 nodes

    # sample graph (path of 5 nodes)
    G = nx.path_graph(5)
    print("Graph nodes:", G.nodes())
    print("Number of nodes (count_nodes):", count_nodes(G))