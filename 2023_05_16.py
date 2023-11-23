"""INSTRUKCJE WARUNKOWE"""

# Operatory logiczne

a = True
b = False

# AND - zwraca True, jeśli oba wyrażenia są prawdziwe, a w przciwnym wyapdku False

print(a and b)  # False
print(a and a)  # True

# OR - zwraca True, jeśli co najmniej jedno w wyrażeń jest prawdziwe

print(a or b)  # True
print(b or b)  # False

# NOT
print(not a)  # False
print(not b)  # True

# Można łączyć warunki
print("łącznie warunków")
print(False or False or True)  # dam nam to True ponieważ co najmniej jedno or zwróci wartość True i jest prawdziwe
print(True and True and False)  # wynkiem będzie False ponieważ operator "and" zwróci TRue tylko wtedy gdy obie strony
# są True

print(True and True or False)
# True and (True or False) ---> True and True --> True

"""OPERATORY RELACJI"""

x = 10
y = 20
print("Operatory relacji")
print(x == y)  # sprawdzenie równości -> False
print(x != y)  # sprawdzenie nierówności -> True
print(x > y)  # większy -> False
print(x < y)  # mniejszy -> True
print(x >= y)  # większe lub równe -> False
print(x <= y)  # mniejsze lub równe -> True

"""INTRUCKJE WARUNKOWE"""
"""
Jest to sposób na wykonywanie różnych blokóœ kodu w zależności od spełniania określoinego warunku. Uzywamy słówka
kluczowego if.
"""

test = True

print("Instrukcje warunkowe")

# if test == True:
#     print("Tak to prawda")

if test:
    print("Tak to prawda")
else:
    print("Nie...")

# Elif

weight = 50

if weight == 50:
    print("Twoja waga jest ok")
elif weight > 50:
    print("ważysz za dużo")
else:
    print("Ważysz za mało")

# bloki elif mogą być powielane, czyli możemy mieć ich ile chcemy

age = 25

if age < 18:
    print("Jesteś niepełnoletni")
elif age >= 18 and age < 30:
    print("jesteś młodym dorosłym")
elif age >= 30 and age < 60:
    print("jestes dorosły")
elif age >= 60:
    print("jesteś osobą starszą")
else:
    print("niepoprawny wiek")

# skrócona wersja

if age < 18:
    print("Jesteś niepełnoletni")
elif 18 <= age < 30:  # age >= 18 and age < 30
    print("jesteś młodym dorosłym")
elif 30 <= age < 60:  # age >= 30 and age < 60
    print("jestes dorosły")
elif age >= 60:
    print("jesteś osobą starszą")
else:
    print("niepoprawny wiek")

# zagnieżdzanie warunków

x = 5
y = 10

if x > y:
    print("x większe od y")
else:
    if x < y:
        print("x mniejsze od y")
    else:
        print("x jest równe y")

# Rozwiązanie zadanka

"""
a = float(input("Podaj pierszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = float(input("Podaj trzecią liczbę: "))

if a >= b and a >= c:
    print(f"Największa liczba: {a}")
elif b >= a and b >= c:
    print(f"Największa liczba: {b}")
else:
    print(f"Największa liczba: {c}")

print(f"Majwiększa liczba z max() to: {max(1, 1, 1, 1)}")
"""

"""LISTA"""

"""
Przechowywanie elementów jest uporządkowane - chodzi o indeksy, czyli 0, 1, 2
Listy są dynamiczne - oznacz to żę mogą być modyfikowane, mozemy do niej dodawać lub usuwać elementy
Lista może być dowolnego typu danych
"""

# Używamy nawiasów kwadratowych oraz każdy nowy element musi byc odzdzielony przecinkami
print("LISTA")
my_list = [1, 2, 3, "four", 5.0, True, None, "test", [1, 2, 3]]
print(my_list)
print(type(my_list))

# Najcześciej wykorzystywane operacje na listach

# len() - możemy sprawdzić długość listy
print("---len---")
print(len(my_list))

print("---DODAWANIE---")
# append() - dodaje element na końcu listy
list_add = [1, 2, 4]
print("---append---")
list_add.append(3)
print(list_add)

# insert() - wstawia element w określonym miejscu na liście
# index - miejsce pod które zostanie wstawiony nowy element
# element - element, który ma być wstawiony na liste
print("---insert---")
list_add.insert(1, "x")
print(list_add)

# extend() - dodaje elementy z innej listy na koniec listy
print("---extend---")
list_add.extend([6, 7, 8])
print(list_add)

# operator +
print("---operator +---")
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
my_list3 = my_list1 + my_list2
print(my_list3)

print("---USUWANIE---")
list_remove = [1, 1, 1, 2, 3, 5, 6]
print(list_remove)

# remove() -> usuwa pierwsze wystąpienie elementu na liście
print("---remove---")
list_remove.remove(1)
print(list_remove)

# pop() -> usuwa element o określonym indeksie i zwraca jego wartość, jeśli nie podamy indeksu to usunie ostatani
print("---pop---")
element = list_remove.pop(4)
print(element)
print(list_remove)

# del - usuwa element o okreslonym indeksie z listy
print("---del---")
del list_remove[-1]
print(list_remove)

print("---DOSTĘP DO ELEMENTÓW NA LIŚCIE---")
cars = ["opel", "mercedes", "skoda", "bmw", "opel", "fiat", "peugeot"]
print(cars)

# operator indeksowania []
print("---operator indeksowania---")
print(cars[0])
print(cars[-1])
print(cars[2])

# operator wycinka (slice) [:]
print("---operator wycinka (slice) [:]---")
print(cars[0:1])
print(cars[-1:3:-1])
print(cars[3:])
print(cars[0::2])

# index() - zwraca indeks pierwszego wystapoenia elementu na liście
print("---index---")
print(cars.index("opel"))

# print(cars.index("honda")) -> jeśli element nie występuje na liście to będzie ValueError


# count() -> zwraca liczbę wystąpienie elementu na liście
print("---count---")
print(cars.count("opel"))

print("---MODYFIKACJA LISTY POPRZEZ ZAMIANĘ ELEMENTU---")
changed_list = [1, 2, 3, 4, 5, 6, 6]
print(changed_list)
changed_list[-1] = 7
# changed_list[100] = 7 wyjątek IndexError, ponieważ nie mam indeksu 100 na liście
print(changed_list)

print("---CZYSZCZENIE LIST---")
cleared_list = [1, 2, 4, 5]
print(cleared_list)
# clear() -> czyści całą liste
cleared_list.clear()
print(cleared_list)

print("---PRACA NA ZAGNIEŻDZONYCH LISTACH---")
l10 = [1, 2, [3, 4, [5, 6]]]
print(l10)
print(len(l10))
print("----")
print(l10[0])
print(l10[1])
print(l10[2])
print("----")
print(l10[2][0])
print(l10[2][1])
print(l10[2][2])
print("----")
print(l10[2][2][0])
print(l10[2][2][1])

print("---KOPIOWANIE LIST---")

# 1. Kopiowanie poprzez przypisanie
print("Kopiowanie poprzez przypisanie")
l1 = [1, 2, 3, 4]
l2 = l1
print(l1)
print(l2)
print(id(l1))
print(id(l2))

l2.append(100)  # trzyma referencje
print(l1)
print(l2)
"""
W tym przypadku l2 jest tylko odniesieniem do oryginalnej listy l1. Oznacza to, że każda zmiana wprowadzona w jednej
liście, będzie widoczna w drugiej.
Nie polecam tak robić, bo później można sie zdziwić ;)
"""

# 2. Płytkie kopiowanie
print("Płytkie kopiowanie")
l3 = [1, 2, 3, 4]
l4 = l3.copy()
# copy() -> tworzy nowy obiekt listy, ale kopiowanie jest wykonane bez przypisania referencji.
print(l3)
print(l4)
print(id(l3))
print(id(l4))

l4.append(100)
print(l3)
print(l4)

# Co gdy płytkie kopiowanie nie wystarcza?
print("Co gdy płytkie kopiowanie nie wystarcza?")
l5 = [1, 2, 3, 4, [5, 6]]
l6 = l5.copy()
print(l5)
print(l6)
print(id(l5))
print(id(l6))

print("Dodaje liczbę 7")
l6.append(7)
print(l5)
print(l6)

print("Dodaje liczbę 8 do zagnieżdzonej listy")
l6[4].append(8)
print(l5)
print(l6)

# 3. Głębokie kopiowanie
print("Głębokie kopiowanie")

import copy

l7 = [1, 2, 3, 4, [5, 6]]
l8 = copy.deepcopy(l7)
print(l7)
print(l8)
print(id(l7))
print(id(l8))

l8[4].append(7)
print(l7)
print(l8)
