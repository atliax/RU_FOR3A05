hofudborgir = ["Róm","Washington","Reykjavík","París","Kaupmannahöfn"]

inntak = input("Sláðu inn nafn á höfuðborg: ")

if inntak in hofudborgir:
    print("Þessi borg er í listanum.")
else:
    svar = input("Þessi borg er ekki í listanum, viltu bæta henni við? (J eða N)")
    if svar.lower() == 'j':
        hofudborgir.append(inntak)

print("Við eigum eftirfarandi borgir á lista:")
print(hofudborgir)
