class nemandi:
    def __init__(self,nafn):
        self.nafn = nafn
        self.einkunn = 10

    def __str__(self):
        return "Nemandi: " + self.nafn + ", einkunn: " + str(self.einkunn)

    def haekka_einkunn(self):
        self.einkunn += 10

    def laekka_einkunn(self):
        self.einkunn -= 10

Siggi = nemandi("Siggi")

print(Siggi)
Siggi.haekka_einkunn()
print(Siggi)
Siggi.laekka_einkunn()
print(Siggi)
