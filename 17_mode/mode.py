def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    res = 0
    count = {}
    c = 0
    for n in nums:
        count[n] = count.get(n, 0) + 1
        if count[n] > c:
            c = count[n]
            res = n
    return res
