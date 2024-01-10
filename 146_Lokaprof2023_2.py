def saekja_heiltolu(strengur):
    heiltala_komin = False
    while not heiltala_komin:
        try:
            tala = int(input(strengur))
            heiltala_komin = True
        except ValueError:
            print("Þetta skilst ekki sem heiltala, reyndu aftur...")
    return tala

tala1 = saekja_heiltolu("Sláðu inn upphaf talnabils:")
tala2 = saekja_heiltolu("Sláðu inn endi talnabils:")

val = 0

print("1. Prenta í vaxandi röð")
print("2. Prenta í minnkandi röð")

while(val != 1 and val != 2):
    val = saekja_heiltolu("Veldu 1 eða 2:")

if(tala1 > tala2):
    temp = tala1
    tala1 = tala2
    tala2 = temp

if(val == 1):
    for i in range(tala1, tala2+1):
        if i % 3 != 0 and i % 5 != 0:
            print(i)
else:
    i_tala = tala2
    while i_tala >= tala1:
        if i_tala % 3 != 0 and i_tala % 5 != 0:
            print(i_tala)
        i_tala -= 1
