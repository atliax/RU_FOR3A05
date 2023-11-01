for i in range(1,9):
    for j in range(1,9):
        if( (i+j) % 2 == 0 ):
            print("H", end=" ")
        else:
            print("S", end=" ")
    print()
