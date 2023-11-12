hitastig = []

print("Sláðu inn meðalhitastig seinustu 12 mánuði: ")

for i in range(1,13):
    hiti = float(input(f"{i} af 12: "))
    hitastig.append(hiti)

print(f"Hæsta hitastigið var: {max(hitastig)}")
print(f"Lægsta hitastigið var: {min(hitastig)}")
