import datetime

w = '='*50

summer = True
if summer is True:
    print("It is summer")
else:
    print("It is not summer")

print(w)

if summer: # summer всегда True
    print("It is summer")
else:
    print("It is not summer")

print(w)

a = ''
if a: #в питоне как True считается любой непустой(не 0) строка, любое число, любой список, любой словарь, любой кортеж
    print('....')
else:
    print(123)

print(w)

numbers = [1, 4, 8, 9, 2, 5, 14, 16, 11, 14, 26, 29]
print(max(numbers)) # находит максимальное число в списке
print(min(numbers)) # находит минимальное число в списке
print(sum(numbers)) # находит сумму всех чисел в списке
print(sorted(numbers)) # сортирует и выволит список по возрастанию
print(sorted(numbers, reverse=True)) # сортирует и выводит список по убыванию
numbers.sort() # перезаписывает список по возрастанию
print(numbers)


max_num = 0 # максимальное число 
for x in numbers: # x - это каждый элемент списка
    if x > max_num: # если x больше max_num, то max_num = x это значит что мы ищем максимальное число из списка
        max_num = x # max_num = x это значит что мы сравниваем следующий элемент списка с max_num(предыдущим максимальным числом)
print(max_num)

print(w)

a = 1/3
print(round(a, 2)) # округляет число до 2 знаков после запятой

print(abs(-1)) # возвращает абсолютное значение числа(это значит что если число отрицательное, то оно станет положительным)

print(w)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = []
for x in my_list:
    new_list.append(x*2)

print(new_list)

print(w)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def multiply_by_two(x): # функция которая умножает число на 2
    return x*2 # возвращает число умноженное на 2

new_list = map(multiply_by_two, my_list) # map - это функция которая принимает функцию и список, и применяет функцию к каждому элементу списка
print(list(new_list)) # преобразует map в список

print(w)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = map(lambda x: x*2, my_list) #(х умножаем на 2 для каждого элемента списка му_лист) lambda - это функция которая принимает аргумент и возвращает результат. Проще говоря, это функция без имени
print(list(new_list)) # преобразует map в список

print(w)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def multiply_by_two(x): # функция которая умножает число на 2
    if x > 10:
        return x * 5
    else:
        return x * 2
    
new_list = map(lambda x: x * 5 if x > 10 else x * 2, my_list) #(х умножаем на 5 если х больше 10, иначе х умножаем на 2)
print(list(new_list)) # преобразует map в список

print(w)

hw_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # список
new_hw_list = map(lambda x: x*3 if x<5 else (x*2 if 5<x<10 else (x%2 if x>10 else x)), hw_list) # елси более 2х условий, то используем скобки. 
print(list(new_hw_list))                          #если у нас есть условия по типу 5<x<10, то нужен дополнительный елс х в конце для обработки этих значений(или питон вернут нан)

print(w)

my_list = [1, 2, 3, 4, 5]
b = 1 if len(my_list) > 4 else 0 # если длина списка больше 4, то b = 1, иначе b = 0
print(b)
#lambda это тернарный оператор

print(w)

# my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list2 = []
# for x in my_list2:
#     if x % 2 == 0:
#         new_list2.append(x)
# print(new_list2)

my_list2 = [1, 2, 3, 4, 5, 6, 7, 8]

# def is_even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False

# def is_even(x):
#     if x % 2 == 0: # если x делится на 2 без остатка, то x четное
#         return True # возвращает True
#     return False # возвращает False(то есть если x не делится на 2 без остатка, то x сразу возвращает фолс тк не выполняется 1е условие а ретурн это конец функции)

def is_even(x):
    return x % 2 == 0 #сравнение возвращает True или False. В нашем случае если x делится на 2 без остатка, то x четное и возвращается True, иначе False


new_list2 = filter(is_even, my_list2) # filter - это функция которая принимает функцию и список, и применяет функцию к каждому элементу списка. 
                                      # для каждого элемента из my_list2 применится функция is_even. И если элемент который попал в нее True, то он пойдет в список
                                      # если False, то не пойдет

print(list(new_list2))

print(w)

tame_now = datetime.datetime.now()
print(tame_now)
print(tame_now.year)
print(tame_now.month)

print(w)

my_time = '2023/06/05 12 hours 30 minutes, 15 seconds' # строка
python_datetime = datetime.datetime.strptime(my_time, '%Y/%m/%d %H hours %M minutes, %S seconds') # переводит строку в datetime
print(python_datetime) 

human_date = python_datetime.strftime('%d %B %Y') # переводит datetime в строку
print(human_date)

print(w)







