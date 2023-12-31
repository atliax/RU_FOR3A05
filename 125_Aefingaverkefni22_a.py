import pprint

pp = pprint.PrettyPrinter(indent=4)

skjal = "data/Tesla.txt"

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

pp.pprint(talning)
