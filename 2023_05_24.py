"""
OBIEKTOWOŚĆ KONTYNUACJA
"""

# Dekoratory
print("---Dekoratory---")

# @nazwa_dekoratora
"""
def nazwa_dekoratora():
    print("nazwa dekoratora")


@nazwa_dekoratora
def testowa():
    print("jestem funkcją")
"""

"3 podstawowe dekoratory, które używane sa w klasach"


class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def full_name(self):  # To jest normalna metoda, z której będziemy korzystac jeśli utworzymy sobie obiekt Student
        print(f"{self.name} {self.surname}")

    """
    Dekorator @staticmethod
    - używamy do definiowania statycznych metoda, które nie są związane z instancją obiektu i mogą być wywoływane
    bez cech dla tej klasy
    - jeśli definiujesz dekorator staticmethod to tracisz możliwość do atrybutów (chechy) danej klasy
    - nazwa jest obowiązkowa (musi się nazywać staticmethod)
    - po co używać? na przykłąd jeśli chcesz żęby Twoja metoda wykonywała jakieś operacje nie związane z atrybutami
    """

    @staticmethod
    def hello():
        print(f"Jestem statyczą metodą i nie muszę mieć dostępu do atrybutów klasy.")

    """
    Dekorator @classmethod
    - tworzone są w celu przeprowadzenia operacji na poziomie klasy, a nie na poziomie poszczególnych instancji 
    (obiektów) klasy
    - dostępu do informacji dotyczących klasy
    """

    @classmethod
    def class_method(cls):  # cls to skrót od class
        print(f"Jestem metodą na tej klasie i dostaję się do full_name {cls}")

    @classmethod
    def increase_age(cls, student):
        student.age += 1

    """
    @property
    """

    @property
    def full_name_property(self):
        return f"{self.name} {self.surname}"


# Wywołanie metody klasy
print("---wywołanie metody klasy---")
Student.class_method()

s = Student("tomek", "nowak", 50)
s1 = Student("adam", "nowak", 21)
s.hello()
s1.hello()

# Wywołanie metody klasy increase_age na konkretnym studencie
print("Przed zwiększeniem wieku")
print(s.age)
Student.increase_age(s)
print("Po zwiększeniu wieku")
print(s.age)

# Wywołanie metody full_name_property
print("---Wywołanie metody full_name_property--")
print(s1.age)
"""
różnica jest taka, że nie muszę robić s1.full_name_property(), ponieważ ta metoda została potraktowana jako 
kolejny atrybut funkcji
"""
print(s1.full_name_property)

# KOncepcja atrybutów publiczny i prywatnych
print("---KOncepcja atrybutów publiczny i prywatnych---")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("seba", 50)
p2 = Person("jan", 20)
print(p1.name)
print(p2.name)

new_value = "adam"

print(p1.name)

# @property -> to będzie też dekorator, który będzie pozwalał nam na dostęp do atrybutu

"""
GETTER I SETTER

GETTER -> czyli metoda odczytu
SETTER -> czyli metoda zapisu


Np w Javie robi się tak, getNazwaAtrybut, setNazwaAtrybutu (ale tego nie musicie pamiętać)
"""


class PrivatePerson:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property  # to jest traktowane jako getter - czyli metoda odczytu
    def name(self):
        return self.__name

    @name.setter  # to jest traktowane jako setter. używając tego mamy kontrole w poprawnośći przypisywanych wartości
    def name(self, new_name):
        # self.__name = new_name
        if type(new_name) != str:
            print(f"Nowe imię ({new_name}) nie jest wartością typu string! Nie mogę przypisać nowego imienia!")
        else:
            self.__name = new_name

    def __calculate_birth_year(self):  # METODA PRYWATNA
        current_year = 2023
        birth_year = current_year - self.__age
        return birth_year

    @property  # property jako przykład na użycie metody rywatnej WEWNĄTRZ KLASY
    def birth(self):
        return self.__calculate_birth_year()


pp = PrivatePerson("Karolina", 25)
# przed dodaniem gettera
# print(pp.__name) # nie mogę się dostać bezpośrednio do atrybutu name poprzez __name

# po dodaniu gettera
print(pp.name)

# pp.name = "tomek" # nie mogę nadpisać atrybutu, jeśli nie mam metody odczytu (settera)

# po dodaniu settera

pp.name = "agnieszka"
print(pp.name)

# bez kontroli
pp.name = 123
print(pp.name)

#  metoda prywatna
print(pp.birth)

"""
HERMETYZACJA
W Pythonie odnosi się do techniki ukrywania atrybutów i metod wewnątrz klasy, aby ograniczyć bezpośredni dostęp do nich
spoza klasy. Można powiedzieć, że oznacza to iż atrybuty i metody mogą być dostępne tylko wewnątrz klasy lub poprzez
specjalne metody, które kontrolują dostęp do nich (GETTERY, SETTERY)
"""

"""
METODY MAGICZNE W PYTHONIE :-)
Zwane inaczej jako Dunder Methods

Są to specjalne metody, które nadają obiektom dodatkowe "moce".
Te metody mają specjalne nazwy i zaczynają się i kończą dwoma podkreślnikami, np. __metoda__().

Dlaczego są magiczne?
- automatycznie wywoływane przez Python w przypadku jakiegoś zdarzenia (i taka jest ich najważniejsza różnica, pomiędzy
zwykłymi metodami, które tworzymy w klasach)
- pozwalają kontrolować zachowanie obiektów w odpowiedzi na określone operacje lub zdarzenia.
"""

print("---Magic methods---")


# __str__() -> wywoływana jest gdy obiekt konwertowany jest na łańcuch znaków za pomocą funkcji str()

# __str__() != str() to nie jest to samo, ale współpracuje ze sobą

class AnotherPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name}, age: {self.age}"


ap = AnotherPerson("John", 25)
# gdybyśmy nie mieli metody magicznej __str__ to będzie <__main__.AnotherPerson object at 0x7f77ee6b6160>
print(str(ap))  # wyświetli: Person: John, age: 25


# __repr__() -> zwraca repprezentacjie obiektu w postaci łańcuach, która jest bardziej technicza. działa z repr()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


point = Point(5, 5)
# gdybyśmy nie miel repr to wtedy <__main__.Point object at 0x7f8fa8629250>
print(repr(point))


# __eq__() -> wywoływana gdy używamy operatora == (porównanie) do porównania dwóch obiektów. Zwraca wartość logiczną
# i wskazuje czy obiekty są sobie równe

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height


rect1 = Rectangle(4, 5)
rect2 = Rectangle(4, 5)
rect3 = Rectangle(3, 6)

print(rect1 == rect2)
print(rect1 == rect3)

# Interakcja między obiektami

print("--interakcja--")


class Car:
    def __init__(self, brand):
        self.brand = brand


class Driver:
    def __init__(self, name):
        self.name = name

    def drive(self, car):
        print(f"{self.name} śmiga sobie autem marki {car.brand}")


driver = Driver("Ania")

car = Car(brand="Ferrari")

driver.drive(car)

"""
informations = [{"name": "Seba", "age": 50}, {"name": "Adam", "age": 20}, {"name": "Miłosz", "age": 40}]

for information in informations:
    for key, value in information.items():
        print(key, value)
"""

"""
IMPORTY
"""

# 1 sposób importowania

import random

random_number = random.randint(1, 100)
print(random_number)

# 2 możemy importować wybrane funckje z bilblioteki

from random import randint, choice

random_number2 = randint(100, 1000)
print(random_number2)

my_list = ["opel", "bmw", "honda", "ferrafi"]
random_element = choice(my_list)
print(random_element)

# 3 ALIAS.

from random import randint as moja_super_nowa_nazwa_funkcji

random_numer3 = moja_super_nowa_nazwa_funkcji(99, 45345)
print(random_numer3)
