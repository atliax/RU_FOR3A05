"""
--------------------------------------------------------------------------------

Check Yourself bls. 160 (More Control Check)

3

0

4

1

iv

--------------------------------------------------------------------------------

number_str = input("Enter an int: ")
number = int(number_str)
count = 0

while number > 0:
    if number % 2 == 0:
        number = number // 2
    elif number % 3 == 0:
        number = number // 3
    else:
        number = number - 1
    count = count + 1

print("Count is: ", count)
print("Number is: ", number)

--------------------------------------------------------------------------------

Check Yourself bls. 173 (for and range Check)

--------------------------------------------------------------------------------

the_max = int(input("Upper: "))
the_sum = 0
extra = 0

for number in range(1,the_max):
    if number%2 and not number%3:
        the_sum = the_sum + number
    else:
        extra = extra + 1

print(the_sum)
print(extra)

--------------------------------------------------------------------------------
"""