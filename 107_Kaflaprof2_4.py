def reikna_vsk(an_vsk, prosenta):
    return an_vsk * (1.0 + prosenta/100.0)

kronur = int(input("Sláðu inn upphæð án VSK: "))
prosent = float(input("Sláðu inn VSK prósentu: "))
lokaverd = reikna_vsk(kronur,prosent)

print(f"Verðið með VSK er: {lokaverd} kr.")
