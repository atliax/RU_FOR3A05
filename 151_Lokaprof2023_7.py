filename = "HanSolo.txt"

oll_ordin = []
ord_talning = {}
oftar_en_einu_sinni = 0

with open(filename, "r") as file:
    raw_innihald = file.read().split()

for ord in raw_innihald:
    oll_ordin.append(ord.replace(",","").replace(".","").replace("?","").lower())

for ord in oll_ordin:
    if ord in ord_talning:
        ord_talning[ord] += 1
    else:
        ord_talning[ord] = 1

for key, value in ord_talning.items():
    if value > 1:
        oftar_en_einu_sinni += 1

heildarfjoldi_orda = len(oll_ordin)

print(f"Orð sem koma fyrir oftar en einu sinni eru: {oftar_en_einu_sinni}")
print(f"Heildarfjöldi orða í skránni er: {heildarfjoldi_orda}")
