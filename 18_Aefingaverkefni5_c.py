langhlid = float(input("Sláðu inn lengd á langhlið trapisu: "))
skammhlid = float(input("Sláðu inn lengd á skammhlið trapisu: "))
haed = float(input("Sláðu inn hæð trapisu: "))

area = (langhlid + skammhlid) * haed / 2

print("Flatarmál trapisunnar er: {}".format(area))
