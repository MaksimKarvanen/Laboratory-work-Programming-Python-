import math
from abc import ABC, abstractmethod


# ex1
class Rectangle:
    def __init__ (self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

# ex2    
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
    def display(self):
        print(f"Name: {self.name}\nRoll number: {self.roll_number}")

# ex3        
class BankAccount:
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостаточно средств")
    def get_balance(self):
        return self.balance

# ex4    
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Я не знаю что говорить"

class Dog(Animal):
    def speak(self):
        return "Гав"
    
class Cat(Animal):
    def speak(self):
        return "Мяу"

#ex5
class Shape:
    def __init__(self, name):
        self.name = name

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

# ex6
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        return f'Имя: {self.name}, Возраст: {self.age}'

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    def display(self):
        base_info = super().display()
        return f'{base_info}, Зар. плата: {self.salary}'

#ex7
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
    
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    
#ex8
class Car:
    wheels = 4
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display(self):
        return f"Марка: {self.make}, Модель: {self.model}, Количество колес: {Car.wheels}"

#ex9
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f"Книга '{book}' добавлена."
    
    def remove_book(self, book):
        self.books.remove(book)
        return f"Книга '{book}' удалена."
    
    def display(self):
        if not self.books:
            return "Книг нет."
        return "Книги в библиотеке:\n" + "\n".join(self.books)    

#ex10
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        return f"Координаты точки: X:{self.x}, Y:{self.y}"

#ex11
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.normal()

    def normal(self):
        self.hours += self.minutes // 60
        self.minutes = self.minutes % 60

    def __add__(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + total_minutes // 60
        return Time(total_hours, total_minutes % 60)
    
    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}"

#ex12
class A:
    def method_a(self):
        return "Метод A"

class B:
    def method_b(self):
        return "Метод B"
    
class C(A, B):
    def method_c(self):
        return "Метод C"
    
#ex13
class Shape2(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle2(Shape2):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape2):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side   

#ex14
class InstanceCounter:
    count = 0

    def __init__(self):
        InstanceCounter.count += 1
        self.instance_number = InstanceCounter.count

    @classmethod
    def get_instance_count(cls):
        return cls.count
    
    def __str__(self):
        return f"Экземпляр номер: {self.instance_number}"

#ex15
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        return f"Элемент '{item}' добавлен в очередь."
    
    def dequeue(self):
        if not self.is_empty():
            return f"Элемент '{self.items.pop(0)}' удален из очереди."
        return "Очередь пуста."
    
    def display(self):
        if self.is_empty():
            return "Очередь пуста."
        return "Элементы в очереди: " + ", ".join(self.items)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

rect = Rectangle(5, 3)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

stud = Student("Максим", 5)
stud.display()

account = BankAccount(12345, 1000)
account.deposit(500)
print(f"Баланс: {account.get_balance()}")
account.withdraw(200)
print(f"Баланс после снятия: {account.get_balance()}")
account.withdraw(2000)

dog = Dog("Собака")
cat = Cat("Кошка")
animal = Animal("Животное")
print(f"{animal.name} говорит: {animal.speak()}")
print(f"{dog.name} говорит: {dog.speak()}")
print(f"{cat.name} говорит: {cat.speak()}")

person = Person("Кирилл", 20)
employee = Employee("Максим", 21, 300000)
print(f'Person: {person.display()}')
print(f'Employee: {employee.display()}')

c1 = Complex(2, 3)
c2 = Complex(4, 5)
print(c1 + c2)

car1 = Car("Porche", "Tycan")
car2 = Car("Jaguar", "F-Pace")
print(car1.display())
print(car2.display())

library = Library()
print(library.add_book("Капитанская дочка"))
library.add_book("Грокаем алгоритмы")
print(library.display())
print(library.remove_book("Капитанская дочка"))
print(library.display())

point1 = Point(1, 2)
point2 = Point(4, 6)
print(point1)
print(point2)
print(f"Расстояние между точками: {point1.distance(point2)}")

time1 = Time(2, 45)
time2 = Time(1, 30)
print(f"Время 1: {time1}")
print(f"Время 2: {time2}")
print(f"Время 1 + Время2 = {time1 + time2}")

obj = C()
print(obj.method_a())
print(obj.method_b())
print(obj.method_c())

circle = Circle2(5)
square = Square(4)
print(f"Площадь круга: {circle.area():.2f}")
print(f"Периметр квадрата: {square.perimeter()}")

odj1 = InstanceCounter()
obj2 = InstanceCounter()
obj3 = InstanceCounter()
print(f"Всего экземпляров: {InstanceCounter.get_instance_count()}")
print(odj1)
print(obj2)
print(obj3)

queue = Queue()
print(queue.enqueue("1"))
print(queue.enqueue("241"))
print(queue.enqueue("33"))
print(queue.display())
print(queue.dequeue())
print(queue.display())
print(f"Размер очереди: {queue.size()}")

