def ex1(data):
    with open(data, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

def ex2(data):
    with open(data, 'r') as file:
        lines = file.readlines()
        length = sum(1 for line in lines)
        words = sum(len(line.split()) for line in lines)
        symbols = sum(len(line) for line in lines)
        print(f"Строк: {length}, Слов: {words}, Символов: {symbols}")

def ex3(data, newfile):
    with open(data, 'r') as data_file:
        text = data_file.read()
    with open(newfile, 'w') as new_file:
        new_file.write(text)
    print("Копирование завершено!")

def ex4(data):
    with open(data, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            print(f"{i}: {line.strip()}")
        
def ex5(data):
    with open(data, 'a') as file:
        file.write("\nЭто новая седьмая строка, добавленная в задании 5.")

def ex6(data):
    vowels = 'аеиоуыэюяaeiouy'
    with open(data, 'r') as file:
        text = file.read().lower()
        count = sum(1 for char in text if char in vowels)
        print(f"Количество гласных: {count}")

def ex7():
    pass

def ex8():
    pass

def ex9():
    pass

def ex10():
    pass

def ex11():
    pass

def ex12():
    pass

def ex13():
    pass

def ex14():
    pass

def ex15():
    pass


ex1("data.txt")
ex2("data.txt")
ex3("data.txt", "newfile.txt")
ex4("data.txt")
ex5("data.txt")
ex6("data.txt")