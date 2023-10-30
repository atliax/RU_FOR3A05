low = int(input("Sláðu inn lægri tölu talnabils: "))
high = int(input("Sláðu inn hærri tölu talnabils: "))

tmp = low

print("Oddatölur á því bili: ")

while tmp <= high:
    if tmp % 2 == 1:
        print(tmp)
    tmp += 1
