x = 3
y = 3

leikbord = []

for i in range(0,x):
    tmp = []
    for j in range(0,y):
        if(i+j) % 2 == 0:
            tmp.append("X")
        else:
            tmp.append("O")
    leikbord.append(tmp)

for i in range(0,x):
    for j in range(0,y):
        print(leikbord[i][j],end="")
    print()
