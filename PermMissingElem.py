# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    missing_ele = 0
    for i in range(1, len(A)+2) :
        missing_ele ^= i
    for i in A :
        missing_ele ^= i
    return missing_ele
    pass
