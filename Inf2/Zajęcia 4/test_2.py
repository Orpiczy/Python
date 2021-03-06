# !/usr/bin/python
# -*- coding: utf-8 -*-
# <Łukasz> <Orpik>, <302892>

from typing import List, Tuple, Callable, Set, Dict, Deque, NamedTuple
from collections import deque
from enum import Enum, auto
import networkx as nx
import matplotlib.pyplot as plt

Distance = int
VertexID = int
AdjList = Dict[VertexID, List[VertexID]]


class TrailSegmentEntry(NamedTuple):
    VertexID_start: int
    VertexID_end: int
    Edge_ID: int
    Edge_Weight: float


Trail = List[TrailSegmentEntry]


class Color(Enum):
    white = 0
    grey = 1
    black = 2


def bfs(g: Dict[int, List[int]], v: int, ) -> List[int]:
    colors = {}
    visited = []
    for key in g.keys():
        colors[key] = Color.white

    colors[v] = Color.grey

    stack = deque([v])
    while len(stack) != 0:
        v = stack.popleft()
        visited.append(v)

        if v in g.keys():
            for n in g[v]:
                try:
                    var = colors[n] == Color.white
                except KeyError:
                    colors[n] = Color.white
                    var = True

                if var:
                    colors[n] = Color.grey
                    stack.append(n)
            colors[v] = Color.black
    return visited


def neighbors(adjlist: AdjList, start_vertex_id: VertexID, max_distance: Distance) -> Set[VertexID]:
    colors = {}
    visited = []
    for key in adjlist.keys():
        colors[key] = Color.white

    colors[start_vertex_id] = Color.grey

    stack = deque([(start_vertex_id, 0)])
    while len(stack) != 0:
        v = stack.popleft()

        if v[1] > max_distance:
            return set(visited[1:])

        visited.append(v[0])
        for n in adjlist[v[0]]:
            try:
                var = colors[n] == Color.white
            except KeyError:
                colors[n] = Color.white
                var = True

            if var:
                colors[n] = Color.grey
                stack.append((n, v[1] + 1))
        colors[v[0]] = Color.black

    return set(visited[1:])


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
