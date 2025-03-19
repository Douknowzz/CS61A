def count_partitions(m, n):
    if m == 0:
        return 1
    elif m < 0:
        return 0
    elif n == 0:
        return 0
    else:
        with_n = count_partitions(m - n, n)
        without_n = count_partitions(m, n - 1)
        return with_n + without_n
