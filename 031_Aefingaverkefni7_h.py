year = int(input("Sláðu inn ártal: "))

leap = False

if year % 4 == 0:
    leap = True

if year % 100 == 0:
    leap = False

if year % 400 == 0:
    leap = True

if leap:
    print("Árið {} er hlaupár.".format(year))
else:
    print("Árið {} er ekki hlaupár.".format(year))
