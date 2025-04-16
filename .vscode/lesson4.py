my_list = [1, 3]
my_tuple = (2, 6 ,9)
 
a, b = my_list
c, d, e = my_tuple

print(a, b)
print(c, d, e)

a = '='*50

print(a)

lll = [1, 3, 5, 2, 5, 7, 1, 3]
print(lll)
print(lll[0:4]) #до идет не включая 4
print(lll[:4]) #от начала до 4
print(lll[3:]) #от 3 до конца
print(lll[1::2]) #шаг 2
print(lll[::-1]) #перевернуть список
print(lll[::-2]) #шаг 2, перевернуть список

print(a)

text = 'my long long string'

print(text[3])
print(len(text))
print(text.index('l'))
print('Long' in text) #проверка на наличие подстроки
print(text.count('l')) #количество подстрок
print(text.find('long')) #найти подстроку
print(text[:7]) #от начала до 7
print(text.startswith('ky')) #проверка на начало

print(a)

txt = 'This is a long long string'
print(txt.capitalize()) #первая буква большая
print(txt.title()) #каждая первая буква большая
print(txt.upper()) #все буквы большие
print(txt.lower()) #все буквы маленькие
print(txt.swapcase()) #большие и маленькие буквы меняются местами

print(a)

msg = 'Hello world'
msg.replace('world', 'universe') #заменить подстроку
msg = msg.replace('world', 'universe') #
print(msg)

print(a)

data = '12,3'
data = data.replace(',', '.')
print(data)

print(a)

text = ' word '
text = text.strip() #удалить пробелы, lstrip() - слева, rstrip() - справа
print(text)

text2 = '"name"'
text2 = text2.strip('"') #удалить кавычки
print(text2)


print(a)

my_string3 = 'some little text'
my_string3 = my_string3.replace(' ', '')
print(my_string3)


print(a)

my_string = 'some little text'
my_string2 = 'some,little,text'
list_from_text = my_string.split() #разделить строку на список
list_from_text2 = my_string2.split(',') #разделить строку на список по запятой
print(list_from_text)
print(list_from_text2)

print(a)

languages = ['Python', 'Java', 'C++', 'Ruby', 'C#']
print(languages)
#languages = ', '.join(languages) #объединить список в строку
print(languages)
print('Studenst knows these languages:', ', '.join(languages)) #объединить список в строку с пробелами

print(a)
 

a = 'one'
b = 'two'
print('First word is:', a, 'and second word is:', b)

my_text = 'First word is {1}, second word is {0}' #первый аргумент - второй, второй аргумент - первый
print(my_text.format(a, b)) 

#f-string
my_text = f'First word is {a}, second word is {b}' #выводит значения переменных в строку 
print(my_text)
 
print(a)

template = 'Hello, {0}' #формальный параметр
#username = input('What is your name?') #фактический параметр
#print(template.format(username)) #подставить фактический параметр в формальный

print(a)

text = 'error'
print(text.upper())

browsers = ['Chrome', 'Firefox', 'Edge', 'Safari']
print(', '.join(browsers))

textt = 'Автоматизация тестирования'
textt = textt.lower()
print(textt.count('а'))

texttt = 'Обнаружен деффект в работе приложения'
print(texttt.replace('деффект', 'ошибка'))

test_name = 'Проверка'
test_status = 'прошла'
test_status2 = 'закончилась'
test_result = 'успешно'
test_result2 = 'неудачно'


print(f'{test_name} {test_status} {test_result}')
print(f'{test_name} {test_status2} {test_result2}')