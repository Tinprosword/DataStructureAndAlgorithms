import sys
import random

from numpy import less, number
from load import load_numbers

# CMD: python quicksort.py numbers/Numbers.txt 
numbers = load_numbers(sys.argv[1])

def quicksort(values):
    """
    n split
    log n sort
    
    if wrong pivot, O(n*n), just like selection_sort
    better to choose random pivot on each recursive loop
    
    best case: O(n log n)
    worst case: O(n*n)
    
    Big O Notation
    Tell you the number of times an operation is performed
    Doesn't describe the duration of operation
        If operation repeatedly, quicksort is better than merge sort
    To describe how the run time of an algorithm increase as the data set getting really big
    
    """
    # Recursively with list smaller in size
    list_length = len(values)
    if list_length <= 1:
        return values    
    # Take the pivot and split into 2 lists, left with values < pivot, right with all values > pivot
    # Break down left and right into single node and empty lists
    # Compare and the merge in left and right sorted list
    # Combine left, pivot, right into final result list
    
    less_than_pivot = []
    greater_than_pivot = []
    # better to use random pivot
    # pivot = values[0]
    randIndex = random.randint(0, list_length-1)
    pivot = values[randIndex]
    
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    # print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

# print(numbers)
sorted_numbers = quicksort(numbers)
# print(sorted_numbers)
