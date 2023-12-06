filename = "JorgeLuisBorgesQuote.txt"

oll_ordin = []
ord_talning = {}

with open(filename, "r") as file:
    raw_innihald = file.read().split()

for ord in raw_innihald:
    oll_ordin.append(ord.strip("“").strip("”").strip(",").strip(".").lower())

einstok_ord = set(oll_ordin)
fjoldi_einstakra_orda = len(einstok_ord)
heildarfjoldi_orda = len(oll_ordin)

print(f"Heildarfjöldi orða: {heildarfjoldi_orda}")
print(f"Fjöldi einstakra orða: {fjoldi_einstakra_orda}")
