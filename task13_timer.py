def timer():
    pass



my_timer = timer()
print(int(my_timer())) # int — для приближенного значения секунд
# Ждем немного...
time.sleep(2)
print(int(my_timer()))

# Вывод:
# 0
# 2