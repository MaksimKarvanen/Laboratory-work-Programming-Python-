import unittest, tempfile, os, re
from typing import List

#ex1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def defect_factorial(n):
    if n == 0:
        return 2
    else:
        return n * defect_factorial(n - 1)
    
class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(3), 6)

class TestDefectFactorial(unittest.TestCase):
    def test_defect_factorial(self):
        self.assertEqual(defect_factorial(5), 120)

#ex2
class Calculator:
    def __init__(self):
        self

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Нельзя делить на ноль")
        return a / b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

class defect_testCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_defect_add(self):
        self.assertEqual(self.calc.add(2, 3), 6)

#ex3
def password_checker(password):
    if len(password) < 8:
        return False, "Пароль должен быть не менее 8 символов"
    
    if not any(char.isdigit() for char in password):
        return False, "Пароль должен содержать хотя бы одну цифру"
    
    if not any(char.isupper() for char in password):
        return False, "Пароль должен содержать хотя бы одну заглавную букву"
    
    return True, "Нормальный пароль"

class TestPasswordChecker(unittest.TestCase):
    def test_short_password(self):
        result, message = password_checker("Abcde1")
        self.assertFalse(result)
        self.assertEqual(message, "Пароль должен быть не менее 8 символов")
    
    def test_no_digit(self):
        result, message = password_checker("Qwertyui")
        self.assertFalse(result)
        self.assertEqual(message, "Пароль должен содержать хотя бы одну цифру")
    
    def test_no_uppercase(self):
        result, message = password_checker("qwertyu1")
        self.assertFalse(result)
        self.assertEqual(message, "Пароль должен содержать хотя бы одну заглавную букву")
    
    def test_valid_password(self):
        result, message = password_checker("Qwertyu1123Qdlmdwq")
        self.assertTrue(result)
        self.assertEqual(message, "Нормальный пароль")

#ex4
class FileManager:
    def __init__(self, filename):
        self.filename = filename
    
    @staticmethod
    def read(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {filename} не найден")
    
    @staticmethod
    def write(filename, content):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    
    @staticmethod
    def append(filename, content):
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(content)
    
    @staticmethod
    def count_lines(filename):
        return len(FileManager.read(filename).splitlines())
    
    @staticmethod
    def count_words(filename):
        return len(FileManager.read(filename).split())

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test.txt")
        FileManager.write(self.test_file, "Line 1\nLine 2\nLine 3")
    
    def tearDown(self):
        for root, dirs, files in os.walk(self.temp_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.temp_dir)
    
    def test_read_write(self):
        content = FileManager.read(self.test_file)
        self.assertEqual(content, "Line 1\nLine 2\nLine 3")
        
        FileManager.write(self.test_file, "New content")
        self.assertEqual(FileManager.read(self.test_file), "New content")
    
    def test_append(self):
        FileManager.append(self.test_file, "\nLine 4")
        content = FileManager.read(self.test_file)
        self.assertIn("Line 4", content)
    
    def test_count_lines(self):
        self.assertEqual(FileManager.count_lines(self.test_file), 3)
    
    def test_count_words(self):
        self.assertEqual(FileManager.count_words(self.test_file), 6)
    
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            FileManager.read("nonexistent.txt")

#ex5
def sort_strings(strings: List[str]) -> List[str]:
    return sorted(strings)

class TestSortStrings(unittest.TestCase):
    def test_sort_strings(self):
        input_strings = ["banana", "apple", "cherry"]
        expected_output = ["apple", "banana", "cherry"]
        self.assertEqual(sort_strings(input_strings), expected_output)

#ex6
def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "").replace(",", "").replace(".", "")
    return s == s[::-1]

class TestIsPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("Яро в тиши творя"))
        self.assertFalse(is_palindrome("Привет"))

#ex7
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
    
    def test_enqueue_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
    
    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())
    
    def test_size(self):
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.size(), 1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)

#ex8
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

class TestGCD(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(101, 10), 1)
        self.assertEqual(gcd(-48, 18), 6)

#ex9
class GuessNumber:
    def __init__(self, secret_number, max_attempts = 5):
        self.secret_number = secret_number
        self.max_attempts = max_attempts
        self.attempts = 0
        self.game_over = False
    
    def guess(self, number):
        if self.game_over:
            return "Игра окончена"
        
        self.attempts += 1
        
        if number == self.secret_number:
            self.game_over = True
            return "Поздравляем! Вы угадали!"
        elif self.attempts >= self.max_attempts:
            self.game_over = True
            return f"Игра окончена. Загаданное число: {self.secret_number}"
        elif number < self.secret_number:
            return "Загаданное число больше"
        else:
            return "Загаданное число меньше"

class TestGuessNumber(unittest.TestCase):
    def test_guess_number(self):
        game = GuessNumber(50, 3)
        
        result = game.guess(50)
        self.assertEqual(result, "Поздравляем! Вы угадали!")
        self.assertTrue(game.game_over)
        
        game = GuessNumber(50, 2)
        game.guess(10) 
        game.guess(60)  
        result = game.guess(70)
        self.assertIn("Игра окончена", result)
        self.assertTrue(game.game_over)
        
        game = GuessNumber(50, 5)
        result = game.guess(30)
        self.assertEqual(result, "Загаданное число больше")
        
        result = game.guess(70)
        self.assertEqual(result, "Загаданное число меньше")

#ex10
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

class TestIsValidEmail(unittest.TestCase):
    def test_email_validation(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertTrue(is_valid_email("user.name@domain.co.uk"))
        self.assertTrue(is_valid_email("user+tag@example.org"))
        
        self.assertFalse(is_valid_email("invalid"))
        self.assertFalse(is_valid_email("invalid@"))
        self.assertFalse(is_valid_email("invalid.com"))
        self.assertFalse(is_valid_email("@domain.com"))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)