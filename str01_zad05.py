print("Unesite sljedece podatke o pravouglom trapezu: ")
a = int(input("veca osnovica: "))
b = int(input("manja osnovica: "))
c = int(input("manji krak: "))
d = int(input("veci krak: "))

def rotacija_pravouglog_trapeza_oko_vece_osnovice(a, Hv, r, s):
    """
    rotacijom nastaju valjak i kupa
    ulazni parametri: veca osnovica a -> njen dio (a-b) postaje visina kupe Hk
                      manja osnovica b -> postaje visina i ivica valjka Hv
                      manji krak c -> postaje poluprecnik r osnove valjka i kupe
                      veci krak d -> ivica kupe s
    povrsina rotacionog tijela = jedna baza valjka + omotac valjka + omotac kupe
    zapremina rotacionog tijela = zapremina valjka + zapremina kupe
    returns povrsina i zapremina rotacionog tijela
    """
    pi = 3.14
    povrsina =  r * pi * (r + 2 * Hv + s)
    Hk = a - b
    zapremina = r * r * pi * (Hv + Hk / 3)
    return povrsina, zapremina

print(rotacija_pravouglog_trapeza_oko_vece_osnovice(a, b, c, d))

