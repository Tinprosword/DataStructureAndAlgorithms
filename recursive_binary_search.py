def recursive_binary_search(list, target):
    """
    Return true if the index position of the target found, else call the function again by passing new list
    case 1: item < target
        new list starting from midpoint+1, up to end of list
    case 2: item > target
        new list starting from 0, up to midpoint
    Required list in sorted
    Stop condition is important, always return in recursive call
    Recursive depth = no. of time calling function itself
    space complexity = O(log n)
    tail optimization = last stack of code is recursive
    iterative >> recursive as space complexity is constant
    """
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2
        
        if list[midpoint] == target:
            return True
        else: 
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)   
            else:
                return recursive_binary_search(list[0:midpoint], target)         


def verify(result):
    print("Target found: ", result)
 

numbers = [1,2,3,4,5,6,7,8,9,10]

result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)