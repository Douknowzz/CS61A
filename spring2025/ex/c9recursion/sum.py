def sum_iter(n):
    s = 0
    i = 1

    while i <= n:
        s = s + i
        i = i + 1

    return s

def sum_rec(n):
    if n == 0:
        return 0
    else:
        return sum_rec(n - 1) + n
