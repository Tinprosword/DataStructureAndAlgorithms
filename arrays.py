from numpy import true_divide


new_list = [1, 2, 3]
"""
memory address of the base
searching - linear vs binary
fast in accessing BUT bad in search
in operator vs for loop

insert:
true insert, linear runtime, in anywhere of the list: worst=insert in index 0
appending, constant time, numbers =[], allocated n+1 memory
memory growth pattern in python is multiple of 4, 0, 4, 8 etc..trigger resize of 4 memory
extend = set of append, O(k) where k = number of items

delete:
delete at index 0, all items has to shift to left, O(n), linear runtime
"""
result = new_list[0] 

if 1 in new_list: print(True)

for n in new_list:
    if n == 1:
        print(True)
        break
    
numbers = []
print(len(numbers))    
numbers.extend([4,5,6])
numbers.append(2)
numbers.append(200)

    