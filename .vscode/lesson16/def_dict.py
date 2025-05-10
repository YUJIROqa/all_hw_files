import collections

with open('.vscode/lesson16/shop.txt', 'r') as shops_file:
    shops = map(lambda x: x.replace('\n', ''), shops_file.readlines()) #для каждой строки(x) в файле
                                                     #заменяем /n на пустую строку

city_shops = collections.defaultdict(list) #создаем словарь, который будет хранить список городов для каждого магазина
for line in shops:
    shop, city = line.split(':') #разделяем строку на два элемента
    city_shops[shop] = city #добавляем в словарь. в словарь добавляем ключ(shop) и значение(city)

print(city_shops)


