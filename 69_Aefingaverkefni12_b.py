def textalengd(strengur):
    talning = 0
    for _ in strengur:
        talning += 1
    return talning

texti = "A Santa at Nasa"
texti_afturabak = texti[::-1]

lengd = textalengd(texti)

for stafur in texti:
    print(stafur)

for stafur in texti_afturabak:
    print(stafur)

#gamla afturábak dótið:
#for i in range(1, lengd+1):
#    index = i * -1
#    print(texti[index])
