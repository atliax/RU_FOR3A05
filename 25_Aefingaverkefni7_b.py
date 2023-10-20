klukkustund = int(input("Sláðu inn tíma dags (klukkustund): "))

if klukkustund < 0 or klukkustund > 24:
    print("Rangur innsláttur")
else:
    if klukkustund <= 18:
        print("Góðan daginn")
    else:
        print("Gott kvöld")
