"""
DZIEDZICZENIE

"""
import random

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def welcome(self):
#         print(f"My name is {self.name} and I am {self.age} years old.")
#
#     def run(self):
#         print(f"{self.name} is running")
#
#     def eat(self):
#         print(f"{self.name} is eating")
#
#     def speak(self):
#         print("Woof Woof")
#
#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def welcome(self):
#         print(f"My name is {self.name} and I am {self.age} years old.")
#
#     def run(self):
#         print(f"{self.name} is running")
#
#     def eat(self):
#         print(f"{self.name} is eating")
#
#     def speak(self):
#         print("Miauuuu")
#
#
# dog = Dog("Azor", 5)
# dog.welcome()
# dog.run()
# dog.eat()
# dog.speak()
#
# cat = Cat("Mruczek", 2)
# cat.welcome()
# cat.run()
# cat.eat()
# cat.speak()

"""
Wniosek:
- dużo powtarzalnego kodu
- kontekst który jest powtarzalny dla tych 2 typów Klas
"""

"""
Dziedziczenie:

- możliwość tworzenia hierarchi klas, gdzie mamy klasę nadrzędną/nadklasę i ona może dziedziczyć cechy i zachowania
po innej klasie (porzędną/podklasą)
"""


# Cat, Dog ---> Animal

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def welcome(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

    def run(self):
        print(f"{self.name} is running")

    def eat(self):
        print(f"{self.name} is eating")

    def speak(self):
        print("I am not speaking :(")


class Dog(Animal):
    def speak(self):
        print("Woof woof")

    def fun(self):
        print("to jest tylko metoda dla psa")


class Cat(Animal):
    def speak(self):
        print("Miauuuu")


dog = Dog("Azor", 7)
cat = Cat("Mruczek", 5)
dog.welcome()
dog.eat()
dog.run()
dog.speak()
dog.fun()

cat.welcome()
cat.eat()
cat.run()
cat.speak()


class Turtle(Animal):

    def diving(self):
        print(f"{self.name} is diving!")


print()
turtle = Turtle("Pędziwiatr", 99)
print(turtle.name)
print(turtle.age)
turtle.welcome()
turtle.run()
turtle.eat()
turtle.speak()
turtle.diving()

print("-----------------")


# Employee, Student --> Person

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print(f"Hello, my name is {self.name}")


class Employee(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)
        # self.name = name # dzięki super nie musisz robić tego
        # self.age = age # dzięki super nie musisz robić tego
        self.company = company

    def work(self):
        print(f"{self.name} pracuje w {self.company}")


class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        # self.name = name # dzięki super nie musisz robić tego
        # self.age = age # dzięki super nie musisz robić tego
        self.school = school

    def study(self):
        print(f"{self.name} studiuje w {self.school}")


em = Employee("Alicja", 25, "Biedronka")

em.hello()
em.work()

student = Student("Basia", 20, "Politechnika")

student.hello()
student.study()

"""
PRACA NA PLIKACH
"""

# w PYTHONIE możemy pracować na plikach poprzez zapis do pliku i odczyt z pliku

# składnia:

# open(nazwa_pliku, tryb)

"""
Poprzez open() istnieje pewna zasada:
1. otwieramy plik
2. pracujemy nad plikiem
3. zamykamy plik

Nie zamknięcie pliku może powodować problemy, więc staramy się o tym pamiętać ;)
Problemy jakie mogą wystąpić to:
- plik nie zostanie zamknięty i dane mogą pozostać w buforze i nie trafić na dysk. Czyli nie wszystkie informacje
zostaną zapisane
- może dojść do wycieków zasobu.
- jeśli ja nie zamknę, a za 30 sekund 'ktoś inny' będzie go otwierał może spowodować problemy z odczytem
"""

"""
Podstawowe tryby:
Tryby to możliwośći jakie są dostępne podczas pracy z plikiem. Jest ich o wiele więcej, ale poznamy te podstawowe.

r -> Odczyt
r+ -> Odczyt i zapis
w -> Zapis (bierzemy pod uwagę, że plik zostanie nadpisany)
a -> zapis, ale nie nadpiszę wartości w pliku, tylko doda na koniec
"""

# file_write = open("write.txt", "a")
# file_write.write("Nowy tekst 1\n")
# file_write.write("Nowy tekst 2\n")
# file_write.write("Nowy tekst 3\n")
# file_write.write("Nowy tekst 4\n")
# file_write.close()
# print("-----------ODCZYT Z PLIKU----------")
# file_read = open("write.txt", "r")
# all_text = file_read.read()
# file_read.close()
# print(all_text)


print("-----------ODCZYT Z PLIKU z PĘTLĄ----------")
file_read2 = open("write.txt", "r")

# "\n" -> enter
counter = 1
for line in file_read2:
    print(f"Linia {counter}: {line}")
    counter += 1

file_read2.close()

names = ["seba", "jan", "kasia", "janusz", "krzychu"]
file_names = open("file_names.txt", "w")
file_names.writelines(name + "\n" for name in names)
# for name in names: # to jest to co wyżej tylko z standardową pętlą for
#     file_names.write(name + \n)
file_names.close()

"""Lepsza wersja otwarcia i zamknięcia pliku"""

# konstrukcja with open() as ... (potocznie znana jako manager contextu - to dla Waszej uwagi)

# NIE MUSIMY SIĘ MARTWIĆ ŻEBY ZAMKNĄĆ PLIK


# with open("liczby.txt", "w") as file:
#     for i in range(1, 100):
#         file.write(f"{i}. {random.random()}\n")


counter = 1
with open("liczby.txt", "r") as file:
    for line in file:
        print(f"Liczba {counter}: {line}", end="")
        counter += 1


# Przykładowe rozwiązanie zad 2
def count_letters(text):
    letters = {}
    for letter in text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    return letters


print(count_letters("aAabcAd"))
