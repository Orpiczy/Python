# <Łukasz> <Orpik>, <302892>

import timeit
from typing import List, Tuple, Callable, Set, Dict, Deque
from collections import deque
from timeit import timeit
import random

A = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 2, 0]
]
G = {
    1: [2, 3, 5],
    2: [1, 4, 6],
    3: [1, 7],
    4: [2],
    5: [1, 6],
    6: [2, 5],
    7: [3]
}


def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    adjlist = {}
    for main_v, list in enumerate(adjmat, 1):
        adjlist[main_v] = []
        for sub_v, edges in enumerate(list, 1):
            for n in range(edges):
                adjlist[main_v].append(sub_v)
    return adjlist


def dfs_recursive(G: Dict[int, List[int]], v: int, visited: List[int] = None) -> List[int]:
    if visited is None:
        visited = []

    visited.append(v)
    print(visited)
    for s in G[v]:
        if s not in visited:
            dfs_recursive(G, s, visited)
    return visited


def dfs_iterative(G: Dict[int, List[int]], v: int, ) -> List[int]:
    visited = []
    stack = deque(v)

    while len(stack) != 0:
        visited.append(v)
        v = stack.pop(0)
        for s in G[v]:
            if s not in visited:
                stack.append(s)

    return visited

Dict_G = adjmat_to_adjlist(A)
print(dfs_recursive(G, 1))
print(dfs_iterative(G, 1))
