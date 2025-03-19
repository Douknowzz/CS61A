def countOnes(n):
    #我的思路
    """
    if n < 10:
        if n == 1:
            return 1
        else:
            return 0
    else:
        all_but_last, last = n // 10, n % 10
        currOne = 1 if last == 1 else 0
        return countOnes(n // 10) + currOne
    """
    #cs61a思路
    if n == 0:
        return 0
    else:
        if n % 10 == 1:
            return countOnes(n // 10) + 1
        else:
            return countOnes(n // 10)
