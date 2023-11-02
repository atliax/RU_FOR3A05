prosenta = float(input("Sláðu inn álagningarprósentu: "))
afslattur = int(input("Sláðu inn persónuafslátt: "))
heildarlaun = int(input("Sláðu inn heildarlaun: "))

stadgreidsla = int(((prosenta / 100) * heildarlaun) - afslattur)
utborgad = heildarlaun - stadgreidsla

print("Staðgreiðslan er {0} kr. sem gerir útborguð laun að {1} kr.".format(stadgreidsla,utborgad))
