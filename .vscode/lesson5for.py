# user_input = input('Print a number: ')
# if user_input.isnumeric():
#     user_input = int(user_input)
#     if user_input == 1:
#         print('One')
#     elif user_input == 2:
#         print('two') 
#     else:
#         print('other')
# else:
#     print('Enter a number')
    
w = '='*50
print(w)

#Loop - циклы
names = ['John', 'Anna', 'Jim', 'Bob', 'Jack', 'Elice']

for name in names:
    if name.startswith('J'):
        print('Mr. ',end = '') #end = '' - не переходит на новую строку 
    print(name)
    
print(w)

names = ('John', 'Anna', 'Jim', 'Bob', 'Jack', 'Elice')

for name in names:
    if name.startswith('J'):
        print('Mr. ',end = '') #end = '' - не переходит на новую строку 
    print(name)

print(w)

names = {'John', 'Anna', 'Jim', 'Bob', 'Jack', 'Elice'}

for name in names:
    if name.startswith('J'):
        print('Mr. ',end = '') #end = '' - не переходит на новую строку 
    print(name)

print(w)

persons = {'Jhon': 132, 'Anna': 123, 'Jim': 123, 'Bob': 123, 'Jack': 123, 'Elice': 123}
for person in persons:
    print(person)

print(w)

persons = {'Jhon': 132, 'Anna': 117, 'Jim': 154, 'Bob': 181, 'Jack': 161, 'Elice': 163}
print(persons.values())
for person in persons.values():
    print(person)

print(w)

persons = {'Jhon': 132, 'Anna': 117, 'Jim': 154, 'Bob': 181, 'Jack': 161, 'Elice': 163}

for name, height in persons.items():
    print(f'{name}: {height}')

print(w)

text = 'Sed vitae justo malesuada, commodo liberia eu bidendum mauris'

words = text.split()
print(words)
with_a = []
without_a = []

for word in words:
    if 'a' in word:
        with_a.append(word)
    else:
        without_a.append(word)
print(', '.join(with_a))
print(', '.join(without_a))

