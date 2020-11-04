import math
print("Unesite koordinate tacke A: ")
a1 = int(input("x: "))
a2 = int(input("y: "))
print("Unesite koordinate tacke B: ")
b1 = int(input("x: "))
b2 = int(input("y: "))
print("Unesite koordinate tacke C: ")
c1 = int(input("x: "))
c2 = int(input("y: "))

def da_li_postoji_trougao(x1, y1, x2, y2, x3, y3):
    """
    ulazni parametri: x i y koordinate tacaka A, B, i C
    provjerava da li trougao odredjenim ovim tackama postoji pomocu formule za povrsinu trougla preko koordinata tacaka
    stampa odgovor "Postoji" ili "Ne postoji"
    """
    povrsina = (abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))) / 2
    if povrsina == 0:
        print("Ne postoji")
    else: 
        print("Postoji")

da_li_postoji_trougao(a1, a2, b1, b2, c1, c2)
