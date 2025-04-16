import random
import helper

w = '='*50

def generate_text(text1, text2):
    return f'Text consists of the words: {text1} and {text2}'
print(generate_text('Ivan', 'Petrov'))

print(w)

n = 2
progression = []
num = 0
while len(progression) < 500:
    progression.append(num)
    num += n
print(progression)

print(w)

def progression(limit = 100):
    n = 2
    num = 1
    count = 0
    while count < limit:
        yield num
        num += n
        count += 1
print(list(progression(10)))

for number in progression(10):
    print(number)


count = 1 # счетчик
for number in progression(1001): # генератор  
    if count == 1000: # если счетчик равен 1000000, то выводим число и выходим из цикла
        print(number) # выводим число
        break # выходим из цикла
    count += 1 # увеличиваем счетчик на 1


print(w)


print(int(random.random() * 100)) # случайное число от 0 до 100 целое 
print(random.randint(1, 100)) # случайное число от 1 до 100
print(random.randrange(1, 100, 2)) # случайное число от 1 до 100 с шагом 2

users = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7', 'user8', 'user9', 'user10', 'user11', 'user12', 'user13', 'user14', 'user15']
print(random.choice(users)) # случайный элемент из списка
print(users[random.randrange(0, len(users))]) # случайный элемент из списка

print(w)

helper.assist()
print(helper.variable)

