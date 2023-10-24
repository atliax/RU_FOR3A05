def factorial(n):
    res = 1
    while(n-1 != 0):
        res += res * (n-1)
        n -= 1

    return res

lower = int(input("Sláðu inn neðri mörk talnabils: "))
upper = int(input("Sláðu inn efri mörk talnabils: "))

print("Tölur frá {0} upp í {1}:".format(lower,upper))

for i in range(lower,upper+1):
    fact_i = factorial(i)
    print("{0}! = {1}".format(i,fact_i))
