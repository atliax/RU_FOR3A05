texti = input("Sláðu inn texta: ")
tala = 0

while tala < 1:
    tala = int(input("Sláðu inn tölu (1 eða hærri): "))

print(texti[::tala])
