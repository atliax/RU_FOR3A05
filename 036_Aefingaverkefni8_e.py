lower = int(input("Sláðu inn neðri mörk talnabils: "))
upper = int(input("Sláðu inn efri mörk talnabils: "))

print("Tölur frá {0} upp í {1}:".format(lower,upper))
for i in range(lower,upper+1):
    print("{0} - í öðru veldi: {1}".format(i,i**2))
