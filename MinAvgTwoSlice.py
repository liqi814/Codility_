# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# Detected time complexity: O(N)

def solution(A):
    # write your code in Python 3.6
    len_A = len(A)
    pre_sum = [0] * (len_A + 1)
    new_avg = min_avg = float('Inf')
    min_avg_slice = -1
    for i in range(1, len_A + 1):
        pre_sum[i] = pre_sum[i-1] + A[i -1]
    for j in range(len_A-1):
        new_avg = (pre_sum[j+2] - pre_sum[j]) / 2.0
        if  new_avg < min_avg:
            min_avg = new_avg
            min_avg_slice = j
    for k in range(len_A-2):
        new_avg = (pre_sum[k+3] - pre_sum[k]) / 3.0
        if  new_avg < min_avg:
            min_avg = new_avg
            min_avg_slice = k
    return min_avg_slice
