import math

radius = float(input("Sláðu inn radíus hrings: "))
area = (radius ** 2) * math.pi

print("Flatarmál hrings með radíus {0} er {1}".format(radius,round(area,2)))
