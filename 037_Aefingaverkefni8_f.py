lower = int(input("Sláðu inn neðri mörk talnabils: "))
upper = int(input("Sláðu inn efri mörk talnabils: "))
summa = 0

for i in range(lower,upper+1):
    summa += i

print("Summan af tölunum frá {0} upp í {1} er: {2}".format(lower,upper,summa))
