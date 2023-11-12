def max_listi(listi):
    haest = listi[0]
    for i in listi:
        if i > haest:
            haest = i
    return haest

def min_listi(listi):
    laegst = listi[0]
    for i in listi:
        if i < laegst:
            laegst = i
    return laegst

hitastig = []

print("Sláðu inn meðalhitastig seinustu 12 mánuði: ")

for i in range(1,13):
    hiti = float(input(f"{i} af 12: "))
    hitastig.append(hiti)

print(f"Hæsta hitastigið var: {max_listi(hitastig)}")
print(f"Lægsta hitastigið var: {min_listi(hitastig)}")
