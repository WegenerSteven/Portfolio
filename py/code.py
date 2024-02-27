def my_func(x, y):
    if x == y:
        return x + y
    elif y <= 0:
        raise ValueError("y must be positive")
    else:
        return my_func(x, y - 1)

try:
    print(my_func(3, 6))
except RecursionError:
    print("Recursion limit exceeded")