nafn = input("Vinsamlegast sláið inn nafn keppanda: ")
thyngd = int(input("Vinsamlegast sláið inn þyngd keppanda: "))

print("Nafn: {}".format(nafn))
print("Þyngdarflokkur: ", end="")

if thyngd < 65:
    print("fluguvigt")
elif thyngd >= 65 and thyngd <= 100:
    print("millivigt")
else:
    print("þungavigt")
