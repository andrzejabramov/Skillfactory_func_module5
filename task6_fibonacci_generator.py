# def fibonacci(number):
#     # Какой-то набор операций здесь
#     for _ in range(...):
#         # Генерируем значение последовательности и останавливаем функцию
#         yield ...
#         # Код здесь выполнится при последующем вызове функции (генерации нового элемента)
#     # И код здесь выполнится при последующем вызове функции (генерации новог


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


fibonacci_generator = fibonacci(7)
for number in fibonacci_generator:
   print(number)


# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)