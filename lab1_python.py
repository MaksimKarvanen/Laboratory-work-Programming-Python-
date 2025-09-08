from datetime import datetime
import math
import random


def ex1():
    print("Hello, World!")

def ex2():
    name = input("Введите ваше имя: ")
    print(f'Привет, {name}!')

def ex3():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    sum_result = num1 + num2
    print(f"Сумма чисел: {sum_result}")

def ex4():
    cels = float(input("Введите температуру в градусах Цельсия: "))
    far = (cels * 9/5) + 32
    print(f'{cels} C = {far} F')

def ex5():
    result = datetime.now()
    print(f'Текущие дата и время: {result}')

def ex6():
    n = int(input("Число для таблицы умножения: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def ex7():
    radius = float(input("Радиус круга: "))
    area = math.pi * radius ** 2
    print(f"Площадь круга: {area:.2f}")

def ex8():
    a = input("Первая переменная: ")
    b = input("Вторая переменная: ")

    print(f"a = {a}, b = {b}")
    a, b = b, a
    print(f"a = {a}, b = {b}")

def ex9():
    number = int(input("Введите число: "))
    if number % 2 == 0:
        print("Число четное")
    else:
        print("Число нечетное")

def ex10():
    number = int(input("Введите число для вычисления его факториала: "))
    result = math.factorial(number)
    print(f'Факториал числа {number} равен {result}')

def ex11():
    weight = float(input("Вес: "))
    height = float(input("Рост: "))

    imt = weight / (height ** 2)
    print(f"Индекс массы тела: {imt}")

def ex12():
    text = input("Введите строку: ")
    reversed = text[::-1]
    print(reversed)

def ex13():
    number = float(input("Введите число: "))
    if number >= 0:
        result = math.sqrt(number)
        print(f"Квадратный корень из {number} = {result:.2f}")
    else:
        print("Ошибка (число отрицательное)")

def ex14():
    kilometers = float(input("Расстояние в километрах: "))
    miles = kilometers * 0.621371
    print(f"Расстояние в милях: {miles:.2f}")

def ex15():
    random_number = random.randint(1, 100)
    print(f"Случайное число от 1 до 100: {random_number}")


ex1()
ex2()
ex3()
ex4()
ex5()
ex6()
ex7()
ex8()
ex9()
ex10()
ex11()
ex12()
ex13()
ex14()
ex15()