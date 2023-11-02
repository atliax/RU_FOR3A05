def textalengd(strengur):
    talning = 0
    for _ in strengur:
        talning += 1
    return talning

texti = input("Sláðu inn texta: ")
fjoldi = -1

while fjoldi < 0 or fjoldi > textalengd(texti):
    fjoldi = int(input("Hvað á að prenta marga stafi? "))

print(texti[0:fjoldi])
