from linked_list import LinkedList

def merge_sort(linked_list):
    """
    Sort a linked list in ascending order
    Create and return a new sorted linked list
    
    1. Divide: find the midpoint of the list and recursively divide into sublist containing single node
    2. Combine: repeatedly merge the sublists created to produce sorted sublists until 1 remains
    
    stopping condition: 
    1. single element/empty list (naively sorted)
    
    how it works:
    split the list into left and right, at index of size()//2 - 1, e.g. when size=5, midpoint=(2-1)=1, left includes (0,1), right includes(2,3,4)
    then remove linked tail at index 1, so there is no reference to index 2
    recursively, until all single node without reference
    then add fake head, determine left or right should be the next node
    after adding to the head, move the current to the node just added
    later, the remaining node head is None, then assign the rest of the remaining list to merged list
    then, discard the fake head
    return the newly merged sorted linked list
    since both of the list head are None, continue to split and then merge
    
    runs in O(kn log n)
    """
    
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at the midpoint into sublists, take floor of the list length
    return sublists - left and right
    
    case when splitting single node, right linked_list would be None
    
    Take O(k log n)
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
    else:        
        listlen = linked_list.size()
        midpoint = listlen//2
        
        # O(k)
        mid_node = linked_list.node_at_index(midpoint-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None
    
    return left_half, right_half

def merge(left, right):   
    """
    Merge 2 linked lists (arrays), sorting by data in nodes
    Return a new merged list
    i,j as indexes of each list
    
    another loop for right list is shorter than left
    another loop for left list is shorter than right
    
    takes n times, linear, O(n)
    """ 
    # Create a new linked list to contain the merged list
    mergedList = LinkedList()
    
    # Add a fake head that is discarded later
    mergedList.add(0)
    
    current = mergedList.head
    
    # Object head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head
    
    # Iterate over left and right until we reach the tail node
    while left_head or right_head:
        # If the head node of left is None, we're past the tail
        # Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next_node
        # If the head node of right is None, we're past the tail
        # Add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to False
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # Obtain node data to perform comparision operations
            left_data = left_head.data
            right_data = right_head.data    
            
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to next node
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                # Move right head to next node
                right_head = right_head.next_node       
        # Move current to next_node
        current = current.next_node
    
    # Discard fake head and set first merged node as head
    head = mergedList.head.next_node
    mergedList.head = head        
     
    return mergedList

l = LinkedList()
l.add(9)
l.add(57)
l.add(22)
l.add(8)
l.add(5)
l.add(1)
l.add(7)
l.add(99)
l.add(105)

print(l)

sorted_linked_list = merge_sort(l)

print(sorted_linked_list)