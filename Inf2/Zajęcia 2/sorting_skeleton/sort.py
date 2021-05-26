# <Łukasz> <Orpik>, <302892>
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

print(bubblesort( [5,2, 3, 1, 4]))

list_random = random.sample(range(10001), 1000)

list_sorted = list_random[:]
list_sorted.sort()

list_sorted_inv = list_random[:]
list_sorted_inv.sort(reverse=True)

nr_equal = random.randrange(1, 1001)
list_equal = [nr_equal for i in range(1000)]

for x in range(10):
    bubble_time_1 = +timeit('bubblesort(list_random)', number=1, globals=globals())

bubble_time_1 = bubble_time_1 / 10
print('Bubblesort random list: {}'.format(bubble_time_1))

for x in range(10):
    quick_time_1 = +timeit('quicksort(list_random)', number=1, globals=globals())

quick_time_1 = quick_time_1 / 10
print('Quicksort random list: {}'.format(quick_time_1))

for x in range(10):
    bubble_time_2 = +timeit('bubblesort(list_sorted)', number=1, globals=globals())

bubble_time_2 = bubble_time_2 / 10
print('Bubblesort sorted list: {}'.format(bubble_time_2))

for x in range(10):
    quick_time_2 = +timeit('quicksort(list_sorted)', number=1, globals=globals())

quick_time_2 = quick_time_2 / 10
print('Quicksort sorted list: {}'.format(quick_time_2))

for x in range(10):
    bubble_time_3 = +timeit('bubblesort(list_sorted_inv)', number=1, globals=globals())

bubble_time_3 = bubble_time_3 / 10
print('Bubblesort sorted_inv list: {}'.format(bubble_time_3))

for x in range(10):
    quick_time_3 = +timeit('quicksort(list_sorted_inv)', number=1, globals=globals())

quick_time_3 = quick_time_3 / 10
print('Quicksort sorted_inv list: {}'.format(quick_time_3))

for x in range(10):
    bubble_time_4 = +timeit('bubblesort(list_equal)', number=1, globals=globals())

bubble_time_4 = bubble_time_4 / 10
print('Bubblesort equal list: {}'.format(bubble_time_4))

for x in range(10):
    quick_time_4 = + timeit('quicksort(list_equal)', number=1, globals=globals())

quick_time_4 = quick_time_4 / 10
print('Quicksort equal list: {}'.format(quick_time_4))

