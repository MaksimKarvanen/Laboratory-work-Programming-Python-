import math, random, datetime, re, collections, statistics


#ex1
def quadratic(a, b, c):
    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"x1 = {x1:.2f}, x2 = {x2:.2f}"
    elif discriminant == 0:
        x = -b / (2 * a)
        return f"x = {x:.2f}"
    else:
        return "Корней нет"
    
#ex2
def rand_password(n):
    password = []
    for _ in range(n):
        password.append(str(random.randint(0, 9)))

    return "".join(password) 

#ex3
def date():
    today = datetime.date.today()
    delta = datetime.timedelta(days = 7)
    date = today + delta

    return date

#ex4
def emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails

#ex5
def groups(text):
    words = re.findall(r'\b\w+\b', text.lower())

    grouped_words = collections.defaultdict(list)
    for word in words:
        grouped_words[len(word)].append(word)
    
    return dict(grouped_words)

#ex6
def find_with_pattern(pattern, text):
    coincidences = re.findall(pattern, text)
    return coincidences

#ex7
def random_float(minimum, maximum, count):
    return [random.uniform(minimum, maximum) for _ in range(count)]

#ex8
def unique_by_key(peoples, key):
    if key not in peoples[0]:
        return "Ключ не найден"
    else:
        sorted_list = sorted(peoples, key=lambda x: x[key])
        result = [collections.OrderedDict(item) for item in sorted_list]

    for item in result:
        print(item)

#ex9
def timezones():
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    print("Время по гринвичу: ", utc_now.strftime("%Y-%m-%d %H:%M:%S"))

    moscow_tz = datetime.timezone(datetime.timedelta(hours=3)) 
    moscow_time = utc_now.astimezone(moscow_tz)
    print("Время в Москве: ", moscow_time.strftime("%Y-%m-%d %H:%M:%S"))

#ex10
def median(numbers):
    return statistics.median(numbers)

print(quadratic(2, 4, -3))
print(rand_password(8))
print(date())
print(
    emails(
        "Уважаемые коллеги, для согласования итогового отчета прошу направить ваши комментарии не позднее 18:00 пятницы." \
        "Основные документы уже разосланы с корпоративной почты project.support@mx-service.com." \
        "Дополнительные вопросы можно задать лично мне: ivanov.ia@domain.co.uk." \
        "Копию письма, пожалуйста, всегда направляйте на billing-department@domain.co.uk."
    )
)
print(groups("Он быстро нашёл огромный дом."))
text = "Молоко стоило $200, а сыр стоил $400"
pattern = r'стоил'
print(find_with_pattern(pattern, text))
print(random_float(0, 2, 5))
peoples = [
    {'name': 'Иван', 'age': 25},
    {'name': 'Мария', 'age': 19},
    {'name': 'Петр', 'age': 32},
    {'name': 'Анна', 'age': 25}
]
key = 'name'
unique_by_key(peoples, key)
timezones()
data = [10, 2, 8, 4, 6]
print(median(data))
