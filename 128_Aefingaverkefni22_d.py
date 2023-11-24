skjal1 = "data/Borges.txt"
skjal2 = "data/Tesla.txt"

ordin_borges = []
ordin_tesla = []

with open(skjal1, "r") as file:
    tempList = file.read().split()
for temp in tempList:
    ordin_borges.append(temp.strip(".").strip(","))
ordin_borges_set = set(ordin_borges)

with open(skjal2, "r") as file:
    tempList = file.read().split()
for temp in tempList:
    ordin_tesla.append(temp.strip(".").strip(","))
ordin_tesla_set = set(ordin_tesla)

ordin_snid_set = ordin_borges_set & ordin_tesla_set

print("Orðin sem eru í báðum skránum:")
for ord in ordin_snid_set:
    print(ord)
