import csv
import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

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
        file.write("\nЭто новая строка, добавленная в задании 5.")

def ex6(data):
    vowels = 'аеиоуыэюяaeiouy'
    with open(data, 'r') as file:
        text = file.read().lower()
        count = sum(1 for char in text if char in vowels)
        print(f"Количество гласных: {count}")

def ex7(data):
    with open(data, 'r') as file:
        for line in file:
            for word in line.split():
                print(word[0].upper() + word[1:], end=' ')

def ex8(newdata):
    with open(newdata, 'w') as file:
        for i in range(10):
            random_list = [random.randint(1, 100) for _ in range(10)]
            file.write(' '.join(map(str, random_list)) + '\n')
    print(f'Список с рандомными числами записан в {newdata}')

def ex9(data):
    with open(data, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            print(f"ID: {row['id']}, Name: {row['name']}, Department: {row['department']}, Salary: {row['salary']}, Start Date: {row['start_date']}, Active: {row['active']}")

def ex10(data):
    try:
        with open(data, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Файл не найден. Пожалуйста, проверьте имя файла и попробуйте снова.")

def ex11(data):
    with open(data, 'rb') as file:
        hex_content = file.read().hex()
        print(hex_content)

def ex12(data1, data2, newdata):
    with open(data1, 'r') as file1, open(data2, 'r') as file2:
        text1 = file1.read()
        text2 = file2.read()

    with open(newdata, 'w') as new_file:
        new_file.write(text1 + '\n' + text2)
        
def ex13(data, oldword, newword):
    with open(data, 'r') as file:
        text = file.read()

    newtext = text.replace(oldword, newword)

    with open(data, 'w') as file:
        file.write(newtext)

def ex14(data, newdata):
    with open(data, 'r') as file:
        lines = file.readlines()
        new_lines = []
        for line in lines:
            if (len(line.strip())):
                new_lines.append(line)
    with open(newdata, 'w') as file:
        file.writelines(new_lines)

def ex15(data, encrypted_data, decrypted_data):
    with open(data, 'r') as file:
        text = file.readlines()
    
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext = cipher.encrypt(''.join(text).encode('utf-8'))

    with open(encrypted_data, 'wb') as file:
        file.write(cipher.nonce)
        file.write(ciphertext)
    print(f"Файл зашифрован и сохранен в {encrypted_data}")

    with open(encrypted_data, 'rb') as file:
        nonce = file.read(16)
        ciphertext = file.read()

    with open(decrypted_data, 'w') as file:
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        decrypted_text = cipher.decrypt(ciphertext).decode('utf-8')
        file.write(decrypted_text)
    print(f"Файл расшифрован и сохранен в {decrypted_data}")
        

ex1("data.txt")
ex2("data.txt")
ex3("data.txt", "newfile.txt")
ex4("data.txt")
ex5("data.txt")
ex6("data.txt")
ex7("data.txt")
ex8("random_numbers.txt")
ex9("data.csv")
ex10("non_existent_file.txt")
ex11("test.bin")
ex12("data.txt", "data2.txt", "combined.txt")
ex13("data.txt", "и последняя", "уже не последняя")
ex14("data.txt", "cleaned_data.txt")
ex15("data.txt", "encrypted_data.bin", "decrypted_data.txt")