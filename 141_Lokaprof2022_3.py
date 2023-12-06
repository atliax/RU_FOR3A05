def saekja_heiltolu(strengur):
    heiltala_komin = False
    while not heiltala_komin:
        try:
            tala = int(input(strengur))
            heiltala_komin = True
        except ValueError:
            print("Þetta skilst ekki sem heiltala, reyndu aftur...")
    return tala

strengur = input("Sláðu inn streng: ")
heiltala = saekja_heiltolu("Sláðu inn heiltölu: ")

annar_strengur = strengur[-3:] * heiltala

print(annar_strengur)
