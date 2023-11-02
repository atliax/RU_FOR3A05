price = int(input("Sláðu inn verð: "))
price_VAT = price * 1.255

print("{0} kr. með 25.5% VSK verður {1} kr.".format(price,round(price_VAT,2)))
