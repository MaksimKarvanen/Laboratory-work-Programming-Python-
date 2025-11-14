import time, functools, os, sqlite3
from contextlib import contextmanager
from typing import Dict, Type

#ex1
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция выполнена за {end_time - start_time} секунд")
        return result
    return wrapper

@timer
def first_function():
    time.sleep(1)

#ex2
def type_check(expected_types: Dict[int, Type]):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i, (arg, expected_type) in enumerate(zip(args, expected_types.values())):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Аргумент {i} должен быть типа {expected_type}, получен {type(arg)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check({0: str, 1: int})
def greet(name: str, age: int) -> str:
    return f"Привет, {name}! Тебе {age} лет."

#ex3
def cache(func):
    cached_results = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cached_results:
            cached_results[key] = func(*args, **kwargs)
        return cached_results[key]
    return wrapper

@cache
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

#ex4
class TimerContext:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        print(f"Блок кода выполнен за {self.end_time - self.start_time:.4f} секунд")

#ex5
class SuppressExceptions:
    def __init__(self, exceptions: tuple):
        self.exceptions = exceptions
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type and issubclass(exc_type, self.exceptions):
            print(f"Подавлено исключение: {exc_type.__name__}: {exc_val}")
            return True
        return False
    
#ex6
def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Функция {func.__name__} вызвана {wrapper.call_count} раз")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@count_calls
def say_hello():
    return "Привет!"

#ex7
def retry_on_exception(max_attempts: int = 3, delay: float = 1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Попытка {attempt + 1} не удалась: {e}. Повтор через {delay} сек...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry_on_exception(max_attempts=3, delay=0.5)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Случайная ошибка!")
    return "Успех!"

#ex8
class FileManager:
    def __init__(self, filename: str, mode: str = 'r'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

#ex9
def html(tag: str = "div", attrs: Dict[str, str] = None):
    attrs = attrs or {}
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, str):
                return result
            
            attr_str = " ".join(f'{k}="{v}"' for k, v in attrs.items())
            if attr_str:
                return f"<{tag} {attr_str}>{result}</{tag}>"
            else:
                return f"<{tag}>{result}</{tag}>"
        return wrapper
    return decorator

@html("div", {"class": "container", "id": "main"})
def get_content():
    return "Это содержимое страницы"

#ex10
class ChangeDirectory:
    def __init__(self, new_path: str):
        self.new_path = new_path
        self.old_path = None
    
    def __enter__(self):
        self.old_path = os.getcwd()
        os.chdir(self.new_path)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.old_path)

#ex11
def delay(seconds: float):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@delay(2)
def delayed_function():
    return "Эта функция была задержана на 2 секунды"

#ex12
class DatabaseConnection:
    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self.connection = None
    
    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

#ex13
def log_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами:")
        print(f"Позиционные: {args}")
        print(f"Именованные: {kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"Функция {func.__name__} вернула: {result}")
        return result
    return wrapper

@log_function
def multiply(a: int, b: int) -> int:
    return a * b

#ex14
class TransactionManager:
    def __init__(self, connection):
        self.connection = connection
    
    def __enter__(self):
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.connection.commit()
            print("Транзакция завершена успешно")
        else:
            self.connection.rollback()
            print(f"Транзакция откачена из-за ошибки: {exc_val}")

#ex15
def uppercase_output(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

@uppercase_output
def get_message() -> str:
    return "это сообщение будет в верхнем регистре"



first_function()

print(greet("Анна", 25))

print(f"fibonacci(10) = {fibonacci(10)}")

with TimerContext():
    time.sleep(0.5)

with SuppressExceptions((ValueError, ZeroDivisionError)):
    raise ValueError("Это исключение будет подавлено!")

say_hello()
say_hello()

result = unreliable_function()
print(f"Результат: {result}")

print(get_content())

print(delayed_function())

multiply(5, 3)

print(get_message())


