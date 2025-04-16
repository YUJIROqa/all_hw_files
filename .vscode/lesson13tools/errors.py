def calc(x, y):
    try:
        return int(x)/int(y)
    except ZeroDivisionError as err:
        print(x, y)
        raise err
        # print(err)
        # print('На ноль делить нельзя')
        #тут как булто есть return None
    except ValueError as err2:
        print(x, y)
        raise err2
        # print(err2)
        # print('Вы ввели не число')
    

print(calc(input('Number 1: '), input('Number 2: ')))
print('Hello')