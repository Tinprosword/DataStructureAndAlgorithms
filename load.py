# .strip() to remove newline
def load_numbers(filename):
    numbers = []
    with open(filename) as f:
        for line in f.readlines():
            numbers.append(line.strip())
    
    return numbers

def load_strings(filename):
    strings = []
    with open(filename) as f:
        for line in f.readlines():
            strings.append(line.strip())
    
    return strings