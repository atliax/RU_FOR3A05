line = int(input("Hvaða línu í margföldunartöflunni viltu sjá? "))

print("{0} sinnum tafla: ".format(line), end='')

for i in range(1,11):
    print("{0} ".format(i*line), end='')

print('')
