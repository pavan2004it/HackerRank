def avg(*args):
    average = 0
    for num in args:
        average += num

    return average / len(args)


print(avg(7))
