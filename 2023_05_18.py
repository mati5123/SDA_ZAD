"""SŁOWNIK ZAGNIEŻDŻANIE"""

student = {
    "name": "JOhn",
    "age": 20,
    "grades": {
        "math": 6,
        "history": 4
    },
    "address": {
        "street": "sezamkowa",
        "city": "warszawa",
        "other": {
            "coś innego": 11
        }
    }
}

"""SET - KONTYNUACJA"""

my_set1 = {1, 2}
# udpate() -> dodanie wiecej elementów do zbioru
print("---update---")
print(my_set1)
my_set1.update([1, 2, 3, 4, 5])
print(my_set1)

# Przecięcie zbiorów
print("---przecięcie---")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

intersection = set1.intersection(set2)
print(intersection)

# Suma zbiorów
print("---suma---")
union = set1.union(set2)
print(union)

# Różnica zbiorów
print("---różnica---")
difference = set1.difference(set2)
print(difference)
difference2 = set2.difference(set1)
print(difference2)

# Symetryczna różnica zbiorów
print("---Symetryczna różnica---")
symetric = set1.symmetric_difference(set2)
print(symetric)

print("---MUTOWALNOŚĆ---")
"""
W pythonie typy danych mogą być:
- MUTOWALNE (Mutable) -> Mogę być zmieniane po utworzeniu przez dodawanie, usuwanie, modyfikacja elementów.
    1. list
    2. set
    3. dict (słownik)
- NIEMUTOWALNE (Immutable) -> Nie mogą być zmieniane po utworzeniu.
    1. int
    2. flaot
    3. string
    4. tuple
"""
# Mam zmienną number = 5 -> tworzony jest nowy obiekt int z wartością 5, zmienna number wskazuje na ten obiekt
number = 5
print(id(number))
# Tutaj mam inkrementacje (czyli zwiększam sobie wartość o 10)
# Python wykonuje działanie:
# - tworzy się nowy obiekt int z wartością 15, a więc zmienna number wskazuje teraz na ten nowy obiekt
number += 10
# Stary obiekt (czyli number = 5) nie jest już potrzebny więc jest usuwany z pamięci
print(id(number))
print(number)
# PODSUMOWAUJĄC: Ta 5 ona nie mogłą zostać zmieniona, ponieważ jest niemutowalna, została ona zastąpiona NOWYM obiektem

# Przykład listy

lst = [1, 2, 3]

print(id(lst))
print(lst)
lst.remove(3)
print(id(lst))
print(lst)
# Podsumowanie:
# W przypadku listy zmienia się wartość obiektu I TO TYLE.
# Lista lst nie musi zostać zastąpiona nową, ponieważ jest mutowalna
# Główna przyczyna/zaleta jest taka, że chodzi o wydajność (więc jeśli mamy duże struktury danych, to nie jest to
# optymalne żeby tworzyć nowy obiekt, ponieważ mogą być spadki wydajności)

# Przykład string

# Przypisuje sobie do zmiennej hello napis Hello i to wskazuje mi na obiekt w pamięci
hello = "Hello "
print(id(hello))
# Dodając do hello nowy ciąg znaków, tworzy mio się nowy łańcuch, który wskazuje na nowy obiekt
hello += "world"
print(id(hello))
print(hello)

# hello[0] = "Z" TypeError, nie da rady

# PODSUMOWUJĄC: NIE MOŻNA ZMIENIAĆ ŁAŃCUCHA ZNAKÓW BEZPOŚREDNIO

# Tuple
"""t = (1, 2, 3)
t.add(3)
t.remove(3)"""

"""
Exceptions / Wyjątki

Sa to specjalne obiekty, które reprezentują sytuacje wyjątkowe. W momencie wystąpienia przerywają program, ale 
umożliwiają na zareagowanie poprzez obsługę błędu. 
"""

"""
Python ma wiele wbudowanych wyjątków m.in.:

1. TypeError - zgłaszany kiedy nie można obsłużyć operacji, na przykład przy próbnie dodania liczby do napisu.
2. ValueError - zgłaszany gdy funkcja otrzymuje argument przy niepoprawnej wartośći, np konwersja tekstu na liczbę.
3. ZeroDivisionError - zgłaszany, gdy próbujesz dzielić przez 0
4. NameError - zgłaszany gdy jest próba odwołania się do niezidentyfikowanej zmiennej
5. AttributeError - zgłaszany gdy, próbujesz się odwołać do nieistniejącego atrybutu
6. IndexError - zgłszany jest gdy próbujesz się dostać do elementu listy, który znajduję się poza zakresem
7. KeyError - zgłaszany, gdy klucz nie istnieje w słowniku
8. FileNotFoundError - zglaszany, przy próbie otwarcia pliku, który nie istnieje

"""

number = 10
text = "text"
l = [1, 2, 3]
d = {"key1": "val1"}
# result = number + text -> TypeError
# text_2 = int(text) -> ValueError
# result = 10 / 0 -> ZeroDivisionError
# print(variable) -> NameError
# text.length -> AttributeError
# element = l[3] -> IndexError
# element = d["key2"] -> KeyError
# file = open("sciezka/moj_plik.txt") -> FileNotFoundError

try:
    print("przed dzieleniem")
    x = 1 / 0
    print("po dzieleniu")
except ZeroDivisionError:
    print("nie działa")

"""
PĘTLI WHILE
Pozwala na wykonywanie określonych instrukcji WIELE RAZY, dopóki warunek jest SPEŁNIONY
"""
print("---PĘTLA WHILE---")
# Składnia:
# while warunek:
#    # instrukcje

print("Początek pętli while...")
y = 0
while y < 5:
    print(f"Wartość mojego y={y}")
    y += 1
print("Koniec pętli while..")

"""
Kod wewnątrz bloku while będzie wykonywany tak długo jak długo będzie spełniony warunek.
"""

"""
while y > 1:
    print("Działam...")

Pętla while może prowadzić do nieskończonej pętli, jeśli warunek jest zawsze spełniony i nie ma żadnej zmiany w warunku
wewnątrz pętli.
"""

"""Instrukcje sterujące w pętli while"""

# Break -> możemy wyjść natychmiast z pętli while
print("---Break---")

print("Początek pętli while z break...")
z = 1
while True:
    print(f"Działam już {z} razy")
    z += 1
    if z > 150:
        break
print("Koniec pętli while z break...")

# Continue -> powduje to natychmiastowe przerwanie bieżącego obiegu i przejście do następnego
print("---Continue---")

print("Początek pętli while z Continue...")
a = 0
while a < 5:
    a += 1
    if a == 3:
        continue
    print(a)
print("Koniec pętli while z Continue...")

"""
ZADANIE:
Napisz program, który będzie dodawać nowych pracowników do LISTY. 
Niech program działa w pętli while., aby można było dodawać nowych pracowników cały czas. 
Napisz menu do programu, które będzie zawierało opcję:
1. Wyświetl wszystkich pracowników
2. Dodaj nowego pracownika
3. Wyjście z programu
"""

# Rozwiązanie zadania:
"""
employees = []

while True:
    print("Menu")
    print("1. Wyświetl wszystkich pracowników")
    print("2. Dodaj nowego pracownika")
    print("3. Wyjście z programu")

    choice = input("Wybierz opcje: ")

    if choice == "1":
        print(f"Pracownicy: {employees}")
    elif choice == "2":
        name = input("Podaj imię pracownika: ")
        employees.append(name)
        print(f"Pracownik {name} został dodany do listy.")
    elif choice == "3":
        print("Program został zakończony.")
        break
    else:
        print("Nieprawidłowa opcja. Wybierz ponownie.")
"""

"""PĘTLA FOR"""
# Iteracja

# Czy jest takie iterowanie?
# Oznacza przechodzenie przez elementy, np listy, krotki jeden po drugim i wykonanie pewnej operacji na każdym z tych
# elementów.


# Składanie pętli for:

"""
for zmienna in sekwencja:
    instrukcje do wykonania w każdej iteracji
"""
print("---pętlafor--")
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

students = ["seba", "adam", "michał"]

for student in students:
    print(student)

text = "Python"

for letter in text:
    print(letter)
