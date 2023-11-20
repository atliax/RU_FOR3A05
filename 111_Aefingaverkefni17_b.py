filename = "data/SV2.txt"
filename_fix = "data/SV2_lagað.txt"

innihald = []

with open(filename, 'r') as file:
    innihald = file.read().split(", ")

with open(filename_fix, 'w') as file_fix:
    for nafn in innihald:
        file_fix.write(nafn+"\n")
