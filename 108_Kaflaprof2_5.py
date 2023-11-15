def lengd_strengs(strengur):
    lengd = 0
    for stafur in strengur:
        lengd += 1
    return lengd

texti = input("Sláðu inn streng: ")
texti_lengd = lengd_strengs(texti)

print(f"Lengd strengsins er {texti_lengd}")
