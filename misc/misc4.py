"""
Common Gotcha - mutable default arguments (BAD)
"""
def append(x, l=None):
    """
    Custom list append function
    """
    if l is None:
        l = []
    l.append(x)
    return l


l_1 = append(1)  # expect [1]


l_2 = append(2)  # expect [2]

print(l_1)
print(l_2)
