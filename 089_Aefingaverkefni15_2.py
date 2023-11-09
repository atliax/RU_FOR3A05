def profa_bil(tala,upphaf,endir):
    if tala >= upphaf and tala <= endir:
        print("Talan er á bilinu.")
    else:
        print("Talan er EKKI á bilinu.")

tala1 = int(input("Sláðu inn tölu: "))
tala2 = int(input("Sláðu inn lægri mörk talnabils: "))
tala3 = int(input("Sláðu inn hærri mörk talnabils: "))

profa_bil(tala1,tala2,tala3)
