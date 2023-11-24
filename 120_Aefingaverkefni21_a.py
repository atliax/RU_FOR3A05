keyra = True
simaskra = {}

while keyra:
    nafn = input("Sláðu inn nafn:")
    simanumer = input("Sláðu inn símanúmer: ")

    simaskra[nafn] = simanumer

    val = 0
    while val != 1 and val != 2:
        val = int(input("Veldu 1 til að slá inn fleiri eða 2 til að hætta: "))

    if val == 2:
        keyra = False

print("Fólkið í símaskránni:")
for key, value in simaskra.items():
    print(f"Nafn: {key}")
    print(f"Símanúmer: {value}\n")
