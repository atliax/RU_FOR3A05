numbers = [6,5,4,3]

number_input = int(input("Sláðu inn tölu: "))

if number_input in numbers:
    print(f"{number_input} is in the list.")
else:
    print(f"{number_input} is not in the list.")
