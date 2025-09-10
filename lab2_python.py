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

    print(result)


ex1()
ex2()
ex3()
ex4()
ex5()