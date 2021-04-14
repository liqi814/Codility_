# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# Detected time complexity:O(N)

def solution(A):
    # write your code in Python 3.6
    len_A = len(A)
    if len_A == 1 :
        return 0
    elif len_A > 2000000000:
        return -1
    cars_counter = [0] * (len_A+1)
    for i in reversed(range(len_A)):
        cars_counter[i] = cars_counter[i+1] + A[i]
        if cars_counter[i] > 1000000000:
            return -1
    passing_paris = 0
    for j in range(len_A-1):
        if A[j] == 0:
            passing_paris += cars_counter[j]
            if passing_paris > 1000000000:
                return -1
    return passing_paris
