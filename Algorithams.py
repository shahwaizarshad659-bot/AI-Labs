# Algorithm 1
def algorithm_1(A, t):
    for i in range(len(A)):
        if A[i] == t:
            return True
    return False


# Algorithm 2
def algorithm_2(A, B, t):
    for i in range(len(A)):
        if A[i] == t:
            return True

    for i in range(len(B)):
        if B[i] == t:
            return True

    return False


# Algorithm 3
def algorithm_3(A, B):
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                return True
    return False


# Algorithm 4
def algorithm_4(A):
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] == A[j]:
                return True
    return False