import sys

from load import load_strings
from quicksort import quicksort

# CMD: python quicksort_strings.py text/Name.txt

# Create a sorted file for binary search algorithm
# CMD: python quicksort_strings.py text/Name.txt > text/Sorted_Name.txt
# Check if the file encoding=UTF-8
# python quicksort_strings.py text/Sorted_Name.txt
strings = load_strings(sys.argv[1])

sorted_strings = quicksort(strings)
for n in sorted_strings:
    print(n)
    