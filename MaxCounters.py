# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    # time complexity: O(N*M)
    # performance: 77 %
    counters = [0] * N
    for i in A:
        if i >= 1 and i <= N :
            counters[i-1] += 1
        elif i == N + 1:
            counters = [max(counters)] * N
        #print(counters)
    return(counters)
    pass

def solution(N, A):
    # write your code in Python 3.6
    # performance: 77 %
    counters = [0] * N
    max_counter = 0
    for i in A:
        if i >= 1 and i <= N :
            counters[i-1] += 1
            max_counter = max(max_counter, counters[i-1])
        elif i == N + 1:
            counters = [max_counter] * N
    return(counters)
    pass
