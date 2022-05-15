from locale import currency
from cv2 import add


class Node:
    """
    array - insert and delete are linear time
    linked list - linear data structure, head and reference to next block, better if lots of insert and delete
    efficient in insert at only head or tail. prepend, append
    
    An object for storing a single node of a linked list.
    Models 2 attributes - data and the link to the next node in the list
    """
    
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        """
        Return a string representation of the node
        Takes O(n) time
        """
        return "<Node data: %s>" % self.data    

class LinkedList:
    """
    Singly linked list, check if list empty
    doubly linked
    """
    def __init__(self):
        self.head = None    
        
    def is_empty(self):
        return self.head == None    
    
    def size(self):
        """
        Return the number of nodes in the list
        Loop to increase counter when current != None        
        """    
        current = self.head
        count = 0
        
        while current:
            count += 1
            current = current.next_node
        
        return count    
     
    def add(self, data):
         """
         Add new Node at head of the list, takes O(1) times
         insert/delete, update few of reference, constant time
         """
         new_node = Node(data)
         new_node.next_node = self.head
         self.head = new_node 
    
    def insert(self, data, index):
         """
         Add new Node at the index of the list, then change previous and next node reference
         insert/delete, update few of reference, constant time O(1)
         Finding the node at the insertion point is linear O(n)
         Overall runtime O(n)
         
         LinkedList = last-in first out
         e.g. add(2) > add(5) > add(10)
         Head=10, 5, Tail=2
         when insert(8) to index 1:
            prev_node=10
            next_node=5
            result = Head=10, 8, 5, Tail=2
         when inset(20) to index 3:
            prev_node=5
            next_node=2
            result = Head=10, 8, 5, 20, Tail=2   
         """
         if index == 0:
            self.add(data)

         if index > 0:
            new_node = Node(data)
            
            position = index
            current = self.head
            
            while position > 1:
                current = current.next_node
                position -= 1
            prev_node = current
            next_node = current.next_node
            
            prev_node.next_node = new_node
            new_node.next_node = next_node    

    def remove(self, key):
        """
        Remove node containing data that matches the key
        Return the node or None if key doesn't exists
        Take O(n) time
        If node has no reference, it will be removed automatically
        
        e.g. add(2) > add(5) > add(10) > add(8)
        when remove(10):
            prev_node = 5
            current = 10
            5.next_node = 10.next_node = 8
            node 10 reference is lost and then removed
        when remove(99):
            node 99 does not exists and no action taken so there is no change in the list   
        """
        current = self.head
        prev_node = None
        found = False
        
        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node        
            elif current.data == key:
                found = True
                prev_node.next_node = current.next_node
            else:
                prev_node = current
                current = current.next_node
        
        return current
    
    def removeAtIndex(self, index):
        """
        Remove node containing data at the index
        Return the node or None if key doesn't exists
        Take O(n) time
        If node has no reference, it will be removed automatically
        
        e.g. add(2) > add(5) > add(10) > add(8)
        [Head: 8]-> [10]-> [5]-> [Tail: 2]
        when remove(2):
            prev_node = 5
            current = 10
            next_node = 8
            5.next_node = 10.next_node = 8
            node 10 reference is lost and then removed
        when remove(99):
            node 99 does not exists and no action taken so there is no change in the list   
            when next_node is None, it reach end of the list, no need to go further
        """
        current = self.head
        prev_node = None
        next_node = None
        is_end = False
        
        if index == 0:
            next_node = current.next_node
            self.head = next_node
            
        if index > 0:
            position = index
            
            while position > 1 and not is_end:
                current = current.next_node
                position -= 1
                
                if current.next_node is None: 
                    is_end = True
                    
            prev_node = current
            if not is_end:                
                next_node = current.next_node                
                prev_node.next_node = next_node.next_node

        return next_node
    
    def search(self, key):
        """
        Search for the first node containing data that matches the  key
        Return None if not found
        Take O(n), linear time
        """
        current = self.head
        
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
            
        return None
    
    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
        
        while position < index:
            current = current.next_node
            position += 1
        
        return current        
    
    def __repr__(self):
        """
        Return a string representation of the list
        add to list until it reach the tail, then join into 1 string output, with the char pattern in between
        Takes O(n) time
        """
        # return "<Node data: %s>" % self.data    
        nodes = []
        current = self.head
        
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)    
            
            current = current.next_node
            
        return '-> '.join(nodes)    
        