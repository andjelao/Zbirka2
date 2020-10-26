import math

print("Unesite sljedece podatke o pravouglom trouglu: ")
a = int(input("duzina manje katete: "))
b = int(input("duzina vece katete: "))

def rotacija_pravouglog_trougla_oko_manje_katete(H,r):
    """
    rotacijom pravouglog trougla oko manje katete a nastaje kupa
    ulazni podaci: manja kateta a -> postaje visina kupe H
                   veca kateta b -> postaje poluprecnik osnove kupe r
    racuna duzinu hipotenuze c pomocu Pitagorine teoreme- ona postaje izvodnica kupe s
    returns povrsinu i zapreminu kupe
    """
    s = math.sqrt(H * H + r * r)
    pi = 3.14
    povrsina = r * pi * (r + s)
    zapremina = (r * r * pi * H) / 3
    return povrsina, zapremina

print("Povrsina i zapremina rotacionog tijela iznose: ", rotacija_pravouglog_trougla_oko_manje_katete(a, b))


