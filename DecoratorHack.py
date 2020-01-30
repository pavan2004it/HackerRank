from functools import wraps


# def decorator_function(origial_function):
#     def wrapper_function(*args, **kwargs):
#         print("Wrapper executed before function {} ".format(origial_function.__name__))
#         return origial_function(*args, **kwargs)
#     return wrapper_function

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in: {} sec".format(orig_func.__name__, t2))
        return result
    return wrapper


# @my_logger
# def display():
#     print("The Display Function Ran")


# display()


@my_logger
@my_timer
def display_info(age, name):
    print("Display info ran with args {}, {}".format(age, name))


display_info("Tom", 27)


# class DecoratorClass:
#
#     def __init__(self, original_function):
#         self.original_function = original_function
#
#     def __call__(self, *args, **kwargs):
#         print("Call method executed this before {}".format(self.original_function.__name__))
#         return self.original_function(*args, **kwargs)
#
#
# @DecoratorClass
# def new_display():
#     print("Display with Class Decorator")
# new_display()


