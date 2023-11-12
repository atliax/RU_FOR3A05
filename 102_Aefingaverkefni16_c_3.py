import random

sortir = ["Hjarta", "Spaða", "Tígul", "Laufa"]
spil = ["Ás", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Gosa", "Drottningu", "Kóng"]

sort = random.choice(sortir)
spil = random.choice(spil)

print(f"Þú dróst {sort} {spil}.")
