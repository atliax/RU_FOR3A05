PI = 3.14

input_komid = False
while not input_komid:
    try:
        radius = float(input("Sláðu inn radíus: "))
        input_komid = True
    except ValueError:
        print("Þetta var ekki heilbrigð tala hjá þér...")

flatarmal_hrings = radius*radius*PI
ummal_hrings = 2*radius*PI
rummal_kulu = (4.0*PI*(radius**3)) / 3.0

print(f"Ef gefinn er radíusinn {radius}, þá reiknast eftirfarandi:")
print(f"Flatarmál hrings: {flatarmal_hrings}")
print(f"Ummál hrings: {ummal_hrings}")
print(f"Rúmmál kúlu: {rummal_kulu}")
