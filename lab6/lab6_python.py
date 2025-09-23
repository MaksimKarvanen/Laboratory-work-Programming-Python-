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
    
# ex5


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
