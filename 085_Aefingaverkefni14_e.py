def power(n, p):
    return n ** p

tala = int(input("Sláðu inn tölu: "))
veldi = int(input("Sláðu inn veldi: "))

utkoma = power(tala,veldi)

print(f"Talan {tala} í veldinu {veldi} er {utkoma}.")
