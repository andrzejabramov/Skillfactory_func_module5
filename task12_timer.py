import time

# def timer():
#     sec = 0
#     while True:
#         time.sleep(1)
#         sec += 1
#         print(sec)
#
# timer()


def timer():
    start = time.time()
    def stopwatch():
        nonlocal start
        end = time.time()
        elapsed = end - start
        start = end
        return elapsed
    return stopwatch


my_timer = timer()
print(int(my_timer())) # int — для приближенного значения секунд
# Ждем немного...
time.sleep(2)
print(int(my_timer()))

# Вывод:
# 0
# 2

# def outer_func(outer_arg):
#     local_var = "Внешняя локальная переменная"
#     def closure():
#         print(outer_arg)
#         print(local_var)
#         print(another_local_var)
#     another_local_var = "Другая внешняя локальная переменная"
#     return closure
#
# closure = outer_func("Внешний аргумент")
#
# closure()

# Внешний аргумент
# Внешняя локальная переменная
# Другая внешняя локальная переменная