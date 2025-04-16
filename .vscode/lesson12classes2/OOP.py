import json
w = '='*50

# def read_data(file_way): #функция для чтения данных из файла
#     file_data = open(file_way, 'r')#file_way - путь к файлу, r - режим чтения
#     data = json.load(file_data) #преобразование строки в словарь
#     print(data) #read для чтения файла
#     file_data.close() #закрытие файла
#     return data

# data1 = read_data('.vscode/lesson12classes2/data1.txt')
# data2 = read_data('.vscode/lesson12classes2/data2.txt')

# print(data1['Country'])
# print(data1['avg_temp'])
# print(data2['Country'])
# print(data2['avg_temp'])

print(w)

class CountryData:

    def __init__(self, file_way):  #конструктор класса. self - ссылка на объект класса, file_way - путь к файлу
        self.file_way = file_way   #ссылка на объект класса
        self.data = self.read_file() #вызов функции read_file
        self.country = self.data['Country'] #ссылка на объект класса
        self.__avg_temp = self.data['avg_temp'] #ссылка на объект класса. __ - защищенный атрибут(нельзя изменить)
        self.is_comfort = self.is_comfort() #ссылка на объект класса

    @property
    def data(self):
        return self.__avg_temp > 25

    def __read_file(self): #функция для чтения данных из файла
        file_data = open(self.file_way, 'r')#file_way - путь к файлу, r - режим чтения
        data = json.load(file_data) #преобразование строки в словарь
        print(data) #read для чтения файла
        file_data.close() #закрытие файла
        return data
    
    def __is_comfort(self):
        return self.avg_temp > 25
    
class CountryDataMinTemp(CountryData):
        def __init__(self, file_way):
            super().__init__(file_way)
            self.min_temp = self.data['min_temp']

data1 = CountryData('.vscode/lesson12classes2/data1.txt')
print(data1.data)
print(data1.country)
print(data1.avg_temp)
print(data1.is_comfort)


data2 = CountryData('.vscode/lesson12classes2/data2.txt')
print(data2.data)
print(data2.country)
print(data2.avg_temp)
print(data2.is_comfort)

data3 = CountryDataMinTemp('.vscode/lesson12classes2/data3.txt')
print(data3.data)
print(data3.country)
print(data3.avg_temp)
print(data3.is_comfort)







