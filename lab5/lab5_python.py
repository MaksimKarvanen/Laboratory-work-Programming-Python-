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


ex1("data.txt")
ex2("data.txt")