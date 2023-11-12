x = 3
y = 3

leikbord = [[0] * y for _ in range(x)]

for i in range(0,x):
    for j in range(0,y):
        if (i+j) % 2 == 0:
            leikbord[i][j] = "X"
        else:
            leikbord[i][j] = "O"

for i in range(0,x):
    for j in range(0,y):
        print(leikbord[i][j],end="")
    print()
