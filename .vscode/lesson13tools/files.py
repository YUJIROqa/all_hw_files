import os
w = '='*50
# data_file = open(".vscode/lesson13tools/data.txt", "r")
# print(data_file.read())
# print('asfasdf' + 1)
# data_file.close()
print(w)

base_path = os.path.dirname(__file__)
#file_path = f'{base_path}/data.txt'
file_path = os.path.join(base_path, 'data.txt')
new_file_path = os.path.join(base_path, 'data1.txt')
print(file_path)

print(w)


def read_file():
    with open(file_path, "r") as data_file:
       for line in data_file.readlines():  
           yield line

for data_line in read_file():
    with open(new_file_path, 'a') as new_file:
        data_line = data_line.replace('.', '').replace(',', '')
        new_file.write(data_line)

print(w)

homework_path = os.path.dirname(base_path)
alina_file_path = os.path.join(homework_path, 'testdata.txt')
print(alina_file_path)

print(w)

with open(alina_file_path, 'r') as alina_file:
    print(alina_file.read())

print(w)

with open('.vscode/lesson13tools/hw_data', 'r') as hw_data:
    hw_data = hw_data.readlines()
    print(hw_data)

print(w)

with open('.vscode/lesson13tools/hw_data', 'r') as hw_data:
    hw_data = hw_data.read()
    print(hw_data)

print(w)

with open('.vscode/lesson13tools/hw_data', 'r') as hw_data:
   for line in hw_data:
       print(line)

print(w)


def create_user_file(filename, name, age, hobby): #функция принимает название файла, имя, возраст и хобби
    with open(filename, 'w') as user_profile: #открывает(а в нашем случае создает) файл с названием filename(его передаем в функции)
        user_profile.writelines([f'Name:{name}\n', f'Age:{age}\n', f'Hobby:{hobby}']) #записывает в файл строки(список)
    

create_user_file('user_profile.txt', 'Egor', 23, 'Sport') #вызываем функцию и передаем в нее параметры

with open('user_profile.txt', 'r') as user_profile: #открываем файл с названием user_profile.txt
    print(user_profile.read()) #читаем файл

print(w)

# Решение:

# Создаем файл и записываем информацию
with open(".vscode/lesson13tools/my_info.txt", "w") as file: #создаем файл в нужной дерриктории
    file.write("Имя: Иван\n") #записываем в файл строки
    file.write("Возраст: 25\n")
    file.write("Хобби: Программирование\n")

# Открываем файл для чтения и выводим содержимое
with open(".vscode/lesson13tools/my_info.txt", "r") as file:
    content = file.read()
    print(content)

print(w)

current_dir = os.path.dirname(__file__) #возвращает путь к текущей директории
print(current_dir)

new_dir = os.path.join(current_dir, 'user_data.txt') #возвращает путь к файлу в нужной директории
print(new_dir)

with open(new_dir, 'w') as new_file: #создает файл в нужной директории
    new_file.write('Это текстовый файл') #записывает в файл строку

check_new_file = os.path.exists(new_dir)
print(check_new_file)

full_path = os.path.abspath(new_dir) #возвращает абсолютный путь к файлу
print(full_path)

print(w)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
def read_line(file_path):
    with open(file_path, 'r') as file:
        return file.readline()
    
def read_lines(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()
    
def read_for_loop(file_path):
    result = []
    with open(file_path, 'r') as file:
        for line in file:
            result.append(line)
    return result

print('read_file, ', read_file('.vscode/lesson13tools/sample.txt'))
print('read_line, ', read_line('.vscode/lesson13tools/sample.txt'))
print('read_lines, ', read_lines('.vscode/lesson13tools/sample.txt'))
print('read_for_loop, ', read_for_loop('.vscode/lesson13tools/sample.txt'))

print(w)

def safe_read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError as err1:
        return err1
    
print(safe_read_file('.vscode/lesson13tools/sample.txt'))

print(safe_read_file('.vscode/lesson13tools/sample2.txt'))

print(w)

def safe_write_file(filename, data):
    # Объявляем функцию с двумя параметрами:
    # filename - путь к файлу, в который будем записывать
    # data - данные, которые нужно записать в файл
    
    try:
        # Блок try обозначает код, который может вызвать исключение
        # Python попытается выполнить этот код, и если возникнет ошибка,
        # выполнение перейдет в блок except
        
        with open(filename, 'w') as file:
            # Открываем файл в режиме записи ('w' = write)
            # Конструкция 'with' автоматически закроет файл после выхода из блока,
            # даже если произойдет ошибка
            # Переменная 'file' содержит объект открытого файла
            
            file.write(data)
            # Метод write() записывает переданные данные в файл
            # Возвращает количество записанных символов, но мы не используем это значение
            
            return True
            # Если запись прошла успешно (не было исключений),
            # функция возвращает True, сигнализируя об успехе операции
            
    except Exception as error:
        # Если в блоке try возникла любая ошибка, выполнение перейдет сюда
        # Exception - базовый класс для большинства исключений в Python
        # 'as error' сохраняет объект исключения в переменную error
        
        print(f'Ошибка при записи в файл {filename}: {error}')
        # Выводим информативное сообщение об ошибке, включая:
        # - путь к файлу, с которым возникла проблема
        # - конкретную информацию об ошибке (тип и описание)
        
        return False
        # Возвращаем False, сигнализируя о неудаче операции

# Тестирование функции с корректным путем к файлу
print(safe_write_file('.vscode/lesson13tools/sample1.txt', 'Hello, world!'))
# Должно вернуть True и создать/перезаписать файл sample1.txt

# Тестирование функции с некорректным путем к файлу
print(safe_write_file('.vscode/lesson13tваыools/sample2.txt.b2b', 'Hello, world!'))
# Должно вернуть False и вывести сообщение об ошибке,
# так как путь содержит русские символы и, вероятно, не существует

print(w)

def file_operation(filename, operation, data=None):
    # Функция для выполнения операций с файлами с обработкой ошибок
    # Параметры:
    #   filename - путь к файлу
    #   operation - тип операции: 'read' для чтения, 'write' для записи
    #   data - данные для записи (используется только при operation='write')
    
    try:
        # Блок try для перехвата возможных ошибок при работе с файлом
        
        if operation == 'read':
            # Если операция - чтение файла
            with open(filename, 'r') as file:
                # Открываем файл в режиме чтения ('r')
                # Используем конструкцию with, которая автоматически закроет файл
                # даже если произойдет ошибка
                
                return file.read()
                # Читаем всё содержимое файла и возвращаем его как строку
                # Если функция выполнится успешно, она вернет содержимое файла
                
        elif operation == 'write':
            # Если операция - запись в файл
            with open(filename, 'w') as file:
                # Открываем файл в режиме записи ('w')
                # Режим 'w' создаст новый файл или перезапишет существующий
                
                file.write(data)
                # Записываем переданные данные в файл
                
            return True
            # После успешной записи возвращаем True
            # Обратите внимание, что этот return находится вне блока with,
            # так как файл уже закрыт, и мы просто сообщаем об успехе
            
    except Exception as error:
        # Если в блоке try произошла любая ошибка (например, файл не найден,
        # недостаточно прав доступа, ошибка кодировки и т.д.),
        # выполнение перейдет сюда
        
        print(f'Ошибка при выполнении операции {operation}: {error}')
        # Выводим информативное сообщение об ошибке, включая:
        # - тип операции, которая вызвала ошибку
        # - конкретную информацию об ошибке из объекта error
        
        return None if operation == 'read' else False
        # Возвращаем разные значения в зависимости от типа операции:
        # - None для ошибки чтения (так как нет данных для возврата)
        # - False для ошибки записи (противоположность True при успехе)
        # Это условное выражение (тернарный оператор) эквивалентно:
        # if operation == 'read':
        #     return None
        # else:
        #     return False

# Пример использования функции для чтения файла:
content = file_operation('.vscode/lessoбn13tools/sample.txt', 'read')
# Вызываем функцию для чтения файла sample.txt
# Обратите внимание: в пути есть русская буква 'б', это, вероятно, опечатка,
# которая приведет к ошибке FileNotFoundError
# Результат (содержимое файла или None при ошибке) сохраняется в переменную content

print("Содержимое файла:", content)
# Выводим результат. Если была ошибка, content будет None,
# и мы увидим: "Содержимое файла: None"

# Пример использования функции для записи в файл:
success = file_operation('.vscode/lessdsgvon13tools/output.txt', 'write', 'New data')
# Вызываем функцию для записи строки 'New data' в файл output.txt
# Обратите внимание: в пути есть опечатка 'lessdsgvon13tools',
# что приведет к ошибке FileNotFoundError
# Результат (True при успехе или False при ошибке) сохраняется в переменную success

print("Запись успешна:", success)
# Выводим результат. Если была ошибка, success будет False,
# и мы увидим: "Запись успешна: False"