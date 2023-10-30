low = int(input("Sláðu inn lægri tölu talnabils: "))
high = int(input("Sláðu inn hærri tölu talnabils: "))

summa = 0

for i in range(low, high+1):
    if i % 2 == 0:
        summa += i

print("Summa sléttu talnanna á bilinu: {}".format(summa))
