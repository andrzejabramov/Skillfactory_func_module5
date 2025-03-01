import random


def ensure_result_is_number(func):
    def wrapper(*args, **kwargs):
        digit = func()
        if isinstance(digit, (int, float)):
            return digit
        else:
            return None
    return wrapper


@ensure_result_is_number
def test_function():
    return random.choice(['Passed', 10, 'Failed', 5.5])


print(test_function())