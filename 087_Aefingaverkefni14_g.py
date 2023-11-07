def leap_year(y):
    leap = False

    if year % 4 == 0:
        leap = True

    if year % 100 == 0:
        leap = False

    if year % 400 == 0:
        leap = True

    return leap

year = int(input("Sláðu inn ártal: "))

hlaupar = leap_year(year)

if hlaupar:
    print(f"Árið {year} er hlaupár.")
else:
    print(f"Árið {year} er ekki hlaupár.")
