upphaf = int(input("Sláðu inn upphaf talnabils: "))
endir = int(input("Sláðu inn lok talnabils: "))

for i in range(upphaf,endir+1):
    if (i%4) != 0:
        print(i)
