# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    length_A = len(A)
    counters = [0] * length_A
    max_counter = 0
    for i in A :
        if i > length_A:
            return 0
        counters[i - 1] += 1
        if counters[i - 1] > max_counter :
            max_counter = counters[i - 1]
    if all(counters) and max_counter == 1 :
        return 1
    else :
        return 0
