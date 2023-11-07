def prenta_tolur(lower, upper):
    for i in range(lower,upper+1):
        print(i, end=" ")
    print()

tala1 = int(input("Sláðu inn upphaf talnabils: "))
tala2 = int(input("Sláðu inn endi talnabils: "))

print("Tölurnar á því bili eru: ")

prenta_tolur(tala1,tala2)
