filename = "BorgesTilvitnun.txt"

oll_ordin = []
ord_talning = {}

with open(filename, "r") as file:
    raw_innihald = file.read().split()

for ord in raw_innihald:
    oll_ordin.append(ord.strip(".").strip(",").strip(";"))

einstok_ord = set(oll_ordin)
fjoldi_einstakra_orda = len(einstok_ord)

for ord in oll_ordin:
    if ord in ord_talning:
        ord_talning[ord] += 1
    else:
        ord_talning[ord] = 1

fyrsta_keyrsla = True
algengasta_ord = ""

for key,value in ord_talning.items():
    if fyrsta_keyrsla:
        algengasta_ord = key
        fyrsta_keyrsla = False
    if ord_talning[algengasta_ord] < value:
        algengasta_ord = key

print(f"Fjöldi ólíkra orða í skránni: {fjoldi_einstakra_orda}")
print(f"Algengasta orðið í skránni: \"{algengasta_ord}\"")
print(f"Það kom fyrir svona oft: {ord_talning[algengasta_ord]}")
