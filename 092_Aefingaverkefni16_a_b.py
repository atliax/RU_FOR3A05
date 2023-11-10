forsetar = ["James E. Carter", "Ronald Reagan", "George H. W. Bush", \
            "William J. Clinton", "George W. Bush", "Barack H. Obama", \
            "Donald J. Trump", "Joseph R. Biden"]

val = input("Hefurðu einhvern forseta Bandaríkjanna í huga?")

if val in forsetar:
    print("Hann er á listanum.")
else:
    print("Hann er ekki á listanum.")
