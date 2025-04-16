w = '='*50
def calc():
    print(1 + 1)

calc()
print(calc)
new_calc = calc
print(new_calc)

new_calc()

print(w)

def greet(): 

    def hello(): # функция внутри функции. Нужна для того чтобы при вызове greet() вызывалась hello()
        return 'hello' # возвращает строку 'hello'
    return hello() # возвращает результат выполнения hello(). То есть greet() вернет hello()
print(greet()) # вызывает greet() и выводит результат выполнения hello()

print(w)

def calculate(price, quantity , quality): # аргументы функции
    return price * quantity * quality # возвращает результат выполнения функции

print(calculate(quantity = 10, price = 20, quality = 3)) # вызывает функцию calculate с аргументами quantity = 10, price = 20, quality = 3

print(w)

def outer():

    def inner():
        result = 2 + 5 
        return result
    
    return inner # возвращает результат выполнения inner

print(outer()) # вызывает функцию outer и выводит результат выполнения inner
print(outer()()) # вызывает функцию outer и выводит результат выполнения inner 
inner_function = outer() # присваивает переменной inner_function результат выполнения inner
print(inner_function()) # вызывает функцию inner_function и выводит результат выполнения inner


print(w)

def func1(give_me_a_func): # принимает функцию в качестве аргумента
    print('before func')
    give_me_a_func() # вызывает функцию в качестве аргумента
    print('after func')



def simple1(): # функция которая будет передаваться в качестве аргумента в функцию func1
    print('simple1')

def simple2():
    print('simple2')

simple1() # вызывает функцию simple1
simple2() # вызывает функцию simple2

func1(simple1) # передает функцию simple1 в качестве аргумента в функцию func1
func1(simple2) # передает функцию simple2 в качестве аргумента в функцию func1
        
def simple3():
    print('I')
    print('love')
    print('Python')
    print('very')
    print('much')

simple3()

func1(simple3)

print(w)

def add_text(func):

    def wrapper():
        print('before')
        func()
        print('after')

    return wrapper



def simple1(): # функция которая будет передаваться в качестве аргумента в функцию func1
    print('simple1')
simple1()
simple1 = add_text(simple1) # присваивает переменной simple1 результат выполнения функции add_text
simple1() #условно говоря это сейчас wrapper()


def simple2():
    print('simple2')
simple2()
simple2 = add_text(simple2) # присваивает переменной simple2 результат выполнения функции add_text
simple2() #условно говоря это сейчас wrapper()
print(simple2)

print(w)

def add_text(func):

    def wrapper():
        print('before')
        func()
        print('after')

    return wrapper


@add_text # означает что функция simple1 будет передаваться в качестве аргумента в функцию add_text
def simple1(): # функция которая будет передаваться в качестве аргумента в функцию func1
    print('simple1')


@add_text
def simple2():
    print('simple2')

simple1()  #условно говоря это сейчас add_text(simple1)()
simple2()  #условно говоря это сейчас add_text(simple2)() 

print(w)

def hyi(chlen):

    def wrapper():
        print("==========")
        chlen()
        print("==========")
    return wrapper

@hyi
def fank1():
    print('Big dick')

@hyi
def fank2():
    print('Small dick')

fank1()
fank2()

print(w)

def add_logs(func):

    def wrapper():
        print(f'Function {func.__name__} started') # выводит имя функции которая будет вызвана
        result = func()                            # помещаем функцию в переменную result, чтобы можно было после выполнения функции добавить пост-действие
        print(f'Function {func.__name__} finished')
        print('-'*50)
        return result # возвращает результат выполнения функции
       
    return wrapper

@add_logs
def simple1():
    print('simple1')
simple1()
#print(simple1.__name__) # выводит имя функции simple1

@add_logs
def simple2():
    print('simple2')   
simple2()

@add_logs
def print_nothing():
    pass
print(print_nothing())

print(w)

def add_logs(func):

    def wrapper(smth):
        print(f'Function {func.__name__} started') # выводит имя функции которая будет вызвана
        result = func(smth)                            # помещаем функцию в переменную result, чтобы можно было после выполнения функции добавить пост-действие
        print(f'Function {func.__name__} finished')
        print('-'*50)
        return result # возвращает результат выполнения функции
       
    return wrapper

@add_logs
def calc(x):
    print(x * 2)
calc(3)

print(w)

def func(*args): # *args - аргументы функции
    print(*args) # *args - распаковывает аргументы функции если добавить * перед аргументом

func(1, 2, 3)

print(w)

def multiply(a, b): # a и b - аргументы функции
    return a * b   # возвращает результат выполнения функции

ymn = multiply

result = multiply(3, 7) # вызывает функцию multiply с аргументами 3 и 7, но она нам не выводит результат, а возвращает его
print(result)
result2 = ymn(3, 7) # вызывает функцию multiply с аргументами 3 и 7, но она нам не выводит результат, а возвращает его
print(result2)
print(multiply) # выводит имя функции multiply
print(ymn) # выводит имя функции ymn

print(w)

def calculator(a, b):

    def add():
        return a + b
    return add()

print(calculator(1, 5))

print(w)

def highlight(func):

    def wrapper():
        print('***')
        func()
        print('***')
    return wrapper

@highlight
def my_name():
    print('Hello, Mr. Egor')
my_name()

# new_my_name = highlight(my_name)
# new_my_name()

print(w)

def show_name(func):
    def wrapper():
        func()
        print(func.__name__)
    return wrapper


@show_name
def hello():
    print('Hello, Mr. Egor')

@show_name
def good_bye():
    print('Goodbye, Mr. Egor')

hello()
good_bye()

print(w)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_list1 = []

# for x in my_list:
#     my_list1.append(x * 2)
# print(my_list1)

# new_list2 = map(lambda x: x * 2, my_list) #берем x из my_list и умножаем на 2(самый быстрый способ)
new_list3 = [x * 2 for x in my_list] # умножь x на 2 для каждого x в my_list
print(new_list3)

print(w)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list4 = []

for x in my_list:
    if x % 2 == 0:
        new_list4.append(x)
print(new_list4)

my_list5 = filter(lambda x: x % 2 == 0, my_list)
print(list(my_list5))


print(w)

new_list6 = [x for x in my_list if x % 2 == 0]
print(new_list6)
