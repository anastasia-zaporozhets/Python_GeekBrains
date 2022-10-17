# Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from math import factorial as fc

def create_range_factorials(n): return [fc(i) for i in range(1, n + 1)]

def ask_number(): return int(input('Введите значение N: '))

def main():
    n = ask_number()
    numbers = create_range_factorials(n)
    print(*numbers)