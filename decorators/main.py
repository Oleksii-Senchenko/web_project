def check_division_error(func):
    def wrapper(a, b):
        try:
            return func(a, b)
        except ZeroDivisionError as e:
            return f"{e}"

    return wrapper


def check_index_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError as e:

            return f"{e}"

    return wrapper


@check_division_error
def divide(a, b):
    return a / b


print(divide(12, 0))
print(divide(12, 2))


@check_index_error
def get_element(list_, index):
    return list_[index]


my_list = [1, 2, 3, 4, 5, 6, 7]
print(get_element(my_list, 52))
print(get_element(my_list, 2))
