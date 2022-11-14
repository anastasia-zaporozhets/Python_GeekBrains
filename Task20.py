# Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.

from random import randint as RI

numbers = [RI(0, 9) for _ in range(15)]
print(numbers)

query = list(map(int, input('Поиск')))
print(query)

for i in range(len(numbers)-3):
    if numbers[i:i+3] == query:
        print('Да')
        break
else:
    print('Нет')    