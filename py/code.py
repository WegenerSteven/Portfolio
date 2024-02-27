def my_func(x, y):
    if x==y:
        return x + y
    else:
        return my_func(x,y-1)
    print(my_func(3,6)) 