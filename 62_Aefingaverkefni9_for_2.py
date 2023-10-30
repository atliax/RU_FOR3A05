low = int(input("Sláðu inn lægri tölu talnabils: "))
high = int(input("Sláðu inn hærri tölu talnabils: "))

for i in range(low, high+1):
    if i % 2 == 1:
        print(i)
