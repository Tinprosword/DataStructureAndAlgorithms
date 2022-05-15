import sys 

from load import load_numbers

"""
Still slow but more efficient than bogo sort
move each minimum node to sorted list

measure the time, use the terminal command
time python selection_sort.py numbers/Numbers.txt
add the user+sys time, as real time could vary

takes O(1/2 n*n) as fewer items are left for comparison
when n goes big, 1/2 constant becomes insignificant, O(n*n)
"""

numbers = load_numbers(sys.argv[1])

def selection_sort(values):
    sorted_list = []
    print("%25s %-25s" % (values,sorted_list))
    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
    print("%25s %-25s" % (values,sorted_list))
    return sorted_list

def index_of_min(values):
    min_index = 0
    for i in range(0, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index            
        