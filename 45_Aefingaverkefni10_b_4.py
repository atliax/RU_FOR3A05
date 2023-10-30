tala1 = int(input("Sláðu inn tölu: "))
tala2 = int(input("Sláðu inn aðra tölu: "))

beast = 666

if (tala1 == beast) or \
   (tala2 == beast) or \
   (tala1 + tala2 == beast) or \
   (tala1 - tala2 == beast) or \
   (tala2 - tala1 == beast):
    print("Merki dýrsins!")
else:
    print("Ekkert merkilegt, því miður.")
