def f(x):
    if x > 0:
        return x + f(x-1)
    else:  # f(0) = 0
        return 0

