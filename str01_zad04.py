import math
print("Unesite sljedece podatke o jednakokrakom trouglu: ")
b = int(input("krak: "))
a = int(input("osnovica: "))

def rotacija_jednakokrakog_trougla_oko_osnovice(s, a):
    """
    rotacijom nastaju dvije kupe k1 i k2
    ulazni parametri : krak b -> postaje izvodnica s obje kupe 
                       osnovica a -> njena polovina postaje visina H obje kupe
    racuna visinu trougla spustenu na osnovicu -> postaje poluprecnik r zajednicke osnove kupa
    povrsina = povrsina omotaca k1 + povrsina omotaca k2
    zapremina = zapremina k1 + zapremina k2
    returns povrsina i zapremina rotacionog tijela
    """
    pi = 3.14
    H = a / 2
    r = math.sqrt(s * s - H * H)
    povrsina = 2 * r * pi * s
    zapremina = (2 * (r * r * pi * H)) / 3
    return povrsina, zapremina

print("Povrsina i zapremina rotacionog tijela iznose: ",rotacija_jednakokrakog_trougla_oko_osnovice(b, a))
