from faker import Faker

fake = Faker(locale='ru_RU')

for i in range(5):
    print(fake.job())
