# Конкатенация и дублирование, для списков, как и для строк, выполнимы операции конкатенации и дублирования с помощью операторов + и * соответственно. Например


# Создание списков различными способами
List6 = ['a','b','c']
List7 = ['abc']
List8 = [range(-4,2,2)]
# Печать списков для наглядности
print(List6)
print(List7)
print(List8)
# Конкатенация всех списков
listnew1 = List6 + List7 + List8
print('Конкатенация всех списков',listnew1)
# Дублирование списка 
listnew2 = List6*2
print('Дублирование списка ',listnew2)

# Использование обеих операций одновременно.
listnew3 = List7*2 + List8*3
print('Использование обеих операций одновременно.',listnew3)