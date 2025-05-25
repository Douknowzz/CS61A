def count_partitions(n, m):
    """Count partitions.

    >>> count_partitions(6, 4)
    9
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n - m, m)
        without_m = count_partitions(n, m - 1)
        return with_m + without_m

def count_partitions2(n, m):
    """Count partitions.

    >>> count_partitions(6, 4)
    9
    """
    if n < 0 or m == 0:
        return 0
    else:
        exact_match = 0
        if n == m:
            exact_match = 1
        with_m = count_partitions(n - m, m)
        without_m = count_partitions(n, m - 1)
        return exact_match + with_m + without_m

def list_partitions(n, m):
    """List partitions.

    >>> for p in list_partitions(6, 4): print(p)
    9
    """
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [[m]]
        with_m = [p + [m] for p in list_partitions(n - m, m)]
        without_m = list_partitions(n, m - 1)
        return exact_match + with_m + without_m


def partitions(n, m):
    """List partitions.

    >>> for p in partitions(6, 4): print(p)
    9
    """
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [str(m)]
        with_m = [p + ' + ' + str(m) for p in partitions(n - m, m)]
        without_m = partitions(n, m - 1)
        return exact_match + with_m + without_m

def partitions2(n, m):
    """Yield partitions.
    """
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in partitions(n - m, n):
            yield p + ' + ' + str(m)
        yield from partitions(n, m - 1)
