# import math
# import random

"""
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

# if else
num = random.randint(1, 10)

guess = eval(input("Enter your guess between 1 and 10:"))

if guess == num:
    print("You are right")
else:
    print("HA! Noob. The number is ", num)

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


print("Converted value to 'min : sec' is ", abs(sec)//60, " : ", abs(sec) % 60)
"""

# Exe 9
while True:
    try:
        hour = int(input("Enter current hour between 1 and 12:"))
        break
    except ValueError as e:
        print("Ony accept integer value.")
