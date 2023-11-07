import math

def circle(radius):
    return 2.0 * math.pi * radius

tala = float(input("Sláðu inn radíus hrings: "))

ummal = circle(tala)

print(f"Ummál hrings með radíus {tala} er: {round(ummal,3)}")
