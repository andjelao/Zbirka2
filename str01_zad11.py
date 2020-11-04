n = int(input("Unesite zeljeni trocifreni broj: "))

def da_li_je_zbir_cifara_trocifrenog_broja_dvocifren_broj(n):
    """
    ulazni parametar: trocifren broj n
    returns boolean da li je zbir cifara n dvocifren broj
    """
    zadnja_cifra = n % 10
    srednja_cifra = (n // 10) % 10
    prva_cifra = n // 100
    """
    kako je najveci trocifreni broj 999 i njegov zbir cifara 27, nema potrebe da provjeravamo uslov 
    da li je suma cifara manja od 100 da bi bila dvocifren broj
    """
    return zadnja_cifra + srednja_cifra + prva_cifra > 9 

print(da_li_je_zbir_cifara_trocifrenog_broja_dvocifren_broj(n))
