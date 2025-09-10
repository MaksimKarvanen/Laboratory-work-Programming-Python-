import math


def ex1():
    result = 0
    n = int(input("Введите число N: "))
    for i in range(1, n + 1):
        result += i
    print(f"Сумма чисел от 1 до {n} равна {result}")

def ex2():
    year = int(input("Введите год: "))
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        flag = True
    else:
        flag = False

    if flag:
        print("Год високосный")
    else:
        print("Год не високосный")

def ex3():
    a, b, c = map(int, input("Введите 3 числа через пробел: ").split())
    print(f"Максимальное число - {max(a, b, c)}")

def ex4():
    print("Четные числа от 1 до 100")
    for i in range(1, 101):
        if i % 2 == 0:
            print(i, end=" ")

    print()

def ex5():
    vowels = "АЕЁИОУЫЭЮЯAEIOU"
    result = 0

    s = input("Введите строку: ")
    for el in s:
        if el.upper() in vowels:
            result += 1

    print(f"В строке {result} гласных")

def ex6():
    lim = int(input("Введите предел для последовательности: "))
    a, b = 0, 1
    while a <= lim:
        print(a, end=" ")
        a, b = b, a + b
    print()

def ex7():
    s = input("Введите строку: ").lower().replace(" ", "")
    if s == s[::-1]:
        print("Строка является палиндромом")
    else:
        print("Строка не является палиндромом")

def ex8():
    n = int(input("Введите N: "))
    for i in range(1, n + 1):
        print(f"Факториал {i}: {math.factorial(i)}")

def ex9():
    n = int(input("Число для таблицы умножения: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def ex10():
    n1 = float(input("Первое число: "))
    n2 = float(input("Второе число: "))
    op = input("Введите операцию (+, -, *, /): ")

    if op == "+":
        result = n1 + n2
    elif op == "-":
        result = n1 - n2
    elif op == "*":
        result = n1 * n2
    elif op == "/":
        if n2 != 0:
            result = n1 / n2
        else:
            result = "Ошибка: деление на ноль!"
    else:
        result = "Неверная операция"

    print(f"Результат: {result}")

def ex11():
    s = input("Введите строку: ")
    
    digits = 0
    letters = 0

    for el in s:
        if el.isdigit():
            digits += 1
        elif el.isalpha():
            letters += 1

    print(f"В строке {digits} цифр и {letters} символов")

def ex12():
    for i in range(1, 101):
        is_prime = True
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i, end=" ")

def ex13():
    n = input("Введите число: ")
    result = sum(int(digit) for digit in n if digit.isdigit())
    print(f"Сумма цифр числа: {result}")

def ex14():
    number = float(input("Введите число: "))
    result = 1 / number
    print(f"Обратное число: {result}")

def ex15():
    n_list = list(map(int, input("Введите числа через пробел: ").split()))
    print(n_list[::-1])


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


