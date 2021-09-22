# Exercise 1
print("Exercise 1")
x = ('*******************')
i = 0

while i < 4:
    print(x)
    i += 1

print("")

# Exercise 2
print("Exercise 2")
print ("""*******************
*                 *
*                 *
*******************""", end= '\n\n')

# Exercise 3
print("Exercise 3")
print("""*
**
***
****""")

# Exercise 4
numerator = int(512-282)
denominator = int(47*48+5)

x = round(numerator/denominator, 4)

print(x, end='\n\n')

# Exercise 5
print("Exercise 5")
num = eval(input("Enter a number:"))

print('The square of ', num, 'is ', (num ** 2), end="\n\n")

# Exercise 6
print("Exercise 6")
num1 = eval(input("Enter a number:"))

print(num1, num1*2, num1*3, num1*4, num1*5, sep="---", end="\n\n")

# Exercise 7
print("Exercise 7")
kg = eval(input("Your weight in kg:"))
pound = kg*2.2
print("Your weight in pound is", round(pound, 2), end="\n\n")

# Exercise 8
print("Exercise 8")
print("Key in 3 numbers:")

x = float(input("N1:"))
y = float(input("N2:"))
z = float(input("N3:"))

total = x + y + z
average = (x + y + z)/3

print("The total is ", total, "and the average is ", round(average, 4), end="\n\n")

# Exercise 9
print("Exercise 9")

bill = eval(input("Amount of bill $"))
percent = eval(input("Tip percents %"))

tip = bill * (percent/100)
print("The tip amount is", tip, ".\nHence the total bill is ", (tip+bill), end=".")




