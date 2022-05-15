import random
import sys

from numpy import number
from load import load_numbers

"""
Bad sorting approach - just randomizes the order repeatedly until it is sorted
Unpredicted time, worst in extreme case
"""
numbers = load_numbers(sys.argv[1])

def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > index[index + 1]:
            return False
    return True    

def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        random.shuffle(values)
        attempts += 1
    print("Attempts: %s" % attempts)
    return values

print (bogo_sort(numbers))