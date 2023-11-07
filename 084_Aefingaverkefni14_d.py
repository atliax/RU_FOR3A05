def prenta_tolur_milli(lower, upper):
    if lower == upper:
        print("Tölurnar mega ekki vera eins.")
    elif lower > upper:
        print("Fyrri talan þarf að vera lægri talan.")
    elif (lower+1) == upper:
        print("Það eru engar tölur á milli {lower} og {upper}.")
    else:
        print(f"Tölurnar á milli {lower} og {upper} eru: ")
        for i in range(lower+1,upper):
            print(i, end=" ")
        print()

tala1 = int(input("Sláðu inn upphaf talnabils: "))
tala2 = int(input("Sláðu inn endi talnabils: "))

prenta_tolur_milli(tala1,tala2)
