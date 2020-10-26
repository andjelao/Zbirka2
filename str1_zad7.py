import math
print("Unesite koordinate tacke A: ")
x1 = int(input("x: "))
y1 = int(input("y: "))
print("Unesite koordinate tacke B: ")
x2 = int(input("x: "))
y2 = int(input("y: "))
print("Unesite koordinate tacke C: ")
x3 = int(input("x: "))
y3 = int(input("y: "))

def povrsina_i_obim_trougla_preko_koordinata_tacaka(x1, y1, x2, y2, x3, y3):
    """
    ulazni podaci: koordinate x i y tri tacke trougla 
    racuna duzinu stranica pomocu formula za odredjivanje razdaljine izmedju dvije tacke
    returns povrsina i obim trougla odredjenog ovim tackama
    """
    povrsina = (abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))) / 2
    rastojanje_a_b = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    rastojanje_a_c = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    rastojanje_b_c = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    obim = rastojanje_a_b + rastojanje_a_c + rastojanje_b_c
    return povrsina, obim

print("Povrsina i obim trougla iznose: ", povrsina_i_obim_trougla_preko_koordinata_tacaka(x1, y1, x2, y2, x3, y3))


