import sys

from numpy import number
from load import load_numbers
from merge_sort import merge, merge_sort
numbers = load_numbers(sys.argv[1])

"""
To compare the performance with quicksort

O(n log n)

Performance
quicksort > merge_sort > selection > bogo
"""
print(numbers)
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)