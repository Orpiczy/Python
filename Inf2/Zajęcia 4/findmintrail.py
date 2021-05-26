#!/usr/bin/python
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Tuple, Callable, Set, Dict, Deque, NamedTuple

from collections import deque
from enum import Enum, auto

VertexID = int
Distance = int


class TrailSegmentEntry(NamedTuple):
    VertexID_start: int
    VertexID_end: int
    Edge_ID: int
    Edge_Weight: float


Trail = List[TrailSegmentEntry]


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
    print('graphddetail', graph_detail)
    g = nx.MultiDiGraph()
    g.add_weighted_edges_from(graph_detail)

    return g


def find_min_trail(g: nx.MultiDiGraph, v_start: VertexID, v_end: VertexID):
    print(g)
    short_path = nx.dijkstra_path(g, v_start, v_end)

    result = []

    for el in range(len(short_path) - 1):
        weights = []

        for edge in G[short_path[el]][short_path[el + 1]].keys():
            weights.append(G[short_path[el]][short_path[el + 1]][edge]['weight'])

        min_weight = min(weights)

        edge_id = 0

        for edge in G[short_path[el]][short_path[el + 1]].keys():
            if min_weight == G[short_path[el]][short_path[el + 1]][edge]['weight']:
                edge_id = edge

        result.append(TrailSegmentEntry(short_path[el], short_path[el + 1], edge_id, min_weight))

    return result


def trail_to_str(trail: Trail) -> str:
    result_str = ''
    total = 0
    for val in trail:
        result_str += '{0:d} -[{1:d}:{2:.1f}]-> '.format(val[0], val[2], val[3])
        total += val[3]

    result_str += ' (total = {:.1f})'.format(total)

    return result_str


G = nx.MultiDiGraph()
G.add_weighted_edges_from(
    [(1, 2, 0.3), (2, 4, 0.2), (4, 6, 0.7), (6, 8, 0.2), (1, 3, 0.4), (3, 5, 0.1), (5, 7, 0.3), (7, 8, 0.3),
     (8, 9, 0.1), (8, 10, 0.2), (9, 11, 0.3), (9, 11, 0.3), (10, 11, 0.4)])
load_multigraph_from_file('dijkstra_multi_2.dat')
Trail_of_graph = find_min_trail(G, 1, 11)

print(trail_to_str(Trail_of_graph))
