hitastig = float(input("Hvað er hitastigið í Palo Alto? (fahrenheit) "))
sumar = input("Er sumar? (J eða N) ").upper()

lower = 60
upper = 90

if sumar == "J":
    upper += 10

if hitastig >= lower and hitastig <= upper:
    print("Íkornarnir eru að leika sér í dag.")
else:
    print("Íkornarnir eru ekki að leika sér í dag.")
