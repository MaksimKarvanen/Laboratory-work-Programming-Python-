import math
import ex7, ex10, ex14

def ex1(n):
    return n * n

def ex2(n):
    if n == 1:
        return True
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def ex3(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

def ex4(l):
    return max(l) if l else None

def ex5(s):
    upper = 0
    lower = 0

    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return upper, lower

def ex6(l):
    return list(set(l))

def calculator_ex7():
    number1 = float(input("Первое число: "))
    number2 = float(input("Второе число: "))
    operation = input("Введите операцию (+, -, *, /): ")

    if operation == '+':
        return ex7.summation(number1, number2)
    elif operation == '-':
        return ex7.subtraction(number1, number2)
    elif operation == '*':  
        return ex7.multiplication(number1, number2)
    elif operation == '/':
        return ex7.division(number1, number2)
    else:
        return "Ошибка: неверная операция!"

def ex8(*args):
    return sum(args)

def ex9(s):
    s = s.lower().replace(" ", "")
    if s == s[::-1]:
        return True
    else:
        return False
    
def converter_ex10():
    print("1. Цельсий в Фаренгейт")
    print("2. Фаренгейт в Цельсий")
    choice = input("Выберите конвертацию (1 или 2): ")
    if choice == '1':
        cels = float(input("Введите температуру в градусах Цельсия: "))
        far = ex10.cel_to_fah(cels)
        print(f'{cels} C = {far} F')
    elif choice == '2':
        far = float(input("Введите температуру в градусах Фаренгейта: "))
        cels = ex10.far_to_cel(far)
        print(f'{far} F = {cels} C')
    else:
        print("Неверный выбор")
    
def ex11(n):
    if n <= 1:
        return n
    else:
        return ex11(n - 1) + ex11(n - 2)
    
def ex12(l):
    return sorted(l, key=lambda x: x[1])
    
def ex13(s):
    words = s.lower().split()
    frequency = {}
    for word in words:
        word = word.strip('.,!?;"\'()[]{}')
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    return frequency

def area_ex14():
    print("1. Площадь круга")
    print("2. Площадь квадрата")
    print("3. Площадь прямоугольника")
    choice = input("Выберите фигуру (1, 2 или 3): ")
    if choice == '1':
        radius = float(input("Введите радиус круга: "))
        area = ex14.circle_area(radius)
        print(f"Площадь круга: {area:.2f}")
    elif choice == '2':
        side = float(input("Введите сторону квадрата: "))
        area = ex14.square_area(side)
        print(f"Площадь квадрата: {area:.2f}")
    elif choice == '3':
        length = float(input("Введите длину прямоугольника: "))
        width = float(input("Введите ширину прямоугольника: "))
        area = ex14.rectangle_area(length, width)
        print(f"Площадь прямоугольника: {area:.2f}")

def ex15(s):
    return s[::-1]

def tic_tac_toe(field):
    for row in field:
        if row[0] == row[1] == row[2] and row[0] != '-':
            return f"{row[0]} win"
    for col in range(3):
        if field[0][col] == field[1][col] == field[2][col] and field[0][col] != '-':
            return f"{field[0][col]} win"
    if field[0][0] == field[1][1] == field[2][2] and field[0][0] != '-':
        return f"{field[0][0]} win"
    if field[0][2] == field[1][1] == field[2][0] and field[0][2] != '-':
        return f"{field[0][2]} win"
    for row in field:
        if '-' in row:
            return "Game not finished"
    return "Draw"


print(ex1(5))          
print(ex2(29))         
print(ex3(5))          
print(ex4([3, 1, 4, 1, 5, 9])) 
print(ex5("Hello World!"))
print(ex6([1, 2, 2, 3, 4, 4, 5]))
print(calculator_ex7())
print(ex8(1, 2, 3, 4, 5))
print(ex9("A man a plan a canal Panama"))
converter_ex10()
print(ex11(6))
print(ex12([(1, 'one'), (2, 'two'), (3, 'three'), (4, 'apple')]))
print(ex13("Hello world! Hello everyone."))
area_ex14()
print(ex15("Hello, World!"))

data = """0 - 0
x x x
0 0 -"""
field = [line.split() for line in data.split('\n')]
print(tic_tac_toe(field))