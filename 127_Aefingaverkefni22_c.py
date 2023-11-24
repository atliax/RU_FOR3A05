skjal = "data/Borges.txt"

talning = {}
ordin = []

with open(skjal, "r") as file:
    tempList = file.read().split()

for temp in tempList:
    ordin.append(temp.strip(".").strip(","))

for ord in ordin:
    if ord in talning:
        talning[ord] += 1
    else:
        talning[ord] = 1

init = False
algengast = ""

for key, value in talning.items():
    if not init:
        algengast = key
        init = True
        continue
    if talning[algengast] < value:
        algengast = key

algengasta_talning = talning[algengast]

print(f"Heildarfjöldi orða: {len(ordin)}")
print(f"Algengasta orðið: \"{algengast}\"")
print(f"það kom fyrir svona oft: {algengasta_talning}")
