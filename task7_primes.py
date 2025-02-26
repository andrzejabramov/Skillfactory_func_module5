def primes(number):
    n = 2
    while n <= number:
#   for n in range(1, number):
        if all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)):
#           n += 1
#        else:
            yield n
        n += 1


prime_generator = primes(1)
for prime in prime_generator:
   print(prime)