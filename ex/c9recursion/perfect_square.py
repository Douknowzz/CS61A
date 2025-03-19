from math import sqrt

def perfect_square(n):
    i = 0
    while i <= sqrt(n):
        if i * i == n:
            return True
        i = i + 1
    return False

def ps(n, i = 0):
    if i > sqrt(n):
        return False
    else:
        return i * i == n or ps(n, i + 1)

