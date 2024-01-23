# # f obliczająca liczbę wyrazów w napisie
def ile_wyzazow_w_napisie(napis: str) -> int:
    return len(napis.split(sep=None, maxsplit=-1))


# # f odwracająca kolejność wyrazów
def odwroc_kolejnosc(napis: str) -> list[str]:
    lista = napis.split(sep=None, maxsplit=-1)
    lista.sort(reverse=True)
    return lista


# # f usuwająca znaki białe w napisie
def usun_biale_znaki(napis: str) -> str:
    podzielony_napis = napis.split(sep=None, maxsplit=-1)
    napis_wynikowy: str = ''
    return napis_wynikowy.join(podzielony_napis)