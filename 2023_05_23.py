"""
FUNKCJE KONTYNUACJA
"""

# Zakres lokalny

x = 10


def foo():
    x = 20
    print(x, "to jest z funkcji")


print("przed wywołaniem funkcji foo()")
print(x)

foo()
print(x)
print("po wywołaniem funkcji foo()")

print("INNY PRZYKŁAD")

full_name = "Sebastian Woźniak"

print(full_name)


def print_employee(name, surname):
    full_name = f"{name} {surname}"
    print(full_name)


print_employee("Jan", "Kowalski")
print(full_name)

# Funkcja może zwracać wiele wartośći
print("---Funkcja może zwracać wiele wartośći---")


def calculator(number1, number2):
    suma = number1 + number2
    diff = number1 - number2

    return suma, diff  # (15, 5)


result1 = calculator(10, 5)
print(result1)
print(result1[0])
print(result1[1])

# x, y, z = (1, 2, 3)

res1, res2 = calculator(100, 77)  # (177, 23)
print(res1)
print(res2)
print(f"suma: {res1}, roznica: {res2}")

# Możemy mieć wiele słów kluczowych return
print("---Wiele return---")


def validate_password(password):
    if len(password) < 8:
        return "Hasło musi być większe niż 8 znaków."

    if "$" not in password:
        return "Hasło musi zawierać znak $"

    return "Hasło jest poprawne."


print(validate_password("top_secret"))

print("---Funkcje w funkcji---")


def diff(n1, n2):
    print(f"odejmuje liczby n1 i n2, wynik to: {n1 - n2}")


def add(n1, n2):
    print(f"dodaje liczby n1 i n2, wynik to: {n1 + n2}")
    diff(n1, n2)


add(100, 50)

print("---Funkcje w parametrze---")


def hello_world():
    print("Hello world!")


def hello_user():
    name = input("Podaj imię: ")
    print(f"Hello {name}")


def call(function):
    function()


call(hello_world)
# call(hello_user)

print("OBIEKTOWOŚĆ")

"""
OBIEKTOWOŚĆ
"""

"""
KLASA:
- jest czymś w rodzaju "projektu" na podstawie którego tworzy się konkretne obiekty, które będą osobnymi bytami.

OBIEKT:
- przypomina rzeczywisty obiekt z otaczajągo nas świata
- posiada pechne cechyy, np (JEŚLI MÓWIMY O TELEFONIE KOMÓRKOWYM) - numer sim, numer tel, lista kontaktów, zainstalowane
aplikacje
- może wykonywac pewne czynnośc, np. (JEŚLI MÓWIMY O TELEFONIE KOMÓRKOWYM) - dzwonienie, odtwarzenie muzyki, wysyłanie
smsów
"""

print(type(100))
print(type("TEkst"))
print(type([1, 2]))

"""
1 (KLASA) do N (OBIEKTÓW) - JEDEN DO WIELU
TELEFON KOMÓRKOWY (KLASA) -> N OBIEKTÓW - CZYLI MOGĘ MIEĆ: MÓJ TELEFON KOMÓRKOWY, TELEFON MOJEJ ŻONY, TELEFON BRATA
"""

# Tworzenie klas i obiektów
print("---Tworzenie klas i obiektów---")


class MyClass:  # KLASA
    pass


first_obj = MyClass()  # OBIEKT KLASY MyClass
print(first_obj)
print(type(first_obj))

"Utwórzmu inną klasę"

"""
funkcja  -> osobne byty, nie muszę być zdefiniowane w KLASACH
metoda -> są one zdefiniowane w KLASACH
"""

"""
def info_function():
    print("To jest funkcja")
"""

print("---nowa klasa -> MyAnotherClass---")


class MyAnotherClass:

    def info(self):  # self - odwoływanie się do obiektu, na którym wywoływana jest metoda
        print(f"Inforamcja o obiekcie: {self}")


another_obj1 = MyAnotherClass()  # 1 obiekt / instancja
another_obj2 = MyAnotherClass()  # 2 obiekt / instancja
another_obj1.info()  # wywołujemy metodę o nazwie info(), która dostępna jest dla tego obiektu
another_obj2.info()  # wywołujemy metodę o nazwie info(), która dostępna jest dla tego obiektu

"""KONSTRUKTOR KLASY"""

print("---Konstruktor klasy---")

"""
Dzięki konstruktorowi możemy utworzyć obiekty z pewnymi atrybutami

Konstruktor umożliwia nam utowrzenie konkretnych atrybutów dla danego obiektu.

__init__ -> metoda konstruktora
"""


class MobilePhone:
    def __init__(self, brand, serial_number, owner):
        # składnia -> self.nazwa_atrybutu
        self.brand = brand  # atrybut brand
        self.serial_number = serial_number  # atrybut serail number
        self.owner = owner  # atrybut owen
        """
        Dlaczego używamy np.self.brand = brand
        1. self.brand odnosi się do atrybutu dla konkretnego obiektu
        2. brand odnosi się do wartości przekazywanej jako argument do metody __init__.
        """

    def description(self):
        print(f"Właścicielem telefonu marki {self.brand} jest {self.owner}")


# Wywołujemy obiekty tej klasy

mp = MobilePhone("ajfon", "0001", "seba")  # utowrzyłem nowy telefon z taki atrybutami
mp1 = MobilePhone(brand="samsung", serial_number="23455", owner="adam")  # drugi obiekt telefonu

print("1 telefon")
mp.description()
print(mp.brand)
print(mp.serial_number)
print(mp.owner)

print()

print("2 telefon")
mp1.description()
print(mp1.brand)
print(mp1.serial_number)
print(mp1.owner)

print("Klasa z atrybutami przypisanymi")


class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.company = "IKEA"
        self.projects = []

    def add_project(self, project_name):
        self.projects.append(project_name)


e1 = Employee("jan", "kowalski")  # 1 obiekt pracownika
e2 = Employee("adam", "nowak")  # 2 obiekt pracownika
print(f"Pracownik {e1.name} {e1.surname} pracuje w {e1.company} i jego projekty to: {e1.projects}")
print(f"Pracownik {e2.name} {e2.surname} pracuje w {e2.company} i jego projekty to: {e2.projects}")
print("Dodaje 2 projekty dla pracownika e1")
e1.add_project(project_name="projekt 1")
e1.add_project(project_name="projekt 2")

print()

print("Dodaje 1 projekt dla pracownika e2")
e2.add_project("project 10")

print()

print(f"Pracownik {e1.name} {e1.surname} pracuje w {e1.company} i jego projekty to: {e1.projects}")
print(f"Pracownik {e2.name} {e2.surname} pracuje w {e2.company} i jego projekty to: {e2.projects}")
