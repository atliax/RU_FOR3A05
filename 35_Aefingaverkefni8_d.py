fyrri = int(input("Sláðu inn tölu: "))
seinni = int(input("Sláðu inn aðra tölu: "))

if fyrri > seinni:
    tmp = seinni
    seinni = fyrri
    fyrri = tmp

if fyrri == seinni:
    print("Tölurnar eru jafnháar.")
elif (fyrri+1) == seinni:
    print("Það eru engar tölur á milli þeirra.")
else:
    print("Tölurnar á milli {0} og {1} eru: ".format(fyrri,seinni))
    for i in range(fyrri+1, seinni):
        print(i)
