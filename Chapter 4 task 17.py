# Напишите программу, которая вычисляет факториал неотрицательного числа, введенного с клавиатуры
# и выводит ошибку, если пользователь ввел отрицательное число.


numberint = int (input('Введите натуральное число: '))  # Сообщение для пользователя

if numberint == 0:                                      # если равно 0 то уравнять к 1
        numberint=1                                     # приравнивание числа к 1, если введена цифра 0

if numberint>0:                                         # если цифра больше то выполняется основное условие, вычисление факториала
    for i in range(1,numberint):                        # цикл начинается с 1, до введенного числа
        numberint=numberint*i                           # присвоение факториала к следующему значению
    print("Факториал числа = ",numberint)               # вывод сообщений в конце цикла, к чему равен факториал
else:                                                   # если нет, то
    print('Введено минусовое число:',numberint)         # выполняется вывод сообщений, то что введено отрицательное число