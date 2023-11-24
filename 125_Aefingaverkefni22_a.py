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

print("Orð             Fjöldi")
print("----------------------")
for key,value in talning.items():
    if len(key) > 7:
        spacer = "\t"
    else:
        spacer = "\t\t"

    print(f"{key}{spacer}{value}")
