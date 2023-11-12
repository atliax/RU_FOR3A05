def max_list(listi):
    max = listi[0]
    for tala in listi:
        if tala > max:
            max = tala
    return max

size = 0
numbers = []

while(size <= 0):
    size = int(input("Sláðu inn stærð listans: "))

for i in range(1,size+1):
    tala = int(input(f"Sláðu inn tölu ({i} af {size}): "))
    numbers.append(tala)

numbers_max = max_list(numbers)
print(f"Hæsta talan í listanum er: {numbers_max}")
