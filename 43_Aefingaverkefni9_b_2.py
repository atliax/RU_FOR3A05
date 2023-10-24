hitastig = float(input("Hvað er hitastigið í Palo Alto? (fahrenheit) "))
season = input("Er sumar? (J eða N) ")

lower = 60
upper = 90

if season == "J":
    upper += 10

if hitastig >= lower and hitastig <= upper:
    print("Íkornarnir eru að leika sér í dag.")
else:
    print("Íkornarnir eru ekki að leika sér í dag.")
