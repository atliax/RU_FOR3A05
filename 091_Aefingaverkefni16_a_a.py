forsetar = ["James E. Carter", "Ronald Reagan", "George H. W. Bush", \
            "William J. Clinton", "George W. Bush", "Barack H. Obama", \
            "Donald J. Trump", "Joseph R. Biden"]

val = 0

print("1. Forsetar fyrir 2000")
print("2. Forsetar eftir 2000")

while(val != 1 and val != 2):
    val = int(input("Veldu 1 eða 2: "))

if(val == 1):
    for forseti in forsetar[:4]:
        print(forseti)
else:
    for forseti in forsetar[4:]:
        print(forseti)
