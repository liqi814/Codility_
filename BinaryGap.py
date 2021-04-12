# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    str_bin_N = str(bin(N).strip('0b'))
    indices = [i for i, x in enumerate(str_bin_N) if x == '1']
    GAP = [0]*len(indices)
    for i in range(1, len(GAP)):
        GAP[i] = indices[i] - indices[i-1] - 1
    return max(GAP)
    pass
