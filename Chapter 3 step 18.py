# Напишите программу, которая выводит "Зеркально отраженное" четыехзначное положительно число.
# При этом если  введено не четырехзначное число или получившееся число не является четырехзначноым
# на экран выводится ошибка.

number5 = int(input('Введите четырхзначное число: '))
if 999< number5 <10000:                  #  Условие только 4 значное число и только положительное
    number1 = int(number5 / 1000)        #  Находим четвертую цифру
    number2 = int((number5 /100) % 10)   #  Находим третью цифру
    number3 = int((number5 % 100)/10)    #  Находим вторую цифру
    number4 = int(number5 % 10)          #  Находим первую цифру
    print(number4,number3,number2,number1)
else:
    print('Введена неправильное число, которое не в ходит в диапазон либо введен текст') 