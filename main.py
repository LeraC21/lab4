def p1():
    try:
        a = int(input('Введите число, чтобы проверить деление на 3: '))
        b = a % 3
    except ValueError:
        print('Введите не число')
    else:
        if b == 0 and a != 0:
            print('Число', a, 'делится на 3')
        else:
            print('Число', a, 'не делится на 3')

def p2():
    try:
        a = int(input('Введите число: '))
        b = 100 / a
    except ZeroDivisionError:
        print('Ввиден 0')
    except ValueError:
        print('Введино не число')
    else:
        print('Результат деления 100 на введеное число: ', b)

def p3(data):
        data = input('Введите дату: ')
        data = data.split('.')
        if int(data[0]) * int(data[1]) == int(data[2][2:4]):
            print('Дата магическая')
        else:
            print('Дата не магическая')

def p4(ticket):
    ticket = input('Введите число:')
    sum1 = sum([int(i) for i in ticket[:int(len(ticket) / 2)]])
    sum2 = sum([int(i) for i in ticket[int(len(ticket) / 2):]])
    if sum1 == sum2:
        print('Число счастливое')
    else:
        print('Число не счастливое')

p1() , p2() , p3(input) , p4(input)