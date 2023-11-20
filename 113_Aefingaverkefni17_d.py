filename = "data/Setningar.txt"

ord = []
seinasta_ord = ""
setning = ""

with open(filename, 'w') as file:
    while seinasta_ord != "EOF":
        ord_inn = input("Sláðu inn næsta orð: ")
        ord.append(ord_inn)
        seinasta_ord = ord_inn

        if ord_inn[-1] == ".":
            for i in range(0,len(ord)):
                setning += " " + ord[i]
            setning = setning.strip()+"\n"
            file.write(setning)
            setning = ""
            ord.clear()
