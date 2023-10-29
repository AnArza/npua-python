def sum_of_elements(numbers, exclude_negative=False):
    res = 0
    for num in numbers:
        if num > 0:
            res += num
        else:
            if not exclude_negative:
                res += num
    return res
