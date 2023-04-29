#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers

"""

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    A peak is defined as an element that is greater than or equal to its neighbors.
    """
    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    if n == 2:
        return max(list_of_integers)
    for i in range(1, n-1):
        if list_of_integers[i] >= list_of_integers[i-1] and list_of_integers[i] >= list_of_integers[i+1]:
            return list_of_integers[i]
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[n-1] >= list_of_integers[n-2]:
        return list_of_integers[n-1]
    return None
