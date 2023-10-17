weight = float(input("Sláðu inn þyngd í kílógrömmum: "))
height = float(input("Sláðu inn hæð í metrum: "))
BMI = weight / height**2

print("Einstaklingur sem er {0}cm á hæð og {1}kg er með BMI {2}.".format(weight,height,round(BMI,4)))
