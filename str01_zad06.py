import math
print("Unesite sljedece brojeve: ")
x = int(input("x: "))
y = int(input("y: "))
alfa = int(input("alfa: "))
beta = int(input("beta: "))
a = int(input("a: "))
b = int(input("b: "))

def izrazi(x, y, alfa, beta, a, b):
    """
    ulazni parametri: brojevi x, y, alfa, beta, a, b koji se uvrstavaju u izraze
    returns vrijednost pet izraza
    """
    prvi = (x ** 3) / 3 - 3 * y ** 2 + (x+1) / (2 * y + 3)
    drugi = -5 * math.sqrt(x + math.sqrt(y))
    treci = 1 + 1 / (2+ (1 / (3 + 1 / 4)))
    cetvrti = 3 * math.sin(2 * alfa) * math.cos(2 * beta) - 5 * math.tan(alfa + beta) ** 2
    peti = math.sqrt(a**2 + b**b - 2 * a * b * math.sin(alfa))

    return prvi, drugi, treci, cetvrti, peti

print(izrazi(x, y, alfa, beta, a, b))


