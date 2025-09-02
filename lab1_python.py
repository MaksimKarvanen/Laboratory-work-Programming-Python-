from datetime import datetime
from math import factorial

def ex2():
    name = input("Введите ваше имя: ")
    print(f'Привет, {name}!')

def ex5():
    result = datetime.now()
    print(f'Текущие дата и время: {result}')

def ex10(number):
    result = factorial(number)
    print(f'Факториал числа {number} равен {result}')




ex2()
ex5()
ex10(int(input("Введите число для вычисления его факториала: ")))