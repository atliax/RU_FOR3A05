import math

def circle(radius):
    return 2.0 * math.pi * radius

tala = float(input("Sláðu inn radíus hrings: "))

ummal = circle(tala)

print("Ummál hrings með radíus {0} er: {1}".format(tala,round(ummal,3)))
