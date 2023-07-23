def partition(lst, fn):
    result = []
    rest = []
    for item in lst:
        if fn(item):
            result.append(item)
        else:
            rest.append(item)
    return [result, rest]
