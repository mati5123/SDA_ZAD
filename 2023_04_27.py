# ============ TYP DANYCH: STRING ============
print("============ TYP DANYCH: STRING ============")

"""
Łańcuch znaków (string).
"""

print("To jest jakiś ciąg ##%3453")
print('To jest jakiś ciąg ##%3453')
print("""To tekst 
    teskt test 
    jest jakiś ciąg ##%3453""")

# docstring - dokumentowanie kodu, używamy wtedy potrójny apostrof

print('jakiś tekst "teks z cudzysłowiu" coś jeszcze')
print("jakiś tekst 'teks z cudzysłowiu' coś jeszcze")

print("\"Pan Tadeusz\" to film")

"""ŁĄCZENIE SEKWENCJI ZNAKÓW"""

name = "Jan"
surname = "Kowalski"
age = 30

# funkcja print może przyjmować kilka argumentów
print(name, surname, age)

# zmiana separatora z przerwy na znak _
print(name, surname, age, sep="_")

# \n -> jest przejście do nowej lini
print(name, surname, age, sep="\n")

# KONKATENACJA - łączenie ze sobą ciągów znaku
# dodanie do siebie łańcucuchów
full_name = name + surname
print(full_name)  # wada: doda nam bez odstępu

full_name2 = name + " " + surname
print(full_name2)

# Stara metoda, teraz już rzadko używana
text = "Moje imię: %s, nazwisko: %s, wiek: %s" % (name, surname, age)
print(text)

# metoda format() - często używana
format_text = "Imię: {}, Nazwisko: {}".format(name, surname)
print(format_text)

# f-string - jedynie prawilna i najlepsza metoda
f_string = f"Moje imię: {name}, nazwisko: {surname}"
print(f_string)

number = 5.234234234
some_txt = f"To jest liczba która ma tylko 3 liczby po przecinku {number:.3f}"
print(some_txt)

"""Podstawowe i przydatne funkcje na stringach"""

# len() -> zwraca długość łańcucha znaków (jego liczbę)
len_text = "Witajcie"
print(len(len_text))

# upper() -> funkcja która zwraca łańcuch znaków w wersji wielkich liter
upper_text = "Robert Lewandowski"
print(upper_text.upper())

# lower() -> funkcja zwracająca łańcuch znaków w wersji z małych liter
lower_text = "Robert Lewandowski"
print(lower_text.lower())

t = "Test Test"
print(t.upper().lower())

# replace() -> funkcja zamieniająca wystapienia określonego ciągu znaków w łańcuchu znaków na innych ciąg
text_replace = "Robert Lewandowski Lewandowski Lewandowski"
new_text_replace = text_replace.replace("Lewandowski", "Kubica")  # zamieni wszystkie wystąpienia
new_text_replace2 = text_replace.replace("Lewandowski", "Kubica", 2)  # zamieni tylko 2 pierwsze wystąpienia
print(new_text_replace)
print(new_text_replace2)

# split() - funkcja dzieląca lańcuch znaków na listę wg separatora
fruits = "jabłko, gruszka, śliwka"
fruits_list = fruits.split(",")
print(fruits_list)

# strip() - funkcja usuwająca białe znaki (spacje tabulatory) ALE tylko na początku i końcu łańcucha
form_text = "  Aleja Niepodległości        "
valid_form_text = form_text.strip()
print(valid_form_text)
print(f"Not valid text: {form_text} || Valid text: {valid_form_text}")

# print("Tekst" + 10) to nie zadziała - będzie błąd

"""RZUTOWANIEM - proces zamiana jednego typu na inny typ."""

print("Tekst " + str(10))  # "10"
print("X" * 100)

x_int = 50
x_as_str = str(x_int)
print(x_as_str)
print(type(x_int))
print(type(x_as_str))
print("----")
y_str = "100"
y_as_int = int(y_str)
print(type(y_str))
print(type(y_as_int))

city = "Warszawa"
# city_int = int(city) Błąd, nie można zmienić string na int, jeśli to nie jest liczba

population = "100.5"
# population_number = int(population) Błąd, nie zadziała bo 100.5 jest liczbą float
population_number = float(population)
print(population_number)
print(type(population_number))

"""INDEKSOWANIE"""

"""
- Rozpoczyna się od 0 dla pierwszego znaku w łańcuchu.
- Zwraca pojedyńczy znak
- Odbywa się za pomocą operatora nawiasów kwadratowych -> []
"""

print("---- INDEKSOWANIE ----")
super_text = "Ala ma kota, kot ma Ale"
print(super_text[0])  # A
print(super_text[3])  # znak spacji
print(super_text[11])  # ,
# print(super_text[24]) błąd IndexError -> bo nie ma tylu znaków!
print(super_text[-1])  # ostatni znak w łańcuchu
print(super_text[-5])  # a
# print(super_text[-100]) błąd IndexError -> bo nie ma tylu znaków!

print("---- SLICE (CIĘCIE) ----")
"""SLICE (CIĘCIA)"""

"""
- Pozwalają na pobieranie zawartości ciągów łańcucha
- Notacja składa się z dwóch indeksów oddzielonych dwukropkiem [x:y]
- Pierwszy indeks to początek, a drugi określa koniec fragmentu
- Jeśli pierwszy jest pominięty to cięcie zaczyna się od początku
- Jeśli drugi jest pominięty to cięcie kończy się na końcu łańcucha
- Cięcia zwracają fragment łańcucha
"""

slice_text = "Wlazł kotek na płotek i mruga."
# [0:5]
print(slice_text[0:5])  # Wlazł
print(slice_text[:5])  # Wlazł - prostrzy zapis
print(slice_text[3:7])
print(slice_text[6:24534])  # jeśli indeks wykracza poza długość, to python nie wywoła błędu, tylko zwróci do ostatniego
# indeksu
print(slice_text[6:])
print(slice_text[:])  # gdy nie ma początku i końca to zwróci cały teskst

# Dodatkowy parametr, STEP (krok)
print(slice_text[0:6:2])  # pobierze co drugi znak od indeksu 0 do 6 -> Wał
print(slice_text[::2])  # pobierze wszystko od początku do końca co drugi znak
print(slice_text[::-3])  # pobierze wszystko od końca do początku co trzeci znak od końca
print(slice_text[::-1])  # odwrócony łańcuch znaków
# palidnrom - fajnie to sprawdzić z slicem
kayak = "kajak"
print(f"Normalnie: {kayak} || Odwrócone: {kayak[::-1]}")

"""
PODSUMOWANIE:

text[:] > Cały łańcuch
text[start:stop] > Znaki od miejsca start do znaku o indeksie stop
text[start:] > Znaki od miejsca start do końca łańcuchu
text[:stop] > Znaki od początku łańcucha od znaku o indeksie stop
text[::n] > Co n-ty znak z częsci łańcucha począwszy od pierwszego
text[start:stop:n] > Co n-ty znak częście łańcucha od miejsca start do stop
text[::-1] > Odwrócony łańcuch
"""

"""
bb = 123123
yy = bb[0]
To nie zadziała bo liczby nie mają idndeksu.
"""

bb = str(123123)
yy = int(bb[0])
print(yy)
print(type(yy))

"""INKREMENTACJA (zwiększenie wartości zmiennej) oraz DEKREMENTACJA (zmniejsze wartości zmiennej)"""

i = 5
i += 1  # to samo co to: i = i + 1
print(i)

j = 5
j -= 1  # to samo co to: j = j - 1
print(j)

# ============ TYP DANYCH: BOOL ============
print("============ TYP DANYCH: BOOL ============")
"""
Typ logiczny, który może przyjąc jedną z dwóch wartości True (prawda) oraz False (fałsz)
"""

false = False
true = True

x = 5
y = 10

# Porównanie wartości
print(x == y)  # False
# Sprawdzenie czy x jest mniejsze niz y
print(x < y)  # True
# Sprawdzenie czy x jest większe niż y
print(x > y)  # False
# Sprawdzenie czy x jest różne od y
print(x != y)  # True

# Porównywanie stringów
print("Ala" == "ala")  # False
print("Ala" == "Ala")  # True

# ============ TYP DANYCH: NONE ============
print("============ TYP DANYCH: NONE ============")

x = None
print(x)
print(type(x))

# ============ TYP DANYCH: INPUT ============
print("============ TYP DANYCH: INPUT ============")

"""
Funkcja input służy do wczytywania danych wprowadzonych przez użytkownika z klawiatury. Funbkcja zwraca typ str.
"""

# test = input("Podaj swoj imię: ")
# age = input("Podaj swój wiek: ")
# print(f"Moje imię to: {test}, a wiek to: {age}")

number1 = int(input("Podaj pierwszą liczbę: "))
number2 = int(input("Podaj drugą liczbę: "))
add = number1 + number2
print(f"Suma: {add}")

# isdigit -> do sprawdzenia, w ramach zajęć
