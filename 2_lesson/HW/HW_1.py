# 1. На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх
#  одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть.

n = int(input())
count1 = count0 = 0

for i in range(n):
    coin = int(input())
    if coin:
        count1 += 1
    else:
        count0 += 1

if count1 > count0:
    print(count0)
else:
    print(count1)