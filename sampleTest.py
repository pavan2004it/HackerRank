"""
A sample code to demonstrate first class functions
which can passed around like variables

"""



# def logger(msg):
#
#     def log_message():
#         print('Log:', msg)
#
#     return log_message
#
#
# log_hi = logger("Hello")
# log_hi()
#
#
# def html_tag(tag):
#
#     def wrap_text(msg):
#         print('<{0}>{1}</{0}>'.format(tag, msg))
#
#     return wrap_text
#
#
# wrap_1 = html_tag("h2")
# wrap_1("Hello World")


def square(x):
    return x * x


f_unc = square
print(f_unc.__name__)
print(f_unc(5))


def my_map(func, args):
    result = []
    for i in args:
        result.append(func(i))
    return result


y = [1, 2, 3, 4, 5]
sq = my_map(square, y)
print(sq)
