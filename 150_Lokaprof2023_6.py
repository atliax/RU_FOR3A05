PI = 3.14

def saekja_kommutolu(strengur):
    tala_komin = False
    while not tala_komin:
        try:
            tala = float(input(strengur))
            tala_komin = True
        except ValueError:
            print("Þetta skilst ekki sem tala, reyndu aftur...")
    return tala

class Kula:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Radíusinn er {self.radius}"

    def rummal_kulu(self):
        return (4.0 * PI * (self.radius ** 3)) / 3.0

rad = saekja_kommutolu("Sláðu inn radíus kúlu:")

kula = Kula(rad)
rummal = round(kula.rummal_kulu(),2)
print(f"Rúmmál kúlunnar er: {rummal}")
print(kula)
