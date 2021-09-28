"""import math
import random

print(math.floor(30.2))
print(math.ceil(30.1))

print(round(5678.1231, -1))
print(round(5678.1231, -2))
print(round(5478.1231, -3), end="\n\n")

x = random.randint(1,10)

print("A random number: ", x)

y = random.randrange(5, 30, 5)
print("Multiple of 5:", y)

# 3.8 Exercise
# Exe 1
for i in range(50):
    print(random.randint(3, 6), end=" ")

print("\n")

# Exe 2
x = random.randint(1, 50)
y = random.randint(2, 5)


print("x:", x, "\ny:", y, "\nx^y=", x**y)

# Exe 3


# Exe 4
print(round(random.uniform(1, 10), 2),end="\n\n")

# Exe 5
for i in range(50):
    print(random.randint(1, i+2), end=" ")

print("\n")

# Exe 6
x = (eval(input("Enter a number for x:")))
y = (eval(input("Enter a number for y:")))

print("The value for |x-y|/x+y =", (abs(x-y))/(x+y),end="\n\n")


# Exe 7
while True:
    try:
        angle = int(input("Enter an angle between -180 and 180:"))
        break
    except ValueError as e:
        print("Ony accept integer value.")

if -180 <= angle < 0:
    print("The equivalent for ", angle, " is ", angle+360)
elif angle < -180:
    print("Invalid input.")
elif angle > 180:
    print("Invalid input.")
else:
    print("You have entered ", angle)

print("\n")

# Exe 8
while True:
    try:
        sec = int(input("Enter the number of second:"))
        break
    except ValueError as e:
        print("Ony accept integer value.")


print("Converted value to 'min : sec' is ", abs(sec)//60, " : ", abs(sec) % 60)"""

# Exe 9
while True:
    hour = int(input("Enter current hour between 1 and 12:"))

    if hour < 0 or hour > 12:
        print("Try again")
    else:
        break

ahead = int(input("Enter the total hours ahead:"))

newHour = int(hour + ahead)

if newHour > 12:
    newHour -= 12

print("New hour = ", newHour, "o'clock\n")

# Exe 10 a b
num = int(input("Enter the value of power:"))

powered = 2**num
print("2 to the power of ", num, " is ", powered)
print("The last digit of 2 to the power of ", num, " is ", powered % 10)
print("The last 2 digits to the power of ", num, " is ", powered % 100, end="\n\n")

# Exe 10 c
num = int(input("Enter the value of power:"))
digits = int(input("Number of last digits to be displayed:"))

powered = 2**num

print("2 to the power of ", num, " is ", powered)
print("The last", digits, "digit of 2 to the power of ", num, " is ", powered % (10**digits))

# Exe 11
kg = float(input("Input your weight in kg:"))

print("Your weight in pound(lbs) is ", round(kg*2.220, 2), "lbs")
