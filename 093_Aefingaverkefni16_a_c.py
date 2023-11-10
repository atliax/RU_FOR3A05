forsetar = ["James E. Carter", "Ronald Reagan", "George H. W. Bush", \
            "William J. Clinton", "George W. Bush", "Barack H. Obama", \
            "Donald J. Trump", "Joseph R. Biden"]

val = input("Hefurðu einhvern forseta Bandaríkjanna í huga?")

fannst = False

for forseti in forsetar:
    if val[:4].lower() == forseti[:4].lower():
        fannst = True

if fannst:
    print("Hann er á listanum.")
else:
    print("Hann er ekki á listanum.")
