print("Unesite koeficijente kvadratne jednacine: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

def da_li_kvadratna_jednacina_ima_realna_rjesenja(a, b, c):
    """
    ulazni parametri: koeficijenti kvadratne jednacine
    boolean returns true ako je determinanta d >= 0
    """
    return b**2 - 4*a*c >= 0

print(da_li_kvadratna_jednacina_ima_realna_rjesenja(a, b, c))