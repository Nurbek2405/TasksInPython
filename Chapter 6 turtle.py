# Чтобы объект Черепашка начертил отрезок, достаточно воспользоваться функциями forward(L) или backward(L). 
# Например, чтобы нарисовать отрезок длиной в 50 единиц (рис. 39) необходим следующий код: 

import turtle as t          # подключаем черепаху

for i in range(24):         # цикл для уменьшение кода
    t.forward(50)           # вперед
    t.left(30)              # поворот на 30 градусов
