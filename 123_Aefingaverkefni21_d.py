prufudict = {
    10:1,
    20:2,
    30:3,
    40:4,
    50:5
}

summa = 0

for key,value in prufudict.items():
    summa += value

print(prufudict)
print(f"Summa lyklanna er: {summa}.")
