einkunnir = []
summa = 0.0

for i in range(5):
    einkunnir.append(float(input("Sláðu inn einkunn {} af 5: ".format(i+1))))
    summa += einkunnir[i]

medaltal = summa / 5
print("Meðaleinkunn: {}".format(medaltal))
