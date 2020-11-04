import math
x = int(input("Unesite vrijednost x: "))

def funkcija(x):
    """
    ulazni parametar: broj x
    vraca vrijednost izracunatu preko odgovarajuce funkcije u zavisnosti od vrijednosti x
    """
    if x <= -7:
        return -2 * x + 7 / 2
    elif x < 1:
        return ( x * x - 3 * x + 5) / (x * x + 2) 
    elif x <= 8:
        return math.sqrt(x * x + 2 * x + 2) + math.sqrt(abs((3 * x) / 2 - 4 / 7))
    else: 
        return abs(3 / (x * x) - 11 * x)

print(funkcija(x))
