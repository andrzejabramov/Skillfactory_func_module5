import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        work = time.time() - start
        print(f'Функция {func.__name__} отработала за {work} секунд')
        return res
    return wrapper


@timeit
def large_sum(n):
    return sum(range(n))


@timeit
def prime_numbers(n):
    primes = []
    for prime in range(2, n):
        isPrime = True
        for num in range(2, int(prime ** 0.5) + 1):
            if prime % num == 0:
                isPrime = False
        if isPrime:
            primes.append(prime)
    return primes


prime_numbers(98765)
large_sum(98765)