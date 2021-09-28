import random

# Exe 1

while True:
    cm = float(input("Enter a centimeter value:"))

    if cm < 0:
        print("Invalid Value. Try again")
    else:
        break

print("Convert value to inch is ", cm/2.54)

# Exe 2
while True:
    try:
        val = float(input("Enter a value of the temperature:"))
        break
    except ValueError as e:
        print("Only enter numbers")

while True:
    temp = str(input("Choose a temperature unit in Celsius or Fahrenheit: (C/F):"))

    if temp == 'C' or temp == 'F':
        break
    else:
        print("Please try again. Only enter C or F.")

if temp == 'C':
    print("Converted value to Fahrenheit is ", (9/5*(val-32)))
else:
    print("Converted value to Celsius is ", (9/5*val+32))

# Exe 3
while True:
    try:
        Cel = float(input("Enter a value of the Celsius:"))
        break
    except ValueError as e:
        print("Only enter numbers")

if Cel < -273.15:
    print("Invalid temperature because it is below absolute zero.")
elif Cel == -273.15:
    print("Temperature is absolute 0.")
elif -273.15 < Cel < 0:
    print("Temperature is below freezing.")
elif Cel == 0:
    print("Temperature is freezing point.")
elif 0 < Cel < 100:
    print("Temperature is in normal range.")
elif Cel == 100:
    print("Temperature is at boiling point.")
else:
    print("Temperature is above boiling point.")


# Exe 4:
while True:
    try:
        credit = float(input("Enter your credit score:"))
        break
    except ValueError as e:
        print("Only enter numbers")

if credit < 0:
    print("Invalid input")
elif credit <= 23:
    print("Freshman")
elif 24 <= credit <= 53:
    print('Sophomore')
elif 53 <= credit <= 83:
    print("Juniors")
else:
    print("Seniors")

# Exe 5
# if else
num = random.randint(1, 10)

guess = eval(input("Enter your guess between 1 and 10:"))

if guess == num:
    print("You are right")
else:
    print("HA! Noob. The number is ", num, "\n")
