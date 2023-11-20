with open("data/SV1.txt", 'r') as file:
    with open("data/SV1_lagað.txt", 'w') as file_fix:
        file_fix.write(file.read().replace("\n", "").replace(" ", ""))
