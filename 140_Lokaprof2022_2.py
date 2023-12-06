def saekja_heiltolu(strengur):
    heiltala_komin = False
    while not heiltala_komin:
        try:
            tala = int(input(strengur))
            heiltala_komin = True
        except ValueError:
            print("Þetta skilst ekki sem heiltala, reyndu aftur...")
    return tala

fyrri_tala = saekja_heiltolu("Sláðu inn neðri mörk talnabils (heiltala): ")
seinni_tala = saekja_heiltolu("Sláðu inn efri mörk talnabils (heiltala): ")

#víxla tölum ef notandinn er með slæman lesskilning...
if seinni_tala < fyrri_tala:
    geyma = fyrri_tala
    fyrri_tala = seinni_tala
    seinni_tala = geyma

for i in range(fyrri_tala, seinni_tala+1):
    if i % 4 != 0 and i % 7 != 0:
        print(i)
