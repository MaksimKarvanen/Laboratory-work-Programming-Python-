import time

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
def ex1_func():
    time.sleep(1)

#ex9
def html(tag="div", attrs=None):
    attrs = attrs or {}
    attr_str = " ".join(f'{k}="{v}"' for k, v in attrs.items())
    def deco(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if not isinstance(res, str):
                return res
            if attr_str:
                return f"<{tag} {attr_str}>{res}</{tag}>"
            else:
                return f"<{tag}>{res}</{tag}>"
        return wrapper
    return deco




ex1_func()


