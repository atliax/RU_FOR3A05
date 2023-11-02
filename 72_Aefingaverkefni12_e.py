texti = input("Sláðu inn texta sem inniheldur bæði hástafi og lágstafi: ")
val = 0

print("1. Bara hástafir")
print("2. Bara lágstafir")

while val != 1 and val != 2:
    val = int(input("Veldu 1 eða 2: "))

if val == 1:
    print(texti.upper())
else:
    print(texti.lower())
