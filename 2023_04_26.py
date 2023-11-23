# ZMIENNE

"""
Zmienna - pojemnik na dane, można powiedzieć, że jest to też taka szufladka, w której COŚ przechowujemy
"""

date_of_birth = "2000-01-01"
print(date_of_birth)
print(id(date_of_birth))

"""
1. Nazwa zmiennej -> czyli date_of_birth
2. Znak przypisania -> '=' przypisanie wartości znajdującej się po prawej stronie do zmiennej która znajduję się po 
lewej stronie
3. Wartość -> czyli oczekiwany rezultat, w tym wypadku jest to data urodzenia
4. Miejsce w pamięcie (możesz to sprawdzić za pomocą funkcji wbudowanej if() )
"""

"""
Ważna koncepcja o nazewnictwie:
nazwy zmiennych, funkcje lub później klasy powinny sugerować to co przechowują, a więc jeśli chcesz umieścić w swojej
zmiennej datę urodzenia to nazwij ją date_of_birth, a nie date.
"""

"""Tutaj przykład z inną nazwą zmiennej -> data ślubu"""
some_variable = "2001-01-01"  # źle, nie wiadomo o co chodzi, osoba która czyta kod będzie musiała się domyślać
date = "2002-01-01"  # lepiej ale można do uszczegółowić, wiadomo już że chodzi o jakąś date ale brak kontekstu
date_of_marriage = "2003-01-01"  # super, jasno i klarownie mówi nam co przechuje, data ślubu

"""
Co jeszcze warto wiedzieć o zmiennych?

1. Nazwa zmiennej może się składać z: liter, cyfr, oraz znaków podkreślenia (_) (var123_321_vasd = "123")
2. Nazwa zmiennej nie może zawierać spacji (var 1234 var = "123123")
3. Nazwa zmiennej nie moze zaczynać się od cyfry (1name = "Seba" źle, _name = "Seba" dobrze)
4. Należy unikać słów, ktore są zarezerwowane dla Pythona (def, if, for, import, from, is, while, execpt, in ... itd)
5. Python rozróżnia wielkości liter (to jest ok: name = "Seba", NAME = "Seba")
"""

# PODSTAWOWE TYPY DANYCH

"""
1. Liczby całkowite (integers) - przechowujemy liczby całkowite, np. 1, 2, 3 itd. 
2. Liczby zmiennoprzecinkowe (floats) - przechowujemy wartości zmiennoprzecinkowe, np. 3.14, 2.0 itd. 
3. Łańcuchy znaków (strings) - przechowywanie ciągów znak,ow, np. "Hello", "Sebastian"
4. Logiczne (booleans) - to typ które służy do przechowywania wartości logicznych (True, False).
5. NoneType - typ niezidentyfikowany, często jest używany do zainicjowania zmiennej
"""

# print

# print() - służy do wyświetlania tekstu lub wartości zmiennych na ekranie

name = "Adam"
print(name)

# type

# type() -> służy do zwrócenia typu danych, jakie są przechowywane w danej zmiennej

type_name = type(name)
print(type_name)

number = 100
print(type(number))

# Przypisanie zmiennych liniowe


v1, v2 = 1, 2
print(v1)
print(v2)

# ============ TYP DANYCH: INT ============
print("============ TYP DANYCH: INT ============")
positive_number = 100
negative_number = -50
negative_number2 = 50
zero = 0
num1 = 30

print(positive_number)
print(negative_number)
print(zero)
print(num1)
print(type(negative_number))

sum1 = positive_number - negative_number2
sum2 = positive_number + negative_number2

print(sum1)
print(sum2)

sum3 = positive_number / num1
print(sum3)
print(type(positive_number))
print(type(num1))
print(type(sum3))

print("---")
sum4 = round(6 / 4)
print(sum4)
print(type(sum4))
print("---")

# ============ TYP DANYCH: FLOAT ============
print("============ TYP DANYCH: FLOAT ============")

x = 3.14
y = -0.5
z = 1.1

print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

a = 5.42344235675
b = 1.2466
c = a - b
print(c)

# round()
# służy do zaokrąglenia wartości zmiennoprzecinkowych do określonej liczy miejsc po przecinku lub najbliższej
# całkowitej

print(round(c))  # zawsze zaokrąglin do liczby całkowitej
print(round(c, 2))  # to nam zaokrągli do 2 miejsce po przecinku

"""PROSTE OBLICZENIA"""
print("PROSTE OBLICZENIA")
print(7 + 3)  # DODAWANIE - 10
print(7 - 3)  # ODEJMOWANIE - 4
print(7 * 3)  # MNOŻENIE - 21
print(7 ** 3)  # POTĘGOWANIE
print(7 / 3)  # DZIELENIE 2.333333...
print(7 // 3)  # DZIELENIE CAŁKOWITE - 2
print(7 % 3)  # MODULO (%) RESZTA Z DZIELENIA - 1
# Operator modulo służy do obliczania reszty z dzielenia dwóch liczb całkowitych

"""
Używam modulo w:
- przypadku 7 % 3, liczba 7 jest podzielna przez 3 dwa razy, co pozostawia resztę 1.
- przypadku 10 % 6, liczba 10 jest podzielna przez 6 tylko raz, co pozostawia resztę 4.
- przypadku 10 % 4, liczba 10 jest podzielna przez 4 dwa razy, co pozostawia resztę 2.
- przypadku 6 % 3, liczba 6 jest podzielna przez 3 bez reszty, co oznacza, że reszta z dzielenia wynosi 0.
"""

"""Wyrażenie modulo warto używać gdy chcemy sprawdzić """

"""Kolejność wykonywania działań jest taka sama jak w matematyce"""
result = 10 + 10 * 2 ** 3
print(result)

"""Możemy zmienić kolejność wykonywania działań, poprzez stosowanie nawiasów"""
result1 = ((10 + 10 * 2) / (1 + 3))
print(result1)

"Łączenie liczb całkowitych z liczbami zmiennoprzecinkowymi"

d = 5 + 5.5
print(d)
print(type(d))
"""
Jeśli chociaż jedna z liczb jest liczbą zmiennoprzecinkową to wynik jest przedstawiony jako liczba zmienoprzecinkowa
"""
