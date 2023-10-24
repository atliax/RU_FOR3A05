lower = int(input("Sláðu inn neðri mörk talnabils: "))
upper = int(input("Sláðu inn efri mörk talnabils: "))

for i in range(lower,upper+1):
    if i % 5 != 0:
        print(i)
