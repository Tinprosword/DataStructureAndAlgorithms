import sys

from load import load_strings
from binary_search import binary_search

# CMD: python binary_search_txt.py text/Sorted_Name.txt
strings = load_strings(sys.argv[1])

# Names looking for from the list
names = ["Trott", "Sneezy", "Zafar", "Eric"]

"""
Binary Search: O(log n)
Linear Search: O(n)
Selection Sort: O(n*n)
Quicksort: O(log n)
Merge Sort: O(n log n)
"""
for name in names:
    index = binary_search(strings, name)
    # print(index)