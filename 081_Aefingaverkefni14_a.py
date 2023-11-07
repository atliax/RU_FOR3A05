def margfoldunartafla_lina(lina):
    for n in range(1,11):
        print(lina*n, end="\t")
    print()

tala = int(input("Hvaða línu á að prenta út? "))

margfoldunartafla_lina(tala)
