# !/usr/bin/python
# -*- coding: utf-8 -*-
# <Łukasz> <Orpik>, <302892>

from typing import List, Tuple, Callable, Set, Dict, Deque
from collections import deque
from enum import Enum, auto

G = {
    1: [2, 4],
    2: [3],
    4: [5],
    5: [2, 6],
    7: [1],
}
G_1 = {
    1: [2, 3, 4],
    2: [1, 5, 6, 7],
    3: [1, 7, 8],
    4: [1, 9],
    5: [2],
    6: [2],
    7: [2, 3],
    8: [3],
    9: [4]
}


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
        for n in g[v]:
            if colors.get(n) == Color.white:
                colors[n] = Color.grey
                stack.append(n)
        colors[v] = Color.black

    return visited




VertexID = int
AdjList = Dict[VertexID, List[VertexID]]
Distance = int


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
                continue

            if var:
                colors[n] = Color.grey
                stack.append((n, v[1] + 1))
        colors[v[0]] = Color.black

    return set(visited[1:])


print(neighbors(G, 1, 1))
print(bfs(G, 1))
