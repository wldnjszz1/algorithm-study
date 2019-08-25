def recursive(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return recursive(x - 1) + recursive(x - 2)


def iterative(x):
    a, b = 1, 0
    for i in range(x):
        a, b = b, a + b
    return b


#정확도 100, 효율성 100
