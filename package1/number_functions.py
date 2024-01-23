# obliczająca sumę cyfr w liczbie
def suma_cyfr(numer: int) -> int:
    suma = 0
    while numer > 0:
        suma += numer % 10  # (*)
        numer //= 10  # (**)
    return suma


# obliczająca silnię liczby
def silnia(number: int) -> int:
    silnia = 1
    for i in range(1, number+1):
        silnia = silnia * i
    return silnia
