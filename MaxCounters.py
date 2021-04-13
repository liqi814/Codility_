# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    #  time complexity: O(N + M)
    counters = [0] * N
    max_result = current_max = 0
    for num in A :
        if num <= N :
            if counters[num -1] < max_result :
                counters[num -1] = max_result
            counters[num -1] += 1
            if counters[num -1] > current_max:
                current_max = counters[num -1]
        else :
            max_result = current_max 
    return [max(i, max_result) for i in counters]
