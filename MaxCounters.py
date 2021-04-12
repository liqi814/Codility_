# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    # time complexity: O(N*M)
    counters = [0] * N
    for i in A:
        if i >= 1 and i <= N :
            counters[i-1] += 1
        elif i == N + 1:
            counters = [max(counters)] * N
        #print(counters)
    return(counters)
    pass
