def print_formatted(number):
    w = len("{0:b}".format(number))
    for i in range(int(number) + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w))
        # print("{0:{width}d}".format(i, width=w) + " " + "{0:{width}o}".format(i, width=w)
        #       + "{0:{width}X}".format(i, width=w) + "{0:{width}b}".format(i, width=w))


print_formatted(17)
