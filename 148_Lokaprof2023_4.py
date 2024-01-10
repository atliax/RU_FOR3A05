def saekja_heiltolu(strengur):
    heiltala_komin = False
    while not heiltala_komin:
        try:
            tala = int(input(strengur))
            heiltala_komin = True
        except ValueError:
            print("Þetta skilst ekki sem heiltala, reyndu aftur...")
    return tala

strengur = input("Sláðu inn textastreng: ")
tala = saekja_heiltolu("Sláðu inn tölu: ")

val = 0

print("Hvernig viltu að strengurinn sé prentaður?")
print("1. Rétt röð")
print("2. Öfug röð")

while val != 1 and val != 2:
    val = saekja_heiltolu("Veldu 1 eða 2: ")

if val == 1:
    print(strengur[::tala])
else:
    print(strengur[::-tala])
