class Worker:
    greeting = 'Sir'
    def __init__(self):
        self.elf = Worker
    def work(self):
        return self.greeting + ', I work'
    def __repr__(self):
        return Bourgeoisie.greeting

class Bourgeoisie(Worker):
    greeting = 'Peon'
    def work(self):
        print(Worker.work(self))
        return 'I gather wealth'

#jack = Worker()
#john = Bourgeoisie()
#jack.greeting = 'Maam'

#################################################
### Using Built-In Functions & Comprehensions ###
#################################################


def min_abs_indices(s):
    """Indices of all elements in list s that have the smallest absolute value.

    >>> min_abs_indices([-4, -3, -2, 3, 2, 4])
    [2, 4]
    >>> min_abs_indices([1, 2, 3, 4, 5])
    [0]
    """
    min_abs = min(map(abs, s))
    return [i for i in range(len(s)) if abs(s[i]) == min_abs]
    #f = lambda i: abs(s[i]) == min_abs
    #return list(filter(f, range(len(s))))


    """
    abs_min = abs(s[0])
    result = []
    for i in range(1, len(s)):
        if abs(s[i]) < abs_min:
            abs_min = abs(s[i])
            result = [i]
        elif abs(s[i]) == abs_min:
            result.append(i)
    return result
    """

def largest_adj_sum(s):
    """Largest sum of two adjacent elements in a list s.

    >>> largest_adj_sum([-4, -3, -2, 3, 2, 4])
    6
    >>> largest_adj_sum([-4, 3, -2, -3, 2, -4])
    1
    """
    return max([s[i] + s[i+1] for i in range(len(s) - 1)])
    #return max([a + b for a, b in zip(s[:-1], s[1:])])

    """
    max_i = 0
    for i in range(len(s)-1):
        curr = s[i]
        next_i = s[i+1]
        if max_i < curr + next_i:
            max_i = curr + next_i
    return max_i
    """

def digit_dict(s):
    """Map each digit d to the lists of elements in s that end with d.

    >>> digit_dict([5, 8, 13, 21, 34, 55, 89])
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    return {d: [x for x in s if x % 10 == d] for d in range(10) if any([x % 10 == d for x in s])}
    #last_digits = [x % 10 for x in s]
    #return {d: [x for x in s if x % 10 == d] for d in range(10) if d in last_digits])}


    """
    dict_s = {}
    for i in s:
        k = i % 10
        if k in dict_s:
            dict_s[k].append(i)
        else:
            dict_s[k] = [i]
    d_sorted = dict(sorted(dict_s.items()))
    return d_sorted
    """

def all_have_an_equal(s):
    """Does every element equal some other element in s?

    >>> all_have_an_equal([-4, -3, -2, 3, 2, 4])
    False
    >>> all_have_an_equal([4, 3, 2, 3, 2, 4])
    True
    """
    return min([s.count(x) for x in s]) > 1
    #return all([s[i] in s[:i] + s[i+1:] for i in range(len(s))])

    """
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] == s[j] and i != j:
                return True
    return False
    """



#############################
### Example: Linked Lists ###
#############################

def ordered(s, key=lambda x: x):
    """Is Link s is ordered?

    >>> ordered(Link(1, Link(3, Link(4))))
    True
    >>> ordered(Link(1, Link(4, Link(3))))
    False
    >>> ordered(Link(1, Link(-3, Link(4))))
    False
    >>> ordered(Link(1, Link(-3, Link(4))), key=abs)
    True
    >>> ordered(Link(1, Link(4, Link(3))), key=abs)
    False
    """
    if s is Link.empty or s.rest is Link.empty:
        return True
    elif key(s.first) > key(s.rest.first):
        return False
    else:
        return ordered(s.rest)

def merge(s, t):
    """Return a sorted Link with the elements of sorted s & t.

    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(4))
    >>> merge(a, b)
    Link(1, Link(1, Link(4, Link(5))))
    >>> a
    Link(1, Link(5))
    >>> b
    Link(1, Link(4))
    """
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        return Link(s.first, merge(s.rest, t))
    else:
        return Link(t.first, merge(s, t.rest))

def merge_in_place(s, t):
    """Return a sorted Link with the elements of sorted s & t.

    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(4))
    >>> merge_in_place(a, b)
    Link(1, Link(1, Link(4, Link(5))))
    >>> a
    Link(1, Link(1, Link(4, Link(5))))
    >>> b
    Link(1, Link(4, Link(5)))
    """
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        s.rest = merge_in_place(s.rest, t)
        return s
    else:
        t.rest = merge_in_place(s, t.rest)
        return t



class Link:
     empty = ()
     def __init__(self, first, rest=empty):
         assert rest is Link.empty or isinstance(rest, Link)
         self.first = first
         self.rest = rest

     def __repr__(self):
         if self.rest is not Link.empty:
             rest_repr = ', ' + repr(self.rest)
         else:
             rest_repr = ''
         return 'Link(' + repr(self.first) + rest_repr + ')'

     def __str__(self):
         string = '<'
         while self.rest is not Link.empty:
             string += str(self.first) + ' '
             self = self.rest
         return string + str(self.first) + '>'
