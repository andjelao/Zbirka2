import math

print("Unesite sljedece podatke o pravouglom trouglu: ")
a = int(input("duzina manje katete: "))
b = int(input("duzina vece katete: "))

def rotacija_pravouglog_trougla_oko_hipotenuze(s2, s1):
    """
    rotacijom nastaju dvije kupe- veca kupa k1 i manja kupa k2
    ulazni podaci: manja kateta a -> postaje s2 - izvodnica k2
                   veca kateta b -> postaje s1 - izvodnica k1
    racuna duzinu hipotenuze trougla c pomocu Pitagorine teoreme-> postaje zbir visina k1 i k2
    kombinacijom dvije formule za povrsinu pravouglog trougla racuna visinu trougla hc -> postaje poluprecnik zajednicke osnove obje kupe
    primjenom Pitagorine teoreme na katete i hc racuna duzinu visina H1 i H2 kupa k1 i k2
    povrsina rotacionog tijela -> zbir omotaca M1 i M2 kupa k1 i k2
    zapremina rotacionog tijela -> zbir zapremina V1 i V2 kupa k1 i k2
    returns povrsina i zapremina rotacionog tijela
    """
    c = math.sqrt(s2 * s2 + s1 * s1)
    povrsina_trougla= (s2 * s1) / 2
    hc = (2 * povrsina_trougla) / c
    H1 = math.sqrt(s1 * s1 - hc * hc)
    H2 = math.sqrt(s2 * s2 - hc * hc)
    pi= 3.14
    povrsina = hc * pi * (s1 + s2)
    zapremina = (hc * hc * pi * (H1 + H2)) / 3
    return povrsina, zapremina

print("Povrsina i zapremina rotacionog trougla iznose: ", rotacija_pravouglog_trougla_oko_hipotenuze(a, b))



