def multiply_even_numbers(nums):
    res = 1
    for n in nums:
        if n % 2 == 0:
            res *= n
    return res
