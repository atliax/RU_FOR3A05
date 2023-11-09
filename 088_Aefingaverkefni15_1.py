def sum_of_three(a,b,c):
    return a+b+c

tala1 = int(input("Sláðu inn fyrstu töluna: "))
tala2 = int(input("Sláðu inn aðra töluna: "))
tala3 = int(input("Sláðu inn þriðju töluna: "))

summa = sum_of_three(tala1,tala2,tala3)

print(f"Summan af {tala1}, {tala2} og {tala3} er: {summa}")
