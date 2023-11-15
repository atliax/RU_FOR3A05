val = 0
summa = 0

upphaf = int(input("Sláðu inn fyrstu tölu talnabils: "))
endir = int(input("Sláðu inn síðustu talnabils: "))

print("1. Prenta í vaxandi röð")
print("2. Prenta í minnkandi röð")

while(val != 1 and val != 2):
    val = int(input("Veldu 1 eða 2: "))

if val == 1:
    for i in range(upphaf,endir+1):
        print(i)
        summa += i
else:
    i = endir
    while(i >= upphaf):
        print(i)
        summa += i
        i -= 1

print(f"Summa talnanna á bilinu {upphaf}-{endir} er: {summa}")
