def er_tala_i_dict(tala, ordabok):
    for key,value in ordabok.items():
        if tala == key:
            return True
    return False

dict1 = { 1:2, 2:3, 3:4, 5:5, 6:6 }

for i in range(1,11):
    if er_tala_i_dict(i,dict1):
        print(f"Talan {i} er til sem lykill í orðabókinni.")
    else:
        print(f"Talan {i} er ekki til sem lykill í orðabókinni.")
