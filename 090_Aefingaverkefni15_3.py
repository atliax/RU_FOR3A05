def factorial(n):
    if n < 0:
        return None
    else:
        margfeldi = 1
        for i in range(1,n+1):
            margfeldi *= i
        return margfeldi

tala = int(input("Sláðu inn tölu: "))

tala_hropmerkt = factorial(tala)

if(tala_hropmerkt != None):
    print(f"Talan {tala} hrópmerkt er: {tala_hropmerkt}.")
else:
    print("Ekki er hægt að hrópmerkja neikvæðar tölur.")
