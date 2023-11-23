def summa(tala1, tala2):
    try:
        return tala1+tala2
    except TypeError:
        return "Villa: breyturnar þurfa að vera af gerðum sem hægt er að leggja saman"

tala3 = summa(1,2)
print(tala3)

tala4 = summa("1",2)
print(tala4)
