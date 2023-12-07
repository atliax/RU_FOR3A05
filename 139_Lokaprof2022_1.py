def saekja_heiltolu(strengur):
    heiltala_komin = False
    while not heiltala_komin:
        try:
            tala = int(input(strengur))
            heiltala_komin = True
        except ValueError:
            print("Þetta skilst ekki sem heiltala, reyndu aftur...")
    return tala

PI = 3.14

input_komid = False
while not input_komid:
    try:
        radius = float(input("Sláðu inn radíus: "))
        input_komid = True
    except ValueError:
        print("Þetta var ekki heilbrigð tala hjá þér...")

val = 0
print("1. Flatarmál hrings")
print("2. Ummál hrings")
print("3. Rúmmál kúlu")
print("4. Hætta")
while val < 1 or val > 4:
    val = saekja_heiltolu("Veldu 1-4: ")

if(val == 1):
    flatarmal_hrings = radius*radius*PI
    print(f"Flatarmál hrings: {flatarmal_hrings}")
elif(val == 2):
    ummal_hrings = 2*radius*PI
    print(f"Ummál hrings: {ummal_hrings}")
elif(val == 3):
    rummal_kulu = (4.0*PI*(radius**3)) / 3.0
    print(f"Rúmmál kúlu: {rummal_kulu}")
