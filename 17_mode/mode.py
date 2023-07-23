def mode(nums):
    res = 0
    count = {}
    c = 0
    for n in nums:
        count[n] = count.get(n, 0) + 1
        if count[n] > c:
            c = count[n]
            res = n
    return res