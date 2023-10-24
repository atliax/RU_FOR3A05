lower = int(input("Sláðu inn neðri mörk talnabilsins: "))
upper = int(input("Sláðu inn efri mörk talnabilsins: "))

print("Tölur frá {0} upp í {1}: ".format(lower,upper))
for i in range(lower,upper+1):
    print(i)
