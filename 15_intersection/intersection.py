def intersection(l1, l2):
    res = []
    for item in l1:
        if item in l2:
            res.append(item)
    return res