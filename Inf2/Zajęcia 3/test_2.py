#!/usr/bin/python
# -*- coding: utf-8 -*-

import timeit
from typing import List, Tuple, Callable, Set, Dict, Deque
from collections import deque
from timeit import timeit
import random


def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    adjlist = {}
    for main_v, list_v in enumerate(adjmat, 1):
        adjlist[main_v] = []
        for sub_v, edges in enumerate(list_v, 1):
            for n in range(edges):
                adjlist[main_v].append(sub_v)
    return {k: v for k, v in adjlist.items() if v}


def dfs_recursive(g: Dict[int, List[int]], v: int, visited: List[int] = None) -> List[int]:
    if visited is None:
        visited = []

    visited.append(v)
    for s in g[v]:
        if s not in visited:
            dfs_recursive(g, s, visited)
    return visited


def dfs_iterative(g: Dict[int, List[int]], v: int) -> List[int]:
    visited = []
    stack = deque([v])

    while len(stack) != 0:
        v = stack.popleft()
        if v not in visited:
            visited.append(v)
            for s in reversed(g[v]):
                if s not in visited:
                    stack.appendleft(s)

    return visited


def is_acyclic(g: Dict[int, List[int]]) -> bool:
    for v_checked in g.keys():
        visited = []
        stack = deque([v_checked])

        while len(stack) != 0:
            v = stack.popleft()
            if v not in visited:
                visited.append(v)
                for s in reversed(g[v]):
                    if v_checked == s:
                        return False
                    stack.appendleft(s)

    return True


adjmat = [[0, 1], [0, 0]]
result = adjmat_to_adjlist(adjmat)
print(result)
