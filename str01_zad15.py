import math
x = int(input("Unesite vrijednost x: "))

def funkcija(x): 
    """
    ulazni parametar: broj x
    returns vrijednost izracunatu preko odgovarajuce funkcije u zavisnosti od vrijednosti x
    """
    if x <= 0:
        return -2 * x ** 2 + 7 / 2
    else: 
        return math.sin(2 * x + 5)
print(funkcija(x))
