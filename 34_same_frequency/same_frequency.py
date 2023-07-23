def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    count1 = {}
    count2 = {}
    for n in str(num1):
        count1[n] = count1.get(n, 0) + 1
    for n in str(num2):
        count2[n] = count2.get(n, 0) + 1
    print(count2, count1)
    if len(count1) == len(count2):
        for k in count1:
            if count1[k] != count2[k]:
                return False
    return True