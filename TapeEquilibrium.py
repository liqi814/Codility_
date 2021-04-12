# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    #time complexity:O(N)
    current_diff= sum(A)
    min_diff=float('inf')
    for i in range(0, len(A)-1):
        current_diff = current_diff - 2 * A[i]
        min_diff = min(min_diff, abs(current_diff))
    return(min_diff)
    pass
