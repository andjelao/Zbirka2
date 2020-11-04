x = int(input("Unesite broj koji zelite da provjerite: "))
a = int(input("Unesite donju granicu intervala: "))
b = int(input("Unesite gornju granicu intervala: "))

def da_li_broj_pripada_zatvorenom_intervalu(x, a, b):
    """
    ulazni parametri: x -> broj za koji provjeravamo pripada li intervalu
                      a -> donja granica intervala, pripada intervalu
                      b -> gornja granica intervala, pripada intervalu
    stampa "Pripada" ili "Ne pripada"
    """
    if x >= a and x <=b:
        print("Pripada")
    else: 
        print("Ne pripada")
        
da_li_broj_pripada_zatvorenom_intervalu(x, a, b)
