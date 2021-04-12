# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    if len(A) <= 1 :
        return(A)
    remains = K % len(A)
    new_A = A[-remains :] + A
    return(new_A[:len(A)])
    pass
