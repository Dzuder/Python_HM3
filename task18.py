# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
#  Последняя строка содержит число X

import random
N = abs(int(input("Введите количество чисел в массиве: ")))
A = random.sample(range(1, 100), N)
X = int(input("Введите число, которое нужно сраввнить со списком чисел: "))
near_numb = abs(X - A[0])
for i in range(1, N):
    check_numb = abs(X - A[i])
    if check_numb < near_numb:
        near_numb = check_numb
        count = i
print(A)
print(f"{A[count]} самое близкое число в списке А к числу {X}")