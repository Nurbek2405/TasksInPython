# 8 
# Напишите программу, которая вычисляет произведение двух чисел, введенных с клавиатуры но выводит его три раза. 
# Используйте в задаче функции преобразования типов int() и str().

from re import I


a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))

print(str(a*b)*3+'\n')

# 9
# Напишите программу, которая выводит строку, 
# введенную пользователем с клавиатуры, столько раз, сколько запросил пользователь
a1=str(input('Введите строку: '))
a2=int(input('Введите количество повторений: '))
print(a1*a2+'\n')

# 10
# Напишите программу, которая просит пользователя ввести сообщение 
# и выводит его с комментарием для другого человека.

b2=str(input('Введите сообщение:'))
print('Для Вас одно новое сообщение: ',b2+'\n')

# 11
# Напишите программу, которая запрашивает количество покупаемых продуктов 
# и выводит общую стоимость покупки. Используйте следующую таблицу стоимости проудктов:
# хлеб - 35.5 руб. молоко - 74 руб. масло - 120 руб. 

c1=float(input('Количество покупаемых единиц хлеба: '))
c2=int(input('Количество покупаемых единиц молока: '))
c3=int(input('Количество покупаемых единиц масла: '))
summa = c1*35.5+c2*74+c3*120
print('Общая сумма к оплате - ', summa ,' руб.')