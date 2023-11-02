tala1 = int(input("Sláðu inn heiltölu: "))
tala2 = int(input("Sláðu inn aðra heiltölu: "))
tala3 = int(input("Sláðu inn eina heiltölu í viðbót: "))
minnsta = 0

if tala1 < tala2:
    minnsta = tala1
else:
    minnsta = tala2

if tala3 < minnsta:
    minnsta = tala3

print("Minnsta talan var {0}.".format(minnsta))
