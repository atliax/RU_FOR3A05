filename = input("Sláðu inn nafn á skrá: ")
filename = "data/"+filename

ord = []

with open(filename, 'r') as file:
    for lina in file:
        lina = lina.strip("\n")
        lina_ord_listi = lina.split(" ")
        for lina_ord in lina_ord_listi:
            ord.append(lina_ord)

lengstaord = max(ord,key=len)
lengd = len(lengstaord)

print(f"Lengsta orðið í skránni ({lengd} stafir): {lengstaord}")
