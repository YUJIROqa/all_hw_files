w = '='*50

e = 0
while e < 5:
    print('Hello')
    e += 1
print('Done')

print(w)

# while True:
#     user_input = input('Enter somth: ')
#     if user_input == 'exit':
#         break
#     elif user_input == 'skip':
#         print('Skipping...')
#         continue
#     elif len(user_input) >10:
#         print('Too long')
#     else:
#         print('OK')

# print('Done')

print(w)

text = 'Sed vitae justo malesuada, commodo liberia end eu bidendum mauris'
words = text.split()
with_a = []
without_a = []

for word in words:
    if word == 'end':
            break
    if 'a' in word:
        with_a.append(word)
        continue
    without_a.append(word)

print(', '.join(with_a))
print(', '.join(without_a))

print(w)

a = 1
b = 5
c = 4
d = 7
e = 5
y = 0

main_num = 47

def calc(numb): # numb - параметр функции . в скобках указываем параметры которые принимает эта функция
    if y == 0:
         print(numb)
    else:
         print(numb + main_num)
    
calc(a) # когда вызываем функцию, то в скобкахпередаем аргументы которые принимает функция
calc(b)
calc(c)
calc(d)
calc(e)

print(w)

a = 1
b = 5
c = 4
d = 7
e = 5
y = 4

main_num = 47

def calc(numb): # numb - параметр функции 
    if y == 0:
         return numb
    else:
         return numb + main_num
    
print(calc(a))
print(calc(b))
print(calc(c))
print(calc(d))
print(calc(e))

print(w)

def calc(numb): # numb - параметр функции 
     print('Hello') # тело функции

calc(23) 

print(w)

def hello(): # глобальная переменная.  в скобках указываем параметры которые принимает эта функция
     a = 12 # локальная переменная 
     return a 
print(hello())

print(w)

def print_words(first, second, third, fourth, fifth):  
     print(f'The first word is {first}, the second word is {second}, the third word is {third}, the fourth word is {fourth}, the fifth word is {fifth}')

print_words('one', 'two', 'three', 'four', 'five') # позиционные аргументы
print_words(fifth = 'five', fourth = 'four', third = 'three', second = 'two', first = 'one') # именованные аргументы

print(w)

def power(number, degree = 2): # degree = 2 - значение по умолчанию
     return number ** degree # возведение в степень 

print(power(3)) # 3 ** 2 = 9
print(power(2, 3)) # 2 ** 3 = 8

print(w)

def example(e, f, g, ff = 'one', gg = 'two'): # ff и gg - именованные аргументы
     print(e, f, g, ff, gg) # ff и gg - именованные аргументы

example(2, 3, 6) # 2 3 6 one two
example(2, 3, 6, 22, gg = 444) # позиционные и именованные аргументы. аргументы передаются по порядку, а именованные аргументы передаются по имени

print(w)

def sum_all(*args): # *args - аргументы, которые передаются в функцию
    # #  print(args)
    # result = 0 # переменная для хранения суммы
    # for x in args: # цикл для перебора аргументов
    #      result += x # суммирование аргументов
    # return result # возвращение результата
    return sum(args) # суммирование аргументов

print(sum_all(1, 4, 6, 11, 25, 65)) 

print(w)

def price_list(title, price):
     print(f'Product: {title}, price: {price}')

price_list('iphone', 100)
price_list('samsung', 200)
price_list('nokia', 300)

print(w)

def price_list(**kwargs): # **kwargs - аргументы, которые передаются в функцию
    print(kwargs) # выводим словарь
    for product in kwargs.items(): # перебираем словарь
         title, price = product # title - название продукта, price - цена продукта
         print(f'Product: {title}, price: {price}') # выводим название и цену продукта

price_list(iphone = 1000, samsung = 2500, nokia = 700) # выводим словарь



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for num in numbers:
     if num % 3 == 0 and num % 5 == 0:
          print('FizzBuzz')
     elif num % 3 == 0:
          print('Fizz')
     elif num % 5 == 0:
          print('Buzz')
     else:
          print(num)

print(w)

# num1 = int(input('Введите число 1: '))
# znak = input('Введите знак: ')
# num2 = int(input('Введите число 2: '))

# if znak == '+':
#      print(num1 + num2)
# elif znak == '-':
#      print(num1 - num2)
# elif znak == '*':
#      print(num1 * num2)
# elif znak == '/':
#      print(num1 / num2)
# else:
#      print('Неверный знак')

print(w)

a = 10
while a > 0:
     print(a)
     a -= 1



# Новый код:
total = 0  # Создаем переменную для хранения суммы
while True:  # Бесконечный цикл, который работает пока не встретит break
     user_input = input('Введите число: ')  # Получаем ввод от пользователя
     if user_input == 'stop':  # Если пользователь ввел 'stop'
          print(f'Итоговая сумма: {total}')  # Выводим финальную сумму
          break  # Прерываем цикл
     if user_input.startswith('-'):  # Если число начинается с минуса
          continue  # Пропускаем это число и продолжаем цикл
     total += int(user_input)  # Преобразуем строку в число и добавляем к сумме
     print(f'Текущая сумма: {total}')  # Выводим текущую сумму

print(w)

total = 0
count = 0
while True:
     user_input = input('Введите число: ')  # Получаем строку
     if user_input == 'end':
          break
     if user_input == 'skip':
          continue
     total += float(user_input)  # Преобразуем в дробное число
     count += 1
     print('total:', total)
print(f'Среднее арифметическое: {total / count}stop')

print(w)

# def is_even(number):
#      if number % 2 == 0:
#           return True
#      elif number % 2 != 0:
#           return False

def is_even(number): # короткая запись 
     return number % 2 == 0 # возвращаем True если число четное, иначе False

# print(is_even(1))
# print(is_even(2))
# print(is_even(3))
# print(is_even(4))
# print(is_even(5))

for i in range(1, 6): # цикл для перебора чисел от 1 до 5
     result = is_even(i) # вызываем функцию is_even и передаем число i
     print(f'Число {i} четное? {result}') # выводим результат

print(w)


def greet(name, greeting = 'Привет'):
     return f'{greeting}, {name}'

print(greet('Иван '))
print(greet('Иван ', 'Здравствуйте'))
print(greet('Егор ', greeting = 'Салам аллейкум'))

print(w)

def find_max(*args):
     return max(args)

print(find_max(1, 2, 3, 4, 5))

print(w)

full = []
i = 0
while i < 1000:
     full.append(i)
     i += 1
print(full)
print(sum(full) / len(full))

def calculate_average(*args):
     return sum(args) / len(args)

print(calculate_average(1, 2, 3, 4, 5))

print(w)



def calculate_average(*args): # *args - аргументы, которые передаются в функцию именованные аргументы
     if len(args) > 0: # если длина аргументов больше 0
     #if args: # если аргументы не пустые. переводится как если аргументы тру
          return sum(args) / len(args) # возвращаем среднее арифметическое
     else:
          return 0 # возвращаем 0

print(calculate_average(10, 20, 30))  # Должно вернуть 20.0
print(calculate_average(5, 10, 15, 20))  # Должно вернуть 12.5
print(calculate_average())  # Должно вернуть 0



print(w)

def create_person(**info):
     print(info)
     for inf in info:
          name, age, city, job = inf
          print(f'Name: {name}, Age: {age}, City: {city}, Job: {job}')

print(create_person(name="Иван", age=30, city="Москва"))
# Должно вернуть: "Имя: Иван, Возраст: 30, Город: Москва"

print(create_person(name="Анна", job="Программист"))
# Должно вернуть: "Имя: Анна, Работа: Программист"
