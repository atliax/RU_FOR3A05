def saekja_heiltolu(strengur):
    heiltala_komin = False
    while not heiltala_komin:
        try:
            tala = int(input(strengur))
            heiltala_komin = True
        except ValueError:
            print("Þetta skilst ekki sem heiltala, reyndu aftur...")
    return tala

artal = saekja_heiltolu("Sláðu inn ártal:")

if(artal % 1000 == 0):
    print("Þarna byrjaði nýtt árþúsund!")
elif(artal % 100 == 0):
    print("Þarna byrjaði ný öld!")
elif(artal == 1964):
    print("Þarna byrjaði saga HR!")
else:
    print("Ósköp venjulegt ár þarna á ferð!")
