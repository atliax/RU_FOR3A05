size = 0
numbers = []

while(size <= 0):
    size = int(input("Sláðu inn stærð listans: "))

for i in range(1,size+1):
    tala = int(input(f"Sláðu inn tölu ({i} af {size}): "))
    numbers.append(tala)

numbers_average = sum(numbers) / len(numbers)
print(f"Meðaltalið af tölunum er: {numbers_average}")
