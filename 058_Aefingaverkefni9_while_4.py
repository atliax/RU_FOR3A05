low = int(input("Sláðu inn lægri tölu talnabils: "))
high = int(input("Sláðu inn hærri tölu talnabils: "))

tmp = low
summa = 0

while tmp <= high:
    if tmp % 2 == 0:
        summa += tmp
    tmp += 1

print("Summa sléttu talnanna á bilinu: {}".format(summa))
