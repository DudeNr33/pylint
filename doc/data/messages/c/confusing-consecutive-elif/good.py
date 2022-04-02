def my_func(a: int, b: int, c: int):
    result = 0
    if a > b:
        if a > c:
            result = a
        result = c
    elif b > c:
        result = b
    else:
        result = c
    return result
