filename = "data/SV2_lagað.txt"
filename_eftirnofn = "data/eftirnöfn.txt"

nofn = []
talning = 0

with open(filename, 'r') as file:
    with open(filename_eftirnofn, 'w') as file_eftirnofn:
        for line in file:
            talning += 1
            eftirnafn = line.split(" ")[1].strip("\n")
            file_eftirnofn.write(f"Nemandi {talning}: {eftirnafn}\n")
