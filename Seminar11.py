import matplotlib.pyplot as plt
from random import randint as rand

# Задача 1. Постройте график функции
# 𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.

def Exercice1():
    x = [x for x in range(-10, 11)]
    y = [5 * i**2 + 10 * i - 30 for i in x ]
    listX = []
    listY = []
    for i in range(len(y)):
        if y[i] < 0:
            listX.append(x[i])
            listY.append(y[i])  
    plt.plot(x, y)
    plt.plot(listX, listY)           
    plt.title("Line graph")   
    plt.ylabel('Y axis')   
    plt.xlabel('X axis')   
    plt.show()

# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список 
# подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.

def Exercice2():
    number_of_houses = [i for i in range(1, 16)]
    square_of_houses = [rand(100, 300) for i in range(len(number_of_houses))]
    prices_of_houses = [rand(3000000, 20000000) for i in range(len(number_of_houses))]
    required_price = 50000
    required_price_line = [required_price for i in range(len(number_of_houses))]
    prices_one_meter = [int(prices_of_houses[i]/square_of_houses[i]) for i in range(len(number_of_houses))]
    
    plt.bar(number_of_houses, prices_one_meter)
    plt.plot(number_of_houses, required_price_line, 'r')
    plt.title("Стоимость домов за кв. метр")   
    plt.ylabel('Стоимость')   
    plt.xlabel('№ дома') 
    plt.show()

    result_number_of_houses = []
    result_square_of_houses = []
    result_prices_of_houses = []
    result_prices_one_meter = []

    for i in range(len(number_of_houses)):
        if prices_one_meter[i] < required_price:
            result_number_of_houses.append(number_of_houses[i])
            result_square_of_houses.append(square_of_houses[i])
            result_prices_of_houses.append(prices_of_houses[i])
            result_prices_one_meter.append(prices_one_meter[i])
    
    for i in range(len(result_square_of_houses)-1):
        for j in range(len(result_square_of_houses)-i-1):
            if result_square_of_houses[j] > result_square_of_houses[j + 1]:
                result_square_of_houses[j], result_square_of_houses[j + 1] = result_square_of_houses[j + 1], result_square_of_houses[j]
                result_number_of_houses[j], result_number_of_houses[j + 1] = result_number_of_houses[j + 1], result_number_of_houses[j]
                result_prices_of_houses[j], result_prices_of_houses[j + 1] = result_prices_of_houses[j + 1], result_prices_of_houses[j]
                result_prices_one_meter[j], result_prices_one_meter[j + 1] = result_prices_one_meter[j + 1], result_prices_one_meter[j]

    data = open('D:/Python.HomeWork/HomeWork/HomeWork11/Houses.txt', 'w')
    for i in range(len(result_square_of_houses)):
        data.writelines(f'Number: {result_number_of_houses[i]} S = {result_square_of_houses[i]} Price: {result_prices_of_houses[i]} Price one meter: {result_prices_one_meter[i]}\n')   
    data.close