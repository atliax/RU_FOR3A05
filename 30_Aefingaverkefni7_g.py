year = int(input("Sláðu inn ártal: "))

if year % 4 == 0:
    print("Árið {} er hlaupár.".format(year))
else:
    print("Árið {} er ekki hlaupár.".format(year))
