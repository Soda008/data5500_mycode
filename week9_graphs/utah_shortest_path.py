#!/usr/bin/env python3
"""
utah_shortest_path_verbose.py

Builds the same undirected weighted graph of Utah towns and prints:
 - the fastest route from LG to SG as node codes,
 - the same route as full city names,
 - each hop with its travel time,
 - and the total travel time (hours).
Saves a PNG visualization as before.
"""

import sys
from pathlib import Path

try:
    import networkx as nx
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except Exception as e:
    print("Missing dependency:", e)
    print("Install dependencies in your virtualenv with: pip install networkx matplotlib")
    sys.exit(1)

CITY_NAMES = {
    "TR": "Tremonton",
    "LG": "Logan",
    "BC": "Brigham City",
    "OG": "Ogden",
    "ED": "Eden",
    "SL": "Salt Lake City",
    "TO": "Tooele",
    "PV": "Provo",
    "PS": "Payson",
    "NP": "Nephi",
    "BV": "Beaver",
    "CC": "Cedar City",
    "SG": "St. George",
    "DL": "Delta",
    "MB": "Moab",
    "TY": "Torrey"
}

EDGES = [
    ("TR", "BC", 0.35),
    ("TR", "LG", 0.50),
    ("LG", "ED", 0.75),
    ("BC", "OG", 0.50),
    ("OG", "SL", 0.75),
    ("SL", "TO", 0.75),
    ("SL", "PV", 0.75),
    ("PV", "PS", 0.33),
    ("PS", "NP", 0.25),
    ("NP", "BV", 1.50),
    ("BV", "CC", 1.00),
    ("CC", "SG", 0.67),
    ("DL", "PV", 2.50),
    ("DL", "SG", 2.50),
    ("TY", "MB", 2.50),
    ("MB", "PV", 3.00),
    ("TY", "SG", 3.00)
]

def build_graph(edges):
    G = nx.Graph()
    for code, name in CITY_NAMES.items():
        G.add_node(code, label=name)
    G.add_weighted_edges_from(edges, weight="weight")
    return G

def visualize_graph(G, out_path="utah_graph_visual.png"):
    plt.figure(figsize=(12, 9))
    pos = nx.spring_layout(G, seed=42)
    nx.draw_networkx_nodes(G, pos, node_color="#ffffff", edgecolors="#000000", node_size=700)
    nx.draw_networkx_labels(G, pos, labels={n: n for n in G.nodes()}, font_size=10)
    nx.draw_networkx_edges(G, pos, width=1.5)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels={k: f"{v:.2f}" for k, v in edge_labels.items()}, font_size=8)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()
    return Path(out_path).resolve()

def shortest_route_verbose(G, src, dst):
    """
    Returns (codes_path, names_path, hops_list, total_time)
    where hops_list is [(u, v, weight), ...] describing each edge along the path.
    """
    try:
        codes = nx.shortest_path(G, source=src, target=dst, weight="weight")
        total = nx.shortest_path_length(G, source=src, target=dst, weight="weight")
        names = [CITY_NAMES.get(c, c) for c in codes]

        # Build hop list with weights
        hops = []
        for i in range(len(codes) - 1):
            u, v = codes[i], codes[i+1]
            w = G[u][v].get("weight", 0.0)
            hops.append((u, v, w))

        return codes, names, hops, total
    except nx.NetworkXNoPath:
        return None, None, None, None

def main():
    G = build_graph(EDGES)
    img_path = visualize_graph(G)
    print(f"Graph visualization saved to: {img_path}")

    src, dst = "LG", "SG"
    codes, names, hops, total = shortest_route_verbose(G, src, dst)

    if codes is None:
        print(f"No path found between {src} and {dst}.")
        return

    print("\nFastest route (codes):")
    print(" -> ".join(codes))

    print("\nFastest route (readable):")
    print(" -> ".join(names))

    print("\nHops and times (hours):")
    for u, v, w in hops:
        print(f"  {u} ({CITY_NAMES[u]}) -> {v} ({CITY_NAMES[v]}): {w:.2f} hours")

    print(f"\nTotal travel time: {total:.2f} hours")

if __name__ == "__main__":
    main()


