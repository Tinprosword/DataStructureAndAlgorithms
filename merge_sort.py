# from itertools import islice

def merge_sort(list):
    """
    Sort a given list in ascending order
    Create and return a new sorted list
    
    1. Divide: find the midpoint of the list and divide into sublist
    2. Conquer: recursively sort the sublist created
    3. Combine: merge the sorted sublists created
    
    stopping condition: 
    1. single element/empty list (naively sorted)
    
    takes split+merge, O(kn log n) time
    linear space, not all split simultaneously, at most requires addition space is log n < n, so it is linear
    """
    
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at the midpoint into sublists, take floor of the list length
    return sublists - left and right
    
    takes O(k log n) time
    each slice is takes O(k), recursion approach
        left = list[:midpoint]
        right = list[midpoint:]
    iterative approach, save the time cost of slice
    """
    listlen = len(list)
    midpoint = listlen//2
    # left = list[:midpoint]
    # right = list[midpoint:]
    
    left = []
    right = []
    count = 0
    # print("len: %s" % listlen)
    for i in range(0, listlen):
        if count < midpoint:
            left.append(list[i])
            # print("left: %s" % list[i])
        else:
            right.append(list[i])
            # print("right: %s" % list[i])
        count += 1
    
    return left, right

def merge(left, right):   
    """
    Merge 2 lists (arrays), sorting them in the process
    Return a new merged list
    i,j as indexes of each list
    
    another loop for right list is shorter than left
    another loop for left list is shorter than right
    
    takes n times, linear
    """ 
    list = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            list.append(left[i])
            i += 1
        else:
            list.append(right[j])
            j += 1    
    #list += left[i:]
    while i < len(left):
        list.append(left[i])
        i += 1
    #list += right[i:]
    while j < len(right):
        list.append(right[j])
        j += 1
     
    return list
    
def verify_sorted(list):
    """
    check only the first 2 elements of the list recursively
    """
    n = len(list)
    
    if n <= 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])   
    
mylist = [9, 57, 22, 8, 5, 1, 7, 99, 105]        
sortedlist = merge_sort(mylist)
print(mylist)
print(verify_sorted(mylist))
print(sortedlist)
print(verify_sorted(sortedlist))