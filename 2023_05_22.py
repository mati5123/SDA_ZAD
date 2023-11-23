"""
PĘTLA FOR - KONTYNUACJA
"""

# range
l = [1, 2, 3, 4, 5]
print(l)
print(list(range(1, 6)))

print("---range---")
for number in range(10, 101):
    print(number)

# enumerate
print("---enumerate---")

cars = ["opel", "bmw", "skoda"]
for car in enumerate(cars):
    print(car)

print("---enumerate z indeksami---")
for index, car in enumerate(cars, start=1):
    # print(f"Samochód {car} znajduję się pod indeksem {index}")
    print(f"{index}. {car}")

# Iterowanie po słowniku

print("---Iterowanie po słownik---")
products = {
    "mleko": 3.44,
    "chleb": 5.17,
    "jogurt": 1.99,
    "piwko": 6.99
}

print(products.items())

for product in products.items():
    print(product)

print(products.keys())

for product_name in products.keys():
    print(product_name)

print(products.values())

for product_price in products.values():
    print(product_price)

print("---jesz raz po items---")
for product, price in products.items():
    print(f"{product.capitalize()} kosztuje mnie {price} PLN.")

print("-----")

total = 0
print("Wchodzę do sklepu...")
for key, value in products.items():
    print(f"Do mojego koszyka dodałem produkt {key} za {value} PLN")
    total += value

print("Placę za produkty...")
print(f"Wydałem na zakupach: {total} PLN")

# zip
print("---zip---")

names = ["Mateusz", "Andrzej", "Kasia", "Monika"]
ages = [45, 30, 44, 32, 66]
surnames = ["kowalski", "nowak", "hyjek"]

print(list(zip(names, ages, surnames)))

for name, age in zip(names, ages):
    print(name, age)

print("odzipowanie")

l2 = [('Mateusz', 45, 'kowalski'), ('Andrzej', 30, 'nowak'), ('Kasia', 44, 'hyjek')]

names2 = []
age2 = []
surnames2 = []
for data in l2:
    names2.append(data[0])
    age2.append(data[1])
    surnames2.append(data[2])

print(names2)
print(age2)
print(surnames2)

print("tworzenie nowych list za pomocą pętli for")

phones = ["iphone", "nokia", "samsung", "xiaomi"]
phone_lengths = []
for phone in phones:
    phone_length = len(phone)
    if phone_length > 5:
        phone_lengths.append(phone_length)

print(phone_lengths)

"""
Tworzenie nowych list z wykorzystaniem podejścia comprehension
"""

print("---List comprehension---")

# Składnia

"""
new_list = []
for element in stara_lista:
    wyrażenie
    if waraunek:
"""

# new_list = [wyrażenie for element in stara_lista if warunek]


"""
phones = ["iphone", "nokia", "samsung", "xiaomi"]
phone_lengths2 = []
for phone in phones:
    phone_length = len(phone)
    phone_lengths.append(phone_length)
    if phone_length > 5:
        phone_lengths.append(phone_length)
"""

phone_lengths2 = [len(phone) for phone in phones if len(phone) > 5]
print(phone_lengths2)

# Inny przykład

nums = [1, 2, 4, 5, 6]
print(nums)
squares = [n ** 2 for n in nums]
print(squares)

"""
jak to wygląda z for
squares = []
for n in nums:
    squares.append(n ** 2)
"""

# Jeszcze inny przykład

fruits = ["apple", "banana", "cherry", "lime"]
print(fruits)
"""
if 'a' in fruit:
    dodaj dużymi literami
else:
    dodaj małymi literami
"""
new_fruits = [fruit.upper() if 'a' in fruit else fruit.lower() for fruit in fruits]
print(new_fruits)

""""
Z for:

new_fruits = []
for fruit in fruits:
    if 'a' in fruit:
        new_fruits.append(fruit.upper())
    else:
        new_fruits.append(fruit.lower())
"""

# Odnośnie słownika -> dict comprehension

# Składnie

# nowy_słownik = {klucz: wartość for element in sekwencja if warunek}

new_products = {"jabłko": 2.52, "banan": 3.04, "gruszka": 3.66}
print(new_products)

promotion_products = {key: value * 0.5 for key, value in new_products.items() if value * 0.5 > 1.5}
print(promotion_products)

"""
Z pętlą for
promotion_products = {}
for key, value in new_products.items():
    new_price = value * 0.5
    if new_price > 1.5:
        promotion_products[key] = new_price
"""

"""
FUNKCJA

- wydzielona część programu, wykonuje określone zadania
- używaliśmy print(), len(), input()
"""

"""
Korzyści:

- kod jest bardziej przejrzysty
- łatwiej modyfikować kod
- WIELOKROTNEGO UŻYCIA - unika się powtarzania tego samego kodu wiele razy
"""

print("---FUNKCJE---")


def hello():
    print("Hello Seba!")


hello()


def hello2(name):
    print(f"Witam {name}")


# my_name = input("Podaj imię: ")
# hello2(my_name)


def hello3(name):
    text = f"Witaj {name}"
    return text


# my_name3 = input("Podaj imię: ")
# # print(hello3(my_name3))
# h = hello3(my_name3)  # Witaj marek
# print(h)
# text = h + " " + " jakiś tekst"
# print(text)


def signature(name, surname, age):
    return f"Nazywam się {name} {surname} i mam {age} lat."


sig = signature("Sebastian", "Woźniak", 50)
print(sig)

sig2 = signature("Seba", 50, "Woźniak")  # trzeba mieć pod uwagą kolejność parametrów
print(sig2)

# Można używać nazw paramaterów aby uniknąć powyższego problemu

sig3 = signature(name="Jan", surname="Nowak", age=30)
print(sig3)


# Wartości domyślne

def create_phone_number(phone_number, prefix="+48"):
    return f"{prefix}{phone_number}"


print(create_phone_number(500100400))
print(create_phone_number(666999666, prefix="+55"))  # nadpisujesz domyślny parametr
print(create_phone_number(666999666, "+33"))  # też nadpisujesz parametr, ale nie musisz koniecznie używac jego nazwy

# ARGS

print("---args---")


def sum_number(*args):
    print(args)
    print(type(args))

    result = 0
    for number in args:
        result += number

    return result


suma = sum_number(5, 2)
suma1 = sum_number(5, 2, 5, 7, 3, 1, 2)
print(suma)
print(suma1)


def sum_number2(*numbers):
    result = 0
    for number in numbers:
        result += number

    return result


suma2 = sum_number2(10, 20, 30)
print(suma2)


def sum_number3(desc, *args):
    result = 0
    for number in args:
        result += number

    return f"Dla {desc}, suma liczb = {result}"


suma3 = sum_number3("liczby pierwsze", 1, 3, 5, 7, 11, 13)
print(suma3)

# KWARGS (dowolne argumenty, para klucz: wartosć)
print("--kwargs--")


def employee(**kwargs):
    desc = ""
    for key, value in kwargs.items():
        desc += f"{key}: {value} \n"

    return desc


e = employee(name="Seba", surname="wozniak", age=20)
print(e)
e1 = employee(name="jan", surnames="kowalskie", age=50, position="CEO", salary=50000)
print(e1)


# Można mieć args i kwargs razem

def homework(*args, **kwargs):
    result = sum(args)
    print(f"Suma liczb: {result}")

    print("CO znajduje się w kwargs?")
    print(kwargs)

    if "title" in kwargs:
        print(f"Tytuł pracy: {kwargs.get('title')}")

    if "author" in kwargs:
        print(f"Autor pracy: {kwargs.get('author')}")


homework(4, 1, 5, 5, 11, title="Dane statystyczne", author="seba")

numbeers = (4, 1, 5, 5, 11)
dane = {"title": "Dane statystyczne INNE", "author": "MAREK"}

homework(*numbeers, **dane)
