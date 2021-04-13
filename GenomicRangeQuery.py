# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# Detected time complexity: O(N + M)

def CharWriteToList(last_time_seen, Obser_Char, Expect_Char, idx):
    if Obser_Char == Expect_Char:
        last_time_seen[idx] = idx
    elif idx > 0:
        last_time_seen[idx] = last_time_seen[idx-1]

def solution(S, P, Q):
    # write your code in Python 3.6
    len_S = len(S)
    len_q = len(Q)
    last_time_seen_A = [-1] * len_S
    last_time_seen_C = [-1] * len_S
    last_time_seen_G = [-1] * len_S
    last_time_seen_T = [-1] * len_S
    
    for index in range(len_S):
        CharWriteToList(last_time_seen_A, S[index], 'A', index)
        CharWriteToList(last_time_seen_C, S[index], 'C', index)
        CharWriteToList(last_time_seen_G, S[index], 'G', index)
        CharWriteToList(last_time_seen_T, S[index], 'T', index)

    min_impact_factor = [0] * len_q

    for k in range(len_q):
        if last_time_seen_A[Q[k]] >= P[k]:
            min_impact_factor[k] = 1
        elif last_time_seen_C[Q[k]] >= P[k]:
            min_impact_factor[k] = 2
        elif last_time_seen_G[Q[k]] >= P[k]:
            min_impact_factor[k] = 3
        elif last_time_seen_T[Q[k]] >= P[k]:
            min_impact_factor[k] = 4
    return(min_impact_factor)
