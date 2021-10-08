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

# Exe 6
print("Less than 10 items = $12 each \nMore than 10, less than 99 items = $10 each \nMore than 99 items = $7 each")
quantity = eval(input("How many items do you want to buy?"))
total = float()

if quantity < 10:
    total = 12*quantity
elif 10 <= quantity < 99:
    total = 10*quantity
elif quantity > 99:
    total = 7*quantity

print("Total cost= $", total)


# Exe 8
year = eval(input("Write down a year:"))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")
else:
    print("Not leap year")


# Exe 12
candy = int()

for i in range(200):
    if (i % 5 == 2 and i % 6 == 3 and i % 7 == 2) == False:
        candy != i
    else:
        candy = i
        print(candy)

# Exe 13
cs = int(0)
ps = int(0)

for i in range(5):
    comp = random.randint(1, 3)
    player = eval(input("Enter 1- Rock | 2- Paper | 3- Scissor:"))

    if comp == 1:
        print(" Computer: Rock", end=" | ")
    elif comp == 2:
        print("Computer : Paper", end=" | ")
    else:
        print('Computer : Scissors', end=" | ")

    if player == 1:
        print("Player: Rock")
    elif player ==2:
        print("Player: Paper")
    else:
        print("Player: Scissors")

    if (comp == 1 and player == 1) or (comp == 2 and player== 2) or (comp == 3 and player == 3):
        print("Draw \n")
        cs = ps = 0
    elif (comp == 1 and player == 3) or (comp == 2 and player == 1) or (comp == 3 and player == 2):
        print("Computer + 1\n")
        cs += 1
    elif (comp == 1 and player == 2) or (comp == 2 and player == 3) or (comp == 3 and player == 1):
        print("Player + 1\n")
        ps += 1

if ps == cs:
    print("Draw")
elif ps > cs:
    print('Player has won')
elif cs > ps:
    print("Computer has won")

# Example
count = 0

for i in range(1, 51):

    if (i ** 2) % 10 == 4:

        count = count + 1

print(count)
