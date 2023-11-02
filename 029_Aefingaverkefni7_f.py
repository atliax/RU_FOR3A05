aldur = int(input("Hvað ertu gamall? "))

if aldur >= 0 and aldur <= 6:
    print("Nú, svo þú ferð að byrja í skóla.")
elif aldur >= 7 and aldur <= 15:
    svar = input("Ætlarðu í menntaskóla (J eða N)? ")
    if svar == "J":
        print("Flott hjá þér, menntun er máttur.")
    else:
        print("Æ, það er ekki gott.")
elif aldur > 105:
    print("Líklega hefur þú slegið eitthvað rangt inn.")
else:
    print("Bless bless.")
