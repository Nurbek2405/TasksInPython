# Пример игры random

import random                                           # подключаем модуль генератора случайных чисел

print("Примеры игры random, кладем псевдослучайное число от 0 до 10: ")
a=random.randint(0,10)
n=3                                                         # 3 попытки
for i in range(n):
    b=int(input('Введите цифру с клавиатуры: '))            # кладем в b целое число, введенное пользователем 
    print('У вас осталось попыток: ',2-i)                   # вывод остаток попыток на экран
    if a == b:                                              # условие
        print('Поздравляем! Вы выиграли')                   
        break                                               # выйти из цикла если, угадали
    elif a>b:
        print('Загаданное число больше введенного: ')
    else:
        print('Загаданное число меньше введенного: ')