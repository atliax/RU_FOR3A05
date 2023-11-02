text = ""

while(len(text) < 1):
    text = input("Sláðu inn texta: ")

if text.isdigit():
    print("Textinn inniheldur bara tölustafi.")
elif text.isalpha():
    print("Textinn inniheldur bara bókstafi.")
else:
    print("Nú segi ég eins og Óli: Þú ert nú meiri rugludallurinn!")
