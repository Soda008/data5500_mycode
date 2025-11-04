#!/usr/bin/env python3
"""
hard.py

Task: Write a Python function that takes a NetworkX graph as input and returns
the number of nodes in the graph that have degree greater than 5.

Include the ChatGPT prompt used as a comment below.
"""

# ChatGPT prompt used:
# "Write a Python function that takes a NetworkX graph as input and returns
#  the number of nodes in the graph that have a degree greater than 5.
#  Include example usage that constructs a sample graph and prints the result."

import sys

try:
    import networkx as nx
except Exception as e:
    print("Missing dependency:", e)
    print("Install into your virtualenv with: python -m pip install networkx")
    sys.exit(1)


def count_high_degree_nodes(G, threshold=5):
    """
    Return the count of nodes in G whose degree is greater than `threshold`.

    For undirected graphs, degree is symmetric. For directed graphs, this uses
    the total degree (in_degree + out_degree).

    Args:
        G (networkx.Graph or networkx.DiGraph): graph instance
        threshold (int): degree threshold (default 5)

    Returns:
        int: number of nodes with degree > threshold
    """
    if G.is_directed():
        # total degree = in_degree + out_degree
        deg_iter = ((n, G.in_degree(n) + G.out_degree(n)) for n in G.nodes())
    else:
        deg_iter = ((n, G.degree(n)) for n in G.nodes())

    count = sum(1 for _, d in deg_iter if d > threshold)
    return count


# Example usage: build a sample graph and print result
if __name__ == "__main__":
    # Example 1: create a dense graph where some nodes exceed degree 5
    G = nx.Graph()
    # create 8 nodes and connect many edges to form high-degree nodes
    nodes = [f"n{i}" for i in range(8)]
    G.add_nodes_from(nodes)
    # fully connect first 6 nodes (clique) -> each will have degree 5
    for i in range(6):
        for j in range(i + 1, 6):
            G.add_edge(nodes[i], nodes[j])
    # connect a few extra edges so some nodes exceed degree 5
    G.add_edge("n0", "n6")
    G.add_edge("n1", "n7")
    G.add_edge("n2", "n7")

    print("Nodes and degrees:")
    for n in G.nodes():
        print(f"  {n}: degree={G.degree(n)}")

    result = count_high_degree_nodes(G, threshold=5)
    print("\nNumber of nodes with degree > 5:", result)

    # Example 2: If you want to test using a directed currency graph (from your assignment),
    # uncomment and adjust the following block to construct a DiGraph and test using total degree.
    #
    # H = nx.DiGraph()
    # currency_edges = [
    #     ("gbp","eur",1.1677480866819),
    #     ("gbp","usd",1.3571876014696),
    #     ("gbp","mxn",0.04568133177015),
    #     ("gbp","rub",0.0094),
    #     ("eur","usd",1.0902714982069),
    #     ("eur","inr",0.01126952353735),
    #     ("usd","inr",0.01296785741399),
    #     ("usd","rub",1.0523815231966),
    #     ("inr","rub",0.158969975),
    #     ("inr","mxn",0.0198498494559),
    #     ("rub","mxn",0.05841),
    #     ("rub","eur",0.008367232284392),
    #     ("mxn","eur",3.126244546),
    #     ("mxn","usd",0.04858),
    # ]
    # H.add_weighted_edges_from(currency_edges, weight="weight")
    # print("\nDirected currency graph total-degree result:", count_high_degree_nodes(H, threshold=5))