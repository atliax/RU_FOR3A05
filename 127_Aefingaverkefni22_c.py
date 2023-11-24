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

algengasta_ord = max(talning.items(), key=lambda x:x[1])
print(f"Algengasta orðið: \"{algengasta_ord[0]}\"")
print(f"það kom fyrir svona oft: {algengasta_ord[1]}")
