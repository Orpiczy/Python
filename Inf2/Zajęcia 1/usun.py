#!/usr/bin/python
# -*- coding: utf-8 -*-

import timeit
from typing import List, Tuple, Callable, Set, Dict
from timeit import timeit
import random


def quicksort(list_to_sort: List[int]):
    list_sorted = list_to_sort[:]
    return quicksort_core(list_sorted)


def quicksort_core(list_sorted: List[int], i: int = 0, j: int = -1) -> List[int]:
    if j == -1:
        j = len(list_sorted) - 1

    pivot = list_sorted[(i + j) // 2]
    i_start = i
    j_start = j

    while i <= j:

        if list_sorted[j] <= pivot <= list_sorted[i] and i <= j:
            list_sorted[i], list_sorted[j] = list_sorted[j], list_sorted[i]
            i += 1
            j -= 1

        while list_sorted[i] < pivot and i <= j:
            i += 1

        while list_sorted[j] > pivot and i <= j:
            j -= 1

    if i_start < j:
        quicksort_core(list_sorted, i_start, j)

    if j_start > i:
        quicksort_core(list_sorted, i, j_start)

    return list_sorted


def bubblesort(list_to_sort: List[int]) -> Tuple[List[int], int]:
    list_sorted = list_to_sort[:]
    changes = 0
    change = 1
    loop = 0

    while change != 0:
        change = 0

        for i in range(len(list_sorted) - 1-loop):
            changes += 1
            if list_sorted[i] > list_sorted[i + 1]:
                list_sorted[i], list_sorted[i + 1] = list_sorted[i + 1], list_sorted[i]
                change += 1
        loop += 1

    return list_sorted, changes