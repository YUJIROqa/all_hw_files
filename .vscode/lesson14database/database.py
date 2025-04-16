import psycopg2
import psycopg2.extras

w = '='*50


db = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = '1488',
    port = '5432'
)

print(w)

cursor = db.cursor(cursor_factory=psycopg2.extras.DictCursor) #переменная которая говорит что сделать с базой данных
                                                   #в скобках указывается чтобы данные были в виде словаря
cursor.execute('SELECT * FROM students') #вывод всех строк

data = cursor.fetchall() #вывод всех строк

for student in data:
    print(student['last_name'])

print(w)

cursor.execute('SELECT * FROM students WHERE id = 2') #эти данные не будут выведены
cursor.execute('SELECT * FROM students WHERE id = 3') #а эти будут
data2 = cursor.fetchone() #вывод одной строки

print(data2) #вывод в виде кортежа(просто перебор)
print(dict(data2)) #вывод в виде словаря(ключ-значение)

print(w)

#query = "SELECT * FROM students WHERE first_name = '{0}' and last_name = '{1}'" #вывод данных по имени и фамилии
query = "SELECT * FROM students WHERE first_name = %s and last_name = %s" #%s - это переменная
cursor.execute(query, (input('first_name: '), input('last_name: ')))
print(cursor.fetchone())
#Алексей'; -- можем написать так, чтобы выводило данные по имени Алексей
#тк -- это комментирование кода SQL и дальше идет выполнение кода 
#работает только с {}, с %s не работает(безопасней)

print(w)


cursor.execute("INSERT INTO students (first_name, last_name, grade, group_id) VALUES ('Сидр', 'Сидоров', 5, 1)")
db.commit() #сохраняет изменения в базе данных
#нужно выполнять весь код или выделять импорты что бы не было ошибок

print(w)

my_num = 34

while True:
    user_num = int(input('Введите число: '))
    if user_num == my_num:
        break
    elif user_num > my_num:
        print('Число должно быть меньше')
    else:
        print('Число должно быть больше')

print('Congratulations!')

print(w)

while True:
    user_input2 = input('Say something: ')
    match user_input2: #match - это оператор сравнения
        case 'hello': #case - это условие(if)
            print('Hello!')
        case 'bye':
            print('Bye!')
        case 'end':
            print('Goodbye!')
            break
        case _: #если нет ни одного из условий
            print('Hi or bye')

print(w)



while True:
    user_input = input('Введите команду: ')
    match user_input:
        case 'show all':
            try:
                cursor.execute("SELECT * FROM students")
                students = cursor.fetchall() 
            except psycopg2.DatabaseError as err:
                print(err)
        case 'find by name':
            try:
                name = input('Введите имя: ')
                cursor.execute("SELECT * FROM students WHERE first_name = %s", (name,))
            except psycopg2.DatabaseError as err:
                print(err)
        case 'exit':
            break
        case _:
            print('Неизвестная команда')
                












db.close()