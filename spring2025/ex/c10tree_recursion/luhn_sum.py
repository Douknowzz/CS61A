def split(n):
    # split a positive number integer into all but its last digits and its last digits
    return n // 10, n % 10

def sum_digits(n):
    # Return the sum of the digits of positive integer n
    if n < 10:
        return n
    else:
        a, b = split(n)
        return sum_digits(a) + b

def luhn_sum(n):
    if n < 10:
        return n
    else:
        a, b = split(n)
        return luhn_sum2(a) + b

def luhn_sum2(n):
    a, b = split(n)
    d = sum_digits(2 * b)
    if n < 10:
        return d
    else:
        return luhn_sum(a) + d
