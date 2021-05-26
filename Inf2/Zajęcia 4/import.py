#!/usr/bin/python
# -*- coding: utf-8 -*-


import networkx as nx
import matplotlib.pyplot as plt


def load_multigraph_from_file(filename: str) -> nx.MultiDiGraph:
    file = open(filename, 'r+')
    graph_detail = []
    for each in file:

        if each.isspace():
            continue

        each = each.split()
        each_tuple = ()

        for count, n in enumerate(each):
            if count == 2:
                each_tuple = each_tuple + (float(n),)
                continue
            each_tuple = each_tuple + (int(n),)
        graph_detail.append(each_tuple)
    print(graph_detail)
    G = nx.DiGraph()
    G.add_weighted_edges_from(graph_detail)
    pos = nx.spring_layout(G)
    nx.draw(G, pos=pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
    plt.show()

    return G


load_multigraph_from_file('dijkstra_multi_2.dat')
