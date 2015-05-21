# -*- coding: utf-8 -*-
def sum_args(*args):
    """
    >>> sum_args(1, 2, 3)
    6

    >>> sum_args(1)
    1
    """
    total = lambda x, y: x + y
    return reduce(total, args)


if __name__ == '__main__':
    # print sum_args(1, 2, 3)
    import doctest
    doctest.testmod()