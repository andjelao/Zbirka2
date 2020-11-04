n = int(input("Unesite zeljeni cetvorocifreni broj: "))

def da_li_su_cifre_jedinica_i_hiljada_jednake(n):
    """
    ulazni parametar: cetvorocifreni broj n
    za jednake cifre jedinica i hiljada- > returns kvadrat dvocifrenog broja koji se dobije kada ih uklonimo
    za razlicite cifre jedinica i hiljada -> returns zbir kvadrata svih cifara
    """
    jedinice = n % 10
    hiljade = n // 1000
    stotine = (n // 100) % 10
    desetice = (n // 10) % 10

    if jedinice == hiljade:
        return (stotine * 10 + desetice)**2
    else:
        return hiljade ** 2 + stotine **2 + desetice ** 2 + jedinice ** 2

print(da_li_su_cifre_jedinica_i_hiljada_jednake(n))
