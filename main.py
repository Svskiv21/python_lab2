from resources import *
from package1 import *

# testing functions from resources.py
tab_rows = [2, 3, 4, 5]
tab_elems = [1, None, None, 3]
chocolate_bar = [[tab_elems[i] for _ in range(tab_rows[i])] for i in range(len(tab_rows))]

# zad 1
result1 = srednia_mediana([0, 1, 2, 3])
print(result1)

# zad 2
tuple1 = (3, 4, 1, 6, 2)
sorted_list = sortowanko(tuple1)
print(sorted_list)

# zad 3
counter_none = ulepszone_szukanie_none(chocolate_bar)
print("Liczba pustych pól w tablicy:", counter_none)

# zad 5
# testing string_functions

napis = 'kajak ślimak kamil'
print(string_functions.usun_biale_znaki(napis))
print(string_functions.ile_wyzazow_w_napisie(napis))
print(string_functions.odwroc_kolejnosc(napis))

# testing number_functions
print(number_functions.suma_cyfr(1234))
print(number_functions.silnia(23))