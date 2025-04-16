import json

w = '='*50

# def read_file(filename):
#     file_data = open(filename, 'r') #открытие файла, r - режим чтения
#      #data = file_data.read() #создаем переменную data ы которую записываем чтение file_data
#     data = json.load(file_data) #преобразование строки в словарь с помощью json модуля 
#     print(data) #вывод переменной data
#     file_data.close() #закрытие файла
#     return data #возвращаем данные

# data1 = read_file('.vscode/lesson12classes2/data1.txt')
# data2 = read_file('.vscode/lesson12classes2/data2.txt')

# print(data1['Country'])
# print(data1['avg_temp'])
# print(data2['Country'])
# print(data2['avg_temp'])


# class CountryData:

#     def __init__(self, filename): #конструктор класса
#         self.filename = filename  #атрибут класса
#         self._data = self.read_file()  #метод класса, сохраняем в _data
#         self._country = self._data['Country']
#         self._avg_temp = self._data['avg_temp']
#         self._is_comfort = self.check_comfort()

#     @property
#     def data(self):
#         return self._data
    
#     @property
#     def country(self):
#         return self._country
    
#     @property
#     def avg_temp(self):
#         return self._avg_temp
    
#     @property #декоратор свойства нужен для того чтобы можно было обращаться к атрибуту как к свойству
#     def is_comfort(self):
#         return self._is_comfort
        
#     @is_comfort.setter
#     def is_comfort(self, value):
#         self._is_comfort = value

#     def read_file(self):
#         file_data = open(self.filename, 'r') #открытие файла, r - режим чтения
#         data = json.load(file_data) #преобразование строки в словарь с помощью json модуля 
#         file_data.close() #закрытие файла
#         return data #возвращаем данные
    
#     def check_comfort(self):  # переименовал метод, чтобы не конфликтовал со свойством
#         return self._avg_temp > 25
    
#     def __str__(self):
#         return f'File {self.filename} with data {self._data}'
    
#     def __lt__(self, obj):
#         return self.avg_temp < obj.avg_temp
    
#     def __le__(self, obj):
#         return self.avg_temp <= obj.avg_temp
    
#     def __add__(self, obj):
#         return self.avg_temp + obj.avg_temp


    
# class CountryDataWithMinTemp(CountryData):
#     def __init__(self, filename): #конструктор класса. Инициализация класса CountryDataWithMinTemp
#         super().__init__(filename) #вызов конструктора класса CountryData. self - ссылка на объект класса
#         self._min_temp = self._data['min_temp'] #атрибут класса добовляемый в класс CountryDataWithMinTemp
    
#     @property
#     def min_temp(self):
#         return self._min_temp


# data1 = CountryData('.vscode/lesson12classes2/data1.txt')
# print(data1.data)
# print(data1.country)
# print(data1.avg_temp)
# print(data1.is_comfort)

# data2 = CountryData('.vscode/lesson12classes2/data2.txt')
# print(data2.data)
# print(data2.country)
# print(data2.avg_temp)
# print(data2.is_comfort)

# data3 = CountryDataWithMinTemp('.vscode/lesson12classes2/data3.txt')
# print(data3.data)
# print(data3.country)
# print(data3.avg_temp)
# print(data3.is_comfort)
# print(data3.min_temp)

# print(data1)
# print(data1 < data2)
# print(data1 <= data2)
# print(data1 > data2)
# print(data1 >= data2)
# print(data1 + data2)

print(w)

class Book:

    def __init__(self, title, author, date_creation):
        self._title = title
        self._author = author
        self._date_creation = date_creation #self.date_creation означает что мы присваиваем атрибуту date_creation значение date_creation
    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def date_creation(self):
        return self._date_creation
    
    @date_creation.setter
    def date_creation(self, value):
        if value == '':
            raise ValueError('Дата не может быть пустой')
        elif value <= 0:
            raise ValueError('Дата не может быть отрицательной или нулевой')
        else:
            self._date_creation = value #присваиваем атрибуту date_creation значение value что бы не нарушать инкапсуляцию

    @author.setter
    def author(self, value):
        if value == '':
            raise ValueError('Автор не может быть пустым')
        else:
            self._author = value

    @title.setter
    def title(self, value):
        if value == '':
            raise ValueError('Название не может быть пустым')
        else:
            self._title = value
        


    def get_age(self):
        return 2025 - self._date_creation
    
    def get_info(self):
        return f'Книга "{self._title}", автор: {self._author}, издана в {self._date_creation} году'
    
    def __str__(self):
        return f'"{self._title}": {self._authot}, {self._date_creation}'
    
    def __lt__(self, obj):
        return self._date_creation < obj._date_creation
    
    def __eq__(self, obj):
        return len(self._title + self._author) > len(obj._title + obj._author)
    



book1 = Book('Game of Thrones', 'George R.R. Martin', 1996)
print(book1.author)
print(book1.title)
print(book1.date_creation)
print(book1.get_age())
print(book1.get_info())


book2 = Book('The Hobbit', 'J.R.R. Tolkien', 1937)
print(book2.author)
print(book2.title)
print(book2.date_creation)
print(book2.get_age())
print(book2.get_info())

try:
    book1.date_creation = -1
    print('Значение успешно изменено')
except ValueError as error:
    print(error)

try:
    book1.title = ''
    print('Значение успешно изменено')
except ValueError as error:
    print(error)

try:
    book1.author = ''
    print('Значение успешно изменено')
except ValueError as error:
    print(error)

print(w)


class EBook(Book):
    def __init__(self, title, author, date_creation, file_format, file_size, download_url): #при инициализации дочернего класса мы передаем и родительские аргументы и новые(которые будут только у дочернего класса)
        super().__init__(title, author, date_creation) #при вызове родительского класса мы передает только аргументы родительского класса
        self._file_format = file_format
        self._file_size = file_size
        self._download_url = download_url

    @property
    def file_format(self):
        return self._sile_format
    
    @property
    def file_size(self):
        return self._file_size
    
    @property
    def download_url(self):
        return self._download_url
    
    def get_info(self):
        return f'Книга "{self._title}", автор {self._author}, издана в {self._date_creation} году, формат файла {self._file_format}, размер файла {self._file_size} МБ, ссылка для скачивания {self._download_url}'
    
    def get_download_link(self):
        return f'Файл можно скачать по ссылке: {self._download_url}'
    

book3 = EBook('Dune', 'Frank Herbert', 1965, 'epub', 1.5, 'https://example.com/dune.epub')
print(book3.get_info())
print(book3.get_download_link())


print(book1.date_creation < book2.date_creation)
print()
