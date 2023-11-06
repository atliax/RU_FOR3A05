def area_of_rectangle(length, height):
    return length * height

lengd = int(input("Sláðu inn lengd á rétthyrningi: "))
haed = int(input("Sláðu inn hæð á rétthyrningi: "))

flatarmal = area_of_rectangle(lengd,haed)

print("Flatarmál rétthyrnings með lengd {} og hæð {} er: {}".format(lengd,haed,flatarmal))
