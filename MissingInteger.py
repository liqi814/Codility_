# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    length_counter = max(A)
    if length_counter < 0 :
        return 1
    else:
        counters=[0] * (length_counter + 1)
    for i in A:
        if i <= 0 :
            continue
        else:
            counters[i-1] += 1
    for j in range(length_counter + 1) :
        if counters[j] == 0 :
            return(j+1)
