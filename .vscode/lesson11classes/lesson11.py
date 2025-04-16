from abc import ABC, abstractmethod

w = '=' * 50

class Group:  # класс родитель
    students = True #
    shcool_number = 42
    director = 'Marivanna'

    def __init__(self, title, student_count, group_lider):
        self.title = title
        self.student_count = student_count
        self.group_lider = group_lider



    def study(self):  # метод класса. Отличается от функции тем, что идет в классе
        print('study')

    @abstractmethod # этот декоратор говорит, что метод должен быть реализован в подклассе
    def move(self): #абстрактный метод. обозначаем что каждый подкласс будет иметь свой метод move
        pass

class PrimaryGroup(Group): # класс наследник(наследует все свойства и методы класса Group)
    max_age = 11
    min_age = 6
    location = 'left'

    def __init__(self, title, student_count, group_lider, classroom): # конструктор класса, нужен для того чтобы передавать параметры в класс
        super().__init__(title, student_count, group_lider) # вызываем конструктор класса родителя
        self.classroom = classroom # добавляем новое свойство

    def move(self):
        print('run fust')


class HightGroup(Group):
    max_age = 18
    min_age = 14

    def move(self):
        print('go slowly')

class MediumGroup(Group):
    max_age = 14
    min_age = 10

#объект класса = экземпляр класса = представитель класса = экземпляр класса
#подгруппы не знают друг о друге и не могут использовать дхарактеристики руг друга
print(w)

first_a = PrimaryGroup('1a', 20, 'MF', 5) #создаем объект класса PrimaryGroup.То есть у first_a будут характеристики PrimaryGroup
eleven_a = HightGroup('1b', 18, 'TD') #создаем объект класса HightGroup.То есть у eleven_a будут характеристики HightGroup
six_a = MediumGroup('1c', 12, 'MF') #создаем объект класса MediumGroup.То есть у six_a будут характеристики MediumGroup

print(first_a.classroom) # выводим свойство classroom объекта first_a
print(first_a.student_count) # выводим свойство student_count объекта first_a
print(first_a.title) # выводим свойство title объекта first_a
print(first_a.group_lider) # выводим свойство group_lider объекта first_a

print(first_a.location) # выводим свойство location объекта first_a
print(eleven_a.max_age) # выводим свойство max_age объекта eleven_a
print(eleven_a.students) # выводим свойство students объекта eleven_a
print(first_a.director  ) # выводим свойство director объекта first_a

first_a.study()
eleven_a.study()

first_a.move()
eleven_a.move()
six_a.study()

print(w)


class Device:

    def __init__(self, name):
        self.name = name

    def power_on(self):
        print(f'{self.name} включено')

class SmartPhone(Device):

    def make_call(self, number):
        print(f'Звоню по номеру {number}')

iphone = SmartPhone('iphone')

iphone.power_on()

iphone.make_call(89889905968)



print(w)



class Animal:    #класс родитель
    def __init__(self, name): #конструктор класса. self - это ссылка на объект класса, name - это параметр конструктора
        self.name = name #свойство класса. Сюда передается параметр name

    def sound(self, name):  #метод класса. self - это ссылка на объект класса, name - это параметр метода
        print(f'{self.name} издает звук') #метод класса. self - это ссылка на объект класса, name - это параметр метода
        
    

class dog(Animal):
    def sound(self):
       super().sound(self.name)  #вызываем метод sound класса родителя
       print(f'{self.name} издает звук гав')

class cat(Animal):
    def sound(self):
        super().sound(self.name)
        print(f'{self.name} издает звук мяу')


dog1 = dog('Бобик') #создаем объект класса dog
dog2 = dog('Шарик') #создаем объект класса dog

cat1 = cat('Мурка') #создаем объект класса cat
cat2 = cat('Пушок') #создаем объект класса cat

dog1.sound() #вызываем метод speak объекта dog1
dog2.sound() #вызываем метод speak объекта dog2

cat1.sound() #вызываем метод speak объекта cat1
cat2.sound()



print(w)


class Employee(ABC):  #класс родитель. ABC - абстрактный базовый класс.
    def __init__(self, name, position): #конструктор класса. self - это ссылка на объект класса, name - это параметр конструктора, position - это параметр конструктора
        self.name = name #свойство класса. Сюда передается параметр name
        self.position = position #свойство класса. Сюда передается параметр position

    @abstractmethod #декоратор абстрактного метода.
    def calculate_salary(self): #абстрактный метод.
        # "Рассчет зп"
        pass

class HourlyEmployee(Employee): #класс наследник.
    def __init__(self, name, position, hourly_rate, hours_worker): #конструктор класса. self - это ссылка на объект класса, name - это параметр конструктора, position - это параметр конструктора, hourly_rate - это параметр конструктора, hours_worker - это параметр конструктора
        super().__init__(name, position) #вызываем конструктор класса родителя
        self.hourly_rate = hourly_rate #добавляем новое свойство
        self.hours_worker = hours_worker #добавляем новое свойство

    def calculate_salary(self): #метод класса.
        print(f'{self.name} заработал {self.hourly_rate * self.hours_worker} рублей') #выводим результат расчета заработка



class SalariedEmployeed(Employee): #класс наследник.
    def __init__(self, name, position, monthly_salary): #конструктор класса. self - это ссылка на объект класса, name - это параметр конструктора, position - это параметр конструктора, monthly_salary - это параметр конструктора
        super().__init__(name, position) #вызываем конструктор класса родителя
        self.montly_salary = monthly_salary #добавляем новое свойство

    def calculate_salary(self): #метод класса.
        print(f'{self.name} заработала {self.montly_salary} рублей') #выводим результат расчета заработка


Egor = HourlyEmployee('Egor', 'Разработчик', 1000, 160) #создаем объект класса HourlyEmployee
Maasha = SalariedEmployeed('Masha', 'Директор', 50000) #создаем объект класса SalariedEmployeed

Egor.calculate_salary() #вызываем метод calculate_salary объекта Egor
Maasha.calculate_salary() #вызываем метод calculate_salary объекта Maasha



