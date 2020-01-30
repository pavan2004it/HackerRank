import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler("sample.log")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def sub(x, y):
    return x - y


def div(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception("Zero division Error")
    else:
        return result


num_1 = 10
num_2 = 0

add_result = add(num_1, num_2)
logger.debug('Add: {} {} + {}'.format(num_1, num_2, add_result))

sub_result = sub(num_1, num_2)
logger.debug('Subtract: {} {} + {}'.format(num_1, num_2, sub_result))

div_result = div(num_1, num_2)
logger.debug('Division: {} {} + {}'.format(num_1, num_2, div_result))
