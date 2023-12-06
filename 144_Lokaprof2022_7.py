def saekja_kommutolu(strengur):
    kommutala_komin = False
    while not kommutala_komin:
        try:
            tala = float(input(strengur))
            kommutala_komin = True
        except ValueError:
            print("Þetta skilst ekki sem tala, reyndu aftur...")
    return tala

class Sivalningur:
    def __init__(self,radius,haed) -> None:
        self.__radius = radius
        self.__haed = haed

    def __str__(self) -> str:
        return f"Radíus: {self.__radius}, Hæð: {self.__haed}"

    def rummal(self) -> float:
        return self.__haed * 3.14 * self.__radius * self.__radius

radius = saekja_kommutolu("Sláðu inn radíus sívalnings: ")
haed = saekja_kommutolu("Sláðu inn hæð sívalnings: ")

sivalningur_eintak = Sivalningur(radius, haed)

print(f"Rúmmál sívalningsins er: {sivalningur_eintak.rummal()}")
print(f"Helstu stærðir sívalningsins eru: {sivalningur_eintak}")
