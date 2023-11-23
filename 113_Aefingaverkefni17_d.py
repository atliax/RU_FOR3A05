filename = "data/Setningar.txt"

ord = []
seinasta_ord = ""
setning = ""

with open(filename, 'w') as file:
    while seinasta_ord != "EOF":
        ord_inn = input("Sláðu inn næsta orð: ").strip() #strip() til öryggis
        ord.append(ord_inn)
        seinasta_ord = ord_inn

        if ord_inn[-1] == ".":
            for i in range(0,len(ord)):
                if ord[i] != ".": #ef orðið er ekki bara punktur einn og sér
                    setning += " "#þá setjum við bil (annars kæmi bil á undan punktinum)
                setning += ord[i]
            setning = setning.strip()+"\n" #strip() til öryggis, ætti ekki strang til tekið að þurfa
            file.write(setning)
            setning = ""
            ord.clear()
