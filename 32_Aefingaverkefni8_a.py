svar = 'J'
while(svar != 'N'):
    tala = int(input("Sláðu inn tölu: "))
    print("Þú hefur valið töluna {}.".format(tala))
    svar = input("Viltu slá inn fleiri tölur? (J eða N) ").upper()
