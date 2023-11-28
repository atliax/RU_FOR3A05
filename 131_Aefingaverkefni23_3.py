class ferhyrningur:
    def __init__(self, lengd, breidd):
        self.lengd = lengd
        self.breidd = breidd
    
    def __str__(self):
        return "Lengd: " + str(self.lengd) + ", breidd: " + str(self.breidd)
    
    def flatarmal(self):
        return self.lengd * self.breidd

    def ummal(self):
        return 2*self.lengd + 2*self.breidd

kassi1 = ferhyrningur(2.0, 3.0)
print(kassi1)
print(f"Flatarmál kassa 1: {kassi1.flatarmal()}")
print(f"Ummál kassa 1: {kassi1.ummal()}")
print()

kassi2 = ferhyrningur(20.0, 15.0)
print(kassi2)
print(f"Flatarmál kassa 2: {kassi2.flatarmal()}")
print(f"Ummál kassa 2: {kassi2.ummal()}")
