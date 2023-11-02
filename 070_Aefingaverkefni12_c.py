texti = input("Sláðu inn texta: ")
fjoldi = -1

while fjoldi < 0 or fjoldi > len(texti):
    fjoldi = int(input("Hvað á að prenta marga stafi? "))

print(texti[0:fjoldi])
