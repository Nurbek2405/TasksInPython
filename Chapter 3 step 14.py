# 14 задача, Напишите программу, которая определяет, входит ли число, введенное пользователем, в отрезок -50 до 50

numa=float(input('Введите любое число от -50 до 50\n'))
if numa <= 50 and numa >= -50:
    print('Число ',numa, 'принадлежит диапазону -50 до 50')
else:
    print('Число ',numa, 'не принадлежит диапазону -50 до 50')

# 15 задача, Напишите программу, которая определяет, входит ли число, введенное пользователем, в полуинтервале -50 до 50

numa=float(input('Введите любое число от -50 до 50\n'))
if numa < 50 and numa > -50:
    print('Число ',numa, 'принадлежит диапазону -50 до 50')
else:
    print('Число ',numa, 'не принадлежит диапазону -50 до 50')
