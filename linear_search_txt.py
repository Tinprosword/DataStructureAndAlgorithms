import sys

from load import load_strings

# CMD: python linear_search_txt.py text/Name.txt
strings = load_strings(sys.argv[1])

print(strings)

def index_of_item(collection, target):
    for i in range(0, len(collection)):
        if target == collection[i]:
            return i
    # return None when not exists in list
    return None    

# Names looking for from the list
names = ["Trott", "Sneezy", "Zafar", "Eric"]
for n in names:
    index = index_of_item(strings, n)
    # print(index)