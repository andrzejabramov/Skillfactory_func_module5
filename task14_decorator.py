import random


def retry_if_result_is_none(times=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                res = func(*args, **kwargs)
                if res != None:
                    return res
                return None
        return wrapper
    return decorator


@retry_if_result_is_none(times=2)
def test_function():
    return random.choice([None, 'Passed'])


print(test_function())