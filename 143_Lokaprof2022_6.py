def saekja_heiltolu(strengur):
    heiltala_komin = False
    while not heiltala_komin:
        try:
            tala = int(input(strengur))
            heiltala_komin = True
        except ValueError:
            print("Þetta skilst ekki sem heiltala, reyndu aftur...")
    return tala

fjoldi = saekja_heiltolu("Hversu margir voru nemendurnir? ")

einkunnir = []
fjoldi_med_5_og_yfir = 0
fjoldi_med_tiu = 0

for i in range(1,fjoldi+1):
    einkunn = saekja_heiltolu(f"Sláðu inn einkunn næsta nemanda ({i} af {fjoldi}):")
    einkunnir.append(einkunn)

haesta_einkunn = einkunnir[0]
laegsta_einkunn = einkunnir[0]

for i in range(0,fjoldi):
    if einkunnir[i] > haesta_einkunn:
        haesta_einkunn = einkunnir[i]
    if einkunnir[i] < laegsta_einkunn:
        laegsta_einkunn = einkunnir[i]
    if einkunnir[i] == 10:
        fjoldi_med_tiu += 1
    if einkunnir[i] >= 5:
        fjoldi_med_5_og_yfir += 1

print(f"Hæsta einkunn: {haesta_einkunn}")
print(f"Lægsta einkunn: {laegsta_einkunn}")
print(f"Fjöldi nemenda með 5 og hærra er: {fjoldi_med_5_og_yfir}")
print(f"Fjöldi nemenda með 10 er: {fjoldi_med_tiu}")
