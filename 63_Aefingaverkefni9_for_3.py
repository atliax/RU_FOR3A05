low = int(input("Sláðu inn lægri tölu talnabils: "))
high = int(input("Sláðu inn hærri tölu talnabils: "))

summa = 0

for i in range(low, high+1):
    summa += i

print("Summa talnanna á bilinu: {}".format(summa))
