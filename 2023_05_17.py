"""Instrukcja warunkowa z wykorzystaniem listy"""
print("Instrukcja warunkowa + lista")

"""zakupy = ["chleb", "masło", "jajka"]
print(zakupy)
product = input("Podaj produkt, który chcesz dodać do koszyka: ")
if product in zakupy:
    print(f"{product} znajduję się już w koszyku")
else:
    zakupy.append(product)
    print(zakupy)"""

"""Tworzenie listy z łańcucha znaków i z powrotem"""
print("Lista ze stringa")

# split() ->podział po białych znakach (on jest domyślny)
print("---split---")
text = "Tutaj jakiś tekst który może być wrzucony na bloga"
print(text.split())  # ['Tutaj', 'jakiś', 'tekst', 'który', 'może', 'być', 'wrzucony', 'na', 'bloga']

cities_str = "warszawa, poznan, krakow, lodz"
print(cities_str.split(","))  # ['warszawa', ' poznan', ' krakow', ' lodz']

# join() -> łączy elementy listy w łańcuchu znaków, odzielając je speratorem. Metoda ta przyjmuje m.in. liste.
print("---join---")
ale_ma_kota = ["Ala", "ma", "kota"]
ale_ma_kota_text = " ".join(ale_ma_kota)  # Ala ma kota
print(ale_ma_kota_text)

number = ["1", "2", "3", "4"]
print("-".join(number))

"""Inny sposób na tworzenie listy"""
print("Inny sposób na utworzenie list")

l = [1, 2, 3, 4]

# list() -> konwertuje, np ciąg znaków na listę
print("---list---")
person = "Robert Lewandowski"
person_to_list = list(person)
print(person_to_list)

# range() ->
print("---range---")
r1 = range(5)
print(list(r1))

# range(start=2, stop=10, step=2)
r2 = range(2, 10, 2)  # sekwencja licz parzystych od 2  do 8
print(list(r2))

"""Sortowanie list"""
print("Sortowanie list")

list_sort = [6, 1, 99, 35, 2, 5, 15, 2, 1, 5, 0, 10]
# sort() -> sortuje elementy na liście w miejscu. nie zwraca żadnej wartości. zmienia oryginalną listę
print("---metoda sort---")
list_sort.sort()
print(list_sort)

fruits = ["banan", "jabło", "kiwi", "pomarańcz", "mango"]
fruits.sort(key=len, reverse=True)
print(fruits)

# sorted() -> sortuje elementy na liście, zwraca posortowaną listę (gdy ją przypiszemy do nowej zmiennej).
# nie zmienia oryginalnej listy
print("---funkcja sorted---")
cars = ["opel", "skoda", "mercedes", "opel", "bmw", "fiat"]
cars_sorted = sorted(cars)
cars_sorted2 = sorted(cars, reverse=True)
cars_sorted3 = sorted(cars, key=len)
print(cars)
print(cars_sorted)
print(cars_sorted2)
print(cars_sorted3)

"""
KROTKA / TUPLE
Jest niemodyfikowalną, uporządkowaną strukturą wartości, której nie można zmieniać po utworzeniu.
Oznacza to, że po zdeklarowaniu krotki nie można dodawać, usuwać ani modyfikować elementów.
"""

# Krotkę tworzymy za pomocą nawiasów okrągłych -> ().
# Umieszczamy równiez wartości oddzielone przecinkami.
print("---KROTKA / TUPLE---")
my_tuple = (1, 2, 3, 2)
print(my_tuple)
print(type(my_tuple))

# Kolejność elementów w krotce jest ustalona podczas jej tworzenia i nie może zostać zmieniona.

# my_tuple[0] = 100 # będzie błąd TypeError, ponieważ nie mozna zamienić wartości krotki

"""Podstawowe funkcje krotki"""

# len() -> funkcja która zwraca liczbę elementów krotki
print("---len---")
print(len(my_tuple))

# index() -> funkcja która zwraca indeks pierwszego wystąpienia okreslonego elementu na krotce
print("---index---")
print(my_tuple.index(2))

# count() -> funkcja zwraca liczkę wystąpień okreslonego elementu na krotce
print("---count---")
print(my_tuple.count(2))

# Dostęp - porzez indeksowanie []
print("---dostęp---")
print(my_tuple[0])
print(my_tuple[-1])

# Rozpakowywanie krotki -
print("---Rozpakowywanie---")
my_tuple2 = (-55.1, 44.9)

x, y = my_tuple2
print(x)
print(y)

form = ("Sebastian", "Woźniak", "sebastian.wozniak@com.pl", 25)

name, surname, email, age = form

print(name)
print(surname)
print(email)
print(age)

"""
Różnica względem listy.

1. Modyfikowalność - krotki nie są modyfikowane, a listy są.
2. Rozmiar - Krotki są mniejsze od list.
3. Prędkość - Krotki są szybsze od list w przypadku odczytu elementów.
4. Zastosowanie -> Krotki stosowane do przechowywanie różnych danych.

"""

"""

x = input("podaj szerokosc X")
y = input("podaj szerokosc Y")

print(punkt)
"""

"""
SŁOWNIK / DICT / DICTIONARY
- umożliwia przechowywanie par klucz - wartość.
- Klucze muszą być unikalne (tzn. nie mogą się powielać)
- Wartości - mogą być dowolnego typu
- pary klucz wartość muszą być rozdzielone przecinkami
"""

# nawiasy klamrowe {}

fruits = {
    "apple": 3.5,
    "orange": 5,
    "banana": 2
}

print(fruits)
print(type(fruits))

# len() -> zwraca liczbę elementów w słowniku
print("---len---")
print(len(fruits))

# keys() -> zwraca listę kluczy ze słownika
print("---keys---")
print(fruits.keys())
print(type(fruits.keys()))

# values() - zwraca listę wartości ze słownika
print("---values---")
print(fruits.values())
print(type(fruits.values()))

# Dodanie nowej wartości do słownika
print("---dodanie---")
# słownik[key] = value
fruits["lime"] = 3.33
print(fruits)

# Aktualizacja wartości
print("---aktualizacja---")
fruits["banana"] = 100
print(fruits)

# Pobranie wartości ze słownka za pomocą klucza
print("---Pobranie---")
print(fruits["apple"])

# print(fruits["peach"]) -> KeyError, błąd który pojawia się gdy nie ma klucza w słowniku

# get() -> bezpieczne pobierania wartości z słownika za pomocą klucza
print("---get---")
print(fruits.get("peach"))
print(fruits.get("peach", 0))

# update() -> aktualizowanie słownika większą ilością danych
print("---update---")
exotic_fruits = {"lychee": 50, "durian": 999}
fruits.update(exotic_fruits)
print(fruits)

extra_fruits = {"apple": 8}
fruits.update(extra_fruits)
print(fruits)

# pop() -> usuwa element ze słownika na podstawie klucza
print("---pop---")
fruits.pop("durian")
print(fruits)

# fruits.pop("lyche") -> zgłoszony zostanie wyjątek KeyError
# można bezpieczniej

x = fruits.pop("lychee", "nie ma owoca do usunięcia")
print(x)
print(fruits)

"""Instrukcja warunkowa + słownik"""
print("---Instrukcja warunkowa + słownik---")

"""
fruit_to_remove = input("Podaj nazwę owoca do usunięcia: ")
if fruit_to_remove in fruits:
    print(f"Usuwam owoc o nazwie: {fruit_to_remove}")
    fruits.pop(fruit_to_remove)
    print(fruits)
else:
    print(f"Nie ma takiego owoca do usunięcia jak: {fruit_to_remove}")
"""

"""
ZBIÓR / SET
- Set zawiera unikalne wartości
- Przypomina słownik, ale taki z samymi kluczami
- Elementy nie są uporządkowane 
"""

# 1. sposób utowrzenia set / zbioru

my_set = set()
print(my_set)
print(type(my_set))

# 2. poprzez przypisanie w nawiasach klamrowych
# d = {1: 1, 2: 2} to jest słownik!!
my_set1 = {1, 2}
print(my_set1)
print(type(my_set1))

# Tworzenie zbiory gdy mamy wiele takich samych wartości
my_set2 = {1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 3, 3, 5, 4, 6, 5, 3, 2, 1}  # {1, 2, 3, 4, 5, 6}
print(my_set2)

my_set3 = {"J", "J", "K", "K", "D"}
print(my_set3)

# Dodawanie elementów do zioru
print("---dodwanie---")
my_set2.add(5)
my_set2.add(6)
my_set2.add(7)
print(my_set2)

# Usuwanie elementów do zbioru
print("---usuwanie---")
my_set2.remove(2)
print(my_set2)

# my_set2.remove(222) -> wyjątek KeyError, bo nie ma takiej liczby jak 222 na zbiorze

# Usuwanie elementów do zbioru bez wyjątku
print("---usuwanie bez wyjątku---")
my_set2.discard(222)
print(my_set2)

"""
my_set100 = {1, 1, 1, 4, 4, 4}
print(my_set100)
set_to_list = list(my_set100)
print(set_to_list)
print(set_to_list[0])
print(set_to_list[1])

l = [1, 1, 1, 1, 1, 1, 44, 5, 3, 3, 2]
print(l)
print(set(l))
"""
