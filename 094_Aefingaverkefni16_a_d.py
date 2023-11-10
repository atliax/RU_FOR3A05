forsetar = ["James E. Carter", "Ronald Reagan", "George H. W. Bush", \
            "William J. Clinton", "George W. Bush", "Barack H. Obama", \
            "Donald J. Trump", "Joseph R. Biden"]

val = input("Hver var forseti á undan James E. Carter? ")
val2 = input("Og hver verður næsti forseti á eftir Joseph R. Biden? ")

forsetar.insert(0,val)

if forsetar[-1] != val2:
    forsetar.append(val2)

print("Hérna má þá sjá lista af nokkrum seinustu forsetum Bandaríkjanna:")

for forseti in forsetar:
    print(forseti)
