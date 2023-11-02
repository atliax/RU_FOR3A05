low = int(input("Sláðu inn lægri tölu talnabils: "))
high = int(input("Sláðu inn hærri tölu talnabils: "))

tmp = low
summa = 0

while tmp <= high:
    summa += tmp
    tmp += 1

print("Summa talnanna á bilinu: {}".format(summa))
