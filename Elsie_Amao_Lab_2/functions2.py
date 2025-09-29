####### Code for Part II #######

def example1(S):
    """Return the sum of the elements in sequence S."""
    n = len(S)
    total = 0
    for j in range(n):                  # loop from 0 to n-1
        total += S[j]
    return total

def example2(S):
    """Return the sum of the elements with even index in sequence S."""
    n = len(S)
    total = 0
    for j in range(0, n, 2):            # note the increment of 2
        total += S[j]
    return total

def example3(S):
    """Return the sum of the prefix sums of sequence S."""
    n = len(S)
    total = 0
    for j in range(n):                  # loop from 0 to n-1
        for k in range(1+j):            # loop from 0 to j
            total += S[k]
    return total

def example4(S):
    """Return the sum of the prefix sums of sequence S."""
    n = len(S)
    prefix = 0
    total = 0
    for j in range(n):
        prefix += S[j]
        total += prefix
    return total

def example5(A, B):                     # assume that A and B have equal length
    """Return the number of elements in B equal to the sum of prefix sums in A."""
    n = len(A)
    count = 0
    for i in range(n):                  # loop from 0 to n-1
        total = 0
        for j in range(n):              # loop from 0 to n-1
            for k in range(1+j):        # loop from 0 to j
                total += A[k]
        if B[i] == total:
            count += 1
    return count

####### Code for Part III #######

def prefix_average1(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0] * n                         # create new list of n zeroes
    for j in range(n):
        total = 0                       # begin computing S[0] + ... + S[j]
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j+1)            # record the average
    return A

def prefix_average2(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0] * n                         # create new list of n zeroes
    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j+1)    # record the average
    return A

def prefix_average3(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0] * n                         # create new list of n zeroes
    total = 0                           # compute prefix sum as S[0] + S[1] + ...
    for j in range(n):
        total += S[j]                   # update prefix sum to include S[j]
        A[j] = total / (j+1)            # compute average based on current sum
    return A

a = prefix_average1([0,4,5,3,5,6])
b = prefix_average2([9,5,3,6,3])
c = prefix_average3([8,5,8,3,7,5,7])
print(a)
print(b)
print(c)