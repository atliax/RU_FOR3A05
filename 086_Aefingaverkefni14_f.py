def modulus(n,m):
    if n >= m:
        talning = 0
        afrit_n = n
        while(afrit_n >= m):
            talning += 1
            afrit_n -= m
        return n - (talning*m)
    else:
        return n

tala = int(input("Sláðu inn tölu: "))

modtala = 0
while(modtala <= 0):
    modtala = int(input("Sláðu inn aðra tölu (hærri en 0): "))

utkoma = modulus(tala,modtala)

print(f"{tala} deilt með {modtala} gefur afganginn {utkoma}.")
