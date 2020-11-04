
n = int(input("Unesite zeljeni cetvorocifreni broj: "))

def proizvodi_cifara_ac_i_bd_jednaki(n):
    """
    ulazni paramterar: cetvorocifreni broj n
    stampa "Super" ako je prva cifra a * treca cifra c = druga cifra b * cetvrta cifra d
    """
    a = n // 1000
    b = (n // 100) % 10
    c = (n // 10) % 10
    d = n % 10

    if a * c == b * d:
        print("Super")

proizvodi_cifara_ac_i_bd_jednaki(n)

