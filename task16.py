# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#   В последующих  строках записаны N целых чисел Ai.
#  Последняя строка содержит число X


import random
N = abs(int(input("Введите количество чисел в массиве: ")))
A = random.sample(range(1, 100), N)
X = int(input("Введите число, которое нужно найти в списке: "))
count = 0
for i in range(N):
    if A[i] == X:
        count += 1
print(A)        
print(f"Число {X} в списке А встречается {count} раз.")