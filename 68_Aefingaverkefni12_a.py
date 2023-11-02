def textalengd(strengur):
    talning = 0
    for _ in strengur:
        talning += 1
    return talning

texti = "Hallo heimur"
lengd = textalengd(texti)

print(texti[0])
print(texti[-1])
print("Lengd: {}".format(lengd))
