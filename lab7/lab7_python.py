import random
import csv


#ex1
def even_num(n):
    for i in range(0, n, 2):
        yield i

print("Четные числа до n:", end=' ')
for num in even_num(10):
    print(num, end=' ')

#ex2
class FibonacciIterator:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

print("\nПервые 10 чисел Фибоначчи:")
fib = FibonacciIterator()
for _ in range(10):
    print(next(fib), end=' ')

#ex3
def read_file_line(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

print("\nФайл построчно:")
for line in read_file_line('test.txt'):
    print(line)

#ex4
def prime_numbers(n):
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i

print("\nПростые числа до n:", end=' ')
for num in prime_numbers(10):
    print(num, end=' ')

#ex5
def squares(n):
    for i in range(1, n + 1):
        yield i ** 2

print("\nКвадраты до n:", end=' ')
for num in squares(5):
    print(num, end=' ')

#ex6
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data

node = Node(1)
node.next = Node(2)
node.next.next = Node(3)

print("\nЭлементы связного списка:", end=' ')
iterator = LinkedListIterator(node)
for i in iterator:
    print(i, end= ' ')

#ex7
def multiples(num, n):
    return (i * num for i in range(1, n + 1))

print("\nПервые n (5) кратные числу 3:", end=' ')
for num in multiples(3, 5):
    print(num, end=' ')

#ex8
def factorials(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        yield fact

print("\nФакториал от 1 до n:", end=' ')
for num in factorials(5):
    print(num, end=' ')

#ex9
def substrings(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            yield s[i:j]

string = "абв"
print(f"\nПодстроки в строке {string}:", end=' ')
for s in substrings(string):
    print(s, end=' ')

#ex10
class NestedListIterator:
    def __init__(self, nested_list):
        self.stack = [iter(nested_list)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            try:
                item = next(self.stack[-1])
                if isinstance(item, list):
                    self.stack.append(iter(item))
                else:
                    return item
            except StopIteration:
                self.stack.pop()
        raise StopIteration

lst = [1, [2, 3], [4, [5, 6]]]
print("\nЭлементы вложенного списка:", end=' ')
iterator = NestedListIterator(lst)
for item in iterator:
    print(item, end=' ')

#ex11
def dice_rolls():
    while True:
        yield random.randint(1, 6)

dr = dice_rolls()
print("\nТри броска кубика:", end=' ')
for _ in range(3):
    print(next(dr), end=' ')

#ex12
def random_numbers(start, end):
    while True:
        yield random.randint(start, end)

print("\nТри случайных числа от 1 до 10:", end=' ')
rn = random_numbers(1, 10)
for _ in range(3):
    print(next(rn), end=' ')

#ex13
class DictKeysIterator:
    def __init__(self, d):
        self.d = d
        self.keys = list(d.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.keys):
            raise StopIteration
        key = self.keys[self.index]
        self.index += 1
        return key
    
d = {'a': 1, 'b': 2, 'c': 3}
iterator = DictKeysIterator(d)
print("\n Ключи словаря:", end=' ')
for key in iterator:
    print(key, end=' ')

#ex14
def cumulative_sum(lst):
    total = 0
    for num in lst:
        total += num
        yield total

print("\n Накопительная сумма:", end=' ')
for num in cumulative_sum([1, 2, 3, 4]):
    print(num, end=' --> ')

#ex15
def read_csv_lines(filename):
    with open(filename, 'r') as file:
        table = csv.reader(file)
        for row in table:
            yield row

print("\nФайл: test.csv")
for row in read_csv_lines('test.csv'):
    print(row)