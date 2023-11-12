def sum_list(listi):
    summa = 0
    for tala in listi:
        summa += tala
    return summa

size = 0
numbers = []

while(size <= 0):
    size = int(input("Sláðu inn stærð listans: "))

for i in range(1,size+1):
    tala = int(input(f"Sláðu inn tölu ({i} af {size}): "))
    numbers.append(tala)

numbers_summa = sum_list(numbers)
print(f"Summan af tölunum er: {numbers_summa}")
