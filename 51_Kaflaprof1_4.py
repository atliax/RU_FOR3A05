dagur = int(input("Sláðu inn dag: "))
manudur = input("Sláðu inn mánuð: ")
ar = int(input("Sláðu inn ár: "))

if dagur == 26 and manudur == "október" and ar == 2023:
    print("rétt")
else:
    print("rangt")
