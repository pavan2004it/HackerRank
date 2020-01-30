import sys


def out_func():
    message = "hi"

    def inner_func():
        print(message)
    return inner_func


x = out_func()

x()

# foo = []
print(sys.getrefcount(out_func))