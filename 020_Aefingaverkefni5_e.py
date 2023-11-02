veldisstofn = float(input("Sláðu inn veldisstofn: "))
veldisvisir = float(input("Sláðu inn veldisvísi: "))
nidurstada = veldisstofn ** veldisvisir

print("{0} í veldinu {1} er {2}".format(veldisstofn,veldisvisir,round(nidurstada,3)))
