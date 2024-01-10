PI = 3.14

def saekja_kommutolu(strengur):
    tala_komin = False
    while not tala_komin:
        try:
            tala = float(input(strengur))
            tala_komin = True
        except ValueError:
            print("Þetta skilst ekki sem tala, reyndu aftur...")
    return tala

def saekja_heiltolu(strengur):
    heiltala_komin = False
    while not heiltala_komin:
        try:
            tala = int(input(strengur))
            heiltala_komin = True
        except ValueError:
            print("Þetta skilst ekki sem heiltala, reyndu aftur...")
    return tala

def flatarmal_hrings(radius):
    return radius * radius * PI

def rummal_kulu(radius):
    return (4.0 * PI * (radius ** 3)) / 3.0

rad = saekja_kommutolu("Sláðu inn radíus: ")
utkoma = 0
val = 0

print("Hvað viltu reikna?")
print("1. Rúmmál kúlu")
print("2. Flatarmál hrings")

while val != 1 and val != 2:
    val = saekja_heiltolu("Veldu 1 eða 2: ")

if val == 1:
    utkoma = rummal_kulu(rad)
    print(f"Rúmmál kúlu með radíusinn {rad} er: {utkoma}")
else:
    utkoma = flatarmal_hrings(rad)
    print(f"Flatarmál hrings með radíusinn {rad} er: {utkoma}")
