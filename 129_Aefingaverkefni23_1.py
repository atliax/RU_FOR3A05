class hundur:
    def __init__(self, nafn, aldur):
        self.nafn = nafn
        self.aldur = aldur

    def gelt(self):
        print("Voff!")

snati = hundur("Snati", 5)

print(snati)

snati.gelt()
