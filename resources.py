import numpy as np

Vector = list


def srednia_mediana(lista: Vector) -> list:
    srednia = np.average(lista)
    mediana = np.median(lista)
    return [srednia, mediana]


def sortowanko(krotka: tuple) -> list[int]:
    lista_wynikowa = []
    for i in krotka:
        lista_wynikowa.append(i)
    lista_wynikowa.sort()
    return lista_wynikowa


def ulepszone_szukanie_none(arr_2d) -> int:
    counter = sum(row.count(None) for row in arr_2d)
    return counter
