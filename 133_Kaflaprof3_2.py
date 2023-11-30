fjoldi = int(input("Hversu margir voru nemendurnir? "))

einkunnir = []
summa_einkunna = 0
fjoldi_med_tiu = 0

for i in range(1,fjoldi+1):
    einkunn = int(input(f"Sláðu inn einkunn næsta nemanda ({i} af {fjoldi}):"))
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
    summa_einkunna += einkunnir[i]

medaleinkunn = summa_einkunna / fjoldi

print(f"Meðaleinkunn: {round(medaleinkunn,2)}")
print(f"Hæsta einkunn: {haesta_einkunn}")
print(f"Lægsta einkunn: {laegsta_einkunn}")
print(f"Fjöldi nemenda með 10 er: {fjoldi_med_tiu}")
