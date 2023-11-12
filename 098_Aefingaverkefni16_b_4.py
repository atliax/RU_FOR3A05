def average_list(listi):
    summa = 0.0
    talning = 0.0
    for tala in listi:
        summa += tala
        talning += 1.0
    return summa / talning

size = 0
numbers = []

while(size <= 0):
    size = int(input("Sláðu inn stærð listans: "))

for i in range(1,size+1):
    tala = int(input(f"Sláðu inn tölu ({i} af {size}): "))
    numbers.append(tala)

numbers_average = average_list(numbers)
print(f"Meðaltalið af tölunum er: {numbers_average}")
