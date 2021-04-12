# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    if X > len(A) and max(A) < X:
        return(-1)
    positions = [False] * (X + 1)
    positions[0] = True
    for i in range(len(A)):
        if not positions[A[i]]:
            positions[A[i]] = i + 1
    if not all(positions):
        return(-1)
    else:
        return(max(positions) -1)
    pass
