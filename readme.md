# Task1_fibonacci

В этом задании вам предстоит поработать со второй классической задачей в контексте рекурсивных функций — числами Фибоначчи.

Числа Фибоначчи — это последовательность чисел, в которой каждое следующее число в ряду является суммой двух предыдущих чисел. Первые два числа в этой последовательности — это 0 и 1.

Например, вот начало последовательности Фибоначчи: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 и так далее. Каждое число в этой последовательности, начиная с третьего, — это сумма двух предыдущих чисел.

1.Алгоритм вычисления n-ного числа Фибоначчи:
Определите два базовых случая: -вложенный Если n меньше или равно 0, верните 0. -вложенный Если n равно 1, верните 1.

2.Иначе, вызовите функцию рекурсивно для (n-1)-го и (n-2)-го числа Фибоначчи и верните их сумму.

Ваша задача — определить функцию fibonacci для вычисления n-ного числа Фибоначчи.

Пример работы программы:


print(fibonacci(5)) 
#### #5
print(fibonacci(7)) 
#### #13
print(fibonacci(8)) 
#### #21

-----------------------------
# Task2_pallindrome

С помощью рекурсии определите, является ли слово палиндромом.
Для этого реализуйте функцию is_palindrome, которая принимает строку s. Если слово — палиндром, функция должна возвращать True, если не палиндром — False.
Пример работы программы:


print(is_palindrome('racecar'))
#### True
print(is_palindrome('gong'))
#### False

-------------------------------
# Task3_binnary

Ваша задача — реализовать алгоритм бинарного поиска. Он значительно экономит время, ускоряя поиск элемента в отсортированном списке или массиве.

Бинарный поиск позволяет сразу исключить половину элементов, в то время как простой линейный поиск проверяет каждый элемент по очереди. Это особенно полезно при работе с большими данными.

Нужно, используя рекурсию, перевести на язык Python следующий алгоритм:

1.Определите средний элемент отсортированного списка.
2.Если средний элемент является искомым значением, то поиск завершён.
3.Если искомое значение меньше среднего элемента, повторите поиск в левой половине списка.
4.Если искомое значение больше среднего элемента, повторите поиск в правой половине списка.
5.Если список пуст (то есть начальная позиция больше конечной), значит, искомого элемента в списке нет.

Определите функцию binary_search, которая принимает первым аргументом список (он уже отсортирован), а вторым — элемент, который необходимо найти.

Функция должна возвращать True, если такой элемент есть в списке, и False — если его нет.

Пример работы программы:


print(binary_search([1, 2, 3, 4, 5], 4))
#### #True
print(binary_search([1, 2, 3, 4, 5], 6))
#### #False

--------------------------
# Task4

Условие: Во многих веб-приложениях URL-ы могут быть структурированы последовательно (например, /product/1, /product/2 и так далее). Создайте функцию-генератор generate_urls, которая будет возвращать последовательные URL-ы для заданного шаблона и диапазона чисел.

Пример работы программы:


url_generator = generate_urls("/product/", 1, 3)
for url in url_generator:
   print(url)
#### #/product/1
#### #/product/2
#### #/product/3

-----------------------------------
# Task5

Условие: Для генерирования тестовых наборов данных вам необходимо создать функцию-генератор generate_user_data, которая принимает: размер генерируемой последовательности, список возможных имен, список возможных фамилий, диапазон возраста (список из двух чисел, включительно).

Генерируемые значения — кортеж из имени, фамилии и возраста. Данные значения должны генерироваться случайным образом (воспользуйтесь библиотекой random).

Пример работы программы:


first_names = ["Alice", "Bob", "Charlie"]
last_names = ["Smith", "Johnson", "Williams"]
user_data_generator = generate_user_data(5, first_names, last_names, [18, 60])
for user in user_data_generator:
   print(user)
#### #('Charlie', 'Williams', 19)
#### #('Charlie', 'Johnson', 48)
#### #('Bob', 'Johnson', 26)
#### #('Charlie', 'Smith', 36)
#### #('Charlie', 'Johnson', 35)

--------------------------------------
# Task6

Условие: В прошлом юните вы уже столкнулись с числами Фибоначчи. Теперь вам необходимо не просто возвращать значение, а генерировать последовательность чисел Фибоначчи до заданного n.
Для этого реализуйте функцию fibonacci, которая принимает n — количество чисел в генерируемой последовательности.

Подсказка: раз оператор yield лишь «замораживает» — приостанавливает работу функции, то очевидно, его не обязательно помещать в самый «конец» (конец в кавычках потому что наша функция не заканчивает работу, а останавливается) функции, то есть:


def func(...):
####   # Какой-то набор операций здесь
   for _ in range(...):
       # Генерируем значение последовательности и останавливаем функцию
       yield ...
       # Код здесь выполнится при последующем вызове функции (генерации нового элемента)
####   # И код здесь выполнится при последующем вызове функции (генерации нового элемента)

Пример работы программы:


fibonacci_generator = fibonacci(7)
for number in fibonacci_generator:
   print(number)
#### #0
#### #1
#### #1
#### #2
#### #3
#### #5
#### #8

--------------------------
# Task7

Условие: И снова о генерации данных, в финальном задании этой темы вас ожидает еще одна классика любых собеседований и в целом крайне полезное задание — создание генератора простых чисел.

Ваша задача — создать функцию-генератор primes, которая принимает число. И она должна сгенерировать последовательность из всех натуральных чисел до этого числа включительно.
Если число делится без остатка только на 1 и на само себя, оно считается простым.

Пример работы программы:


prime_generator = primes(7)
for prime in prime_generator:
   print(prime)

#### #2
#### #3
#### #5
#### #7

-----------------------------
# Task8

Условие: Вам дан список цен на товары в долларах и отношение к курсу евро. С помощью функции map преобразуйте данные цены в валюту евро.
Выводить на экран ничего не надо, лишь создать список и сохранить его в предложенной переменной.

Стартовый код:


prices_in_usd = [10, 20, 30, 40, 50]
exchange_rate = 0.85

prices_in_euro = # Ваш код здесь

--------------------------------
# Task9

Условие: QA-инженерам часто приходится проверять, как система реагирует на разные типы данных. Допустим, у вас есть форма регистрации на сайте, где одним из полей является «Телефон». Вы хотите проверить, обрабатывается ли введенный телефон корректно.
Пусть у вас есть список номеров телефонов в разных форматах:

['123-456-7890', '123.456.7890', '(123) 456-7890', '+1234567890', '1234567890'].

Напишите функцию format_phone_number, которая с помощью filter приводит номер к единому формату: 1234567890.
А затем в formatted_numbers с помощью map сохраните результат применения функции format_phone_number к списку phone_numbers.

Стартовый код:


phone_numbers = ['123-456-7890', '123.456.7890', '(123) 456-7890', '+1234567890', '1234567890']

def format_phone_number(number):
#### #Ваш код здесь (Воспользуйтесь filter)

formatted_numbers = # Ваш код здесь (Воспользуйтесь map)

--------------------------------------
# Task10

Представьте: вы работаете в компании, которая разрабатывает мобильные приложения. Вы приступаете к тестированию функционала, который отслеживает, сколько раз пользователи выполняют определенные действия в приложении. Вам нужно создать замыкание-счетчик, которое поможет вам в этой задаче.

Для этого создайте функцию create_counter, которая возвращает замыкание-счетчик. Счетчик должен увеличиваться на 1 каждый раз, когда вызывается замыкание.

Пример работы программы:


counter = create_counter()
print(counter())  # вернет "1"
print(counter())  # вернет "2"
print(counter())  # вернет "3"

#### #1
#### #2
#### #3

-------------------------------------------
# Task11

Вы сотрудник финансовой компании, работающей над созданием системы, отслеживающей транзакции пользователей. Вы заметили, что система должна уметь проверять уникальность идентификаторов транзакций.

Задача – Вам нужно создать замыкание, которое будет проверять, встречалось ли значение ранее или нет.

Вам необходимо проверять уникальность элементов. Создайте замыкание — функцию create_unique_checker, — которое принимает значение и возвращает True, если это значение ранее не встречалось, и False в противном случае. Подсказка: вспомните о структуре (типе данных) set.

Пример работы программы:


unique_checker = create_unique_checker()
print(unique_checker(5))  
print(unique_checker(5))  
print(unique_checker(10))  

#### #True
#### #False
#### #True

------------------------------------------
# Task12

Вы работаете в стартапе, который разрабатывает решения в области IoT. Одна из ваших задач — определить эффективность выполнения различных функций и модулей. Вам поступила задача создать функцию timer, которую будут использовать в качестве таймера для измерения времени выполнения различных операций.

Задача – Для этого вам необходимо создать замыкание, которое будет выступать в роли таймера. Это замыкание должно возвращать время, прошедшее с момента его последнего вызова.

Пример работы программы:


my_timer = timer()
print(int(my_timer())) # int — для приближенного значения секунд
#### #Ждем немного...
time.sleep(2)
print(int(my_timer()))

#### #Вывод:
#### #0
#### #2

----------------------------------------
# Task13


