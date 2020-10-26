import math
print("Unesite sljedece podatke o jednakokrakom trouglu: ")
b = int(input("krak: "))
a = int(input("osnovica: "))

def rotacija_jednakokrakog_trougla_oko_visine_spustene_na_osnovicu(s, a):
    """ 
    rotacijom nastaje kupa
    ulazni podaci: krak b -> postaje izvodnica kupe s
                   osnovica a jednakokrakog trougla-> njena polovina postaje poluprecnik osnove kupe r
    racuna visinu trougla spustenu na osnovicu -> postaje visina kupe H
    returns povrsina i zapremina rotacionog tijela
    """
    r = a / 2
    pi = 3.14
    H = math.sqrt( s * s - r * r)
    povrsina = r * pi * (r + s)
    zapremina = (r * r * pi * H) / 3
    return povrsina, zapremina

print("Povrsina i zapremina rotacionog tijela iznose: ", rotacija_jednakokrakog_trougla_oko_visine_spustene_na_osnovicu(b, a))


