import math
from math import *

# Exe 1
count = int(0)

for i in range(1, 101):
    if (i**2) % 10 == 1:
        print(i, end=" ")
        count += 1

print("\nThe total count is ", count)

# Exe 2
count4 = 0
count9 = 0

for i in range(1, 101):
    if (i**2) % 10 == 4:
        count4 += 1

    if (i**2) % 10 == 9:
        count9 += 1

print("\nTotal number ends in 4:", count4)
print("Total number ends in 9:", count9)

print()

# Exe 3
n = eval(input("Enter a number for n:"))
n1 = 0
result = 0

for i in range(2, n+1):
    n1 += 1/i

result = (1 + n1) - log(n)
print(round(result, 3))

print()

# Exe 4
odd = 0
even = 0

for i in range(1, 2000):
    if i % 2 == 0:
        odd += i
    else:
        even += i

result = odd-even
print("The final sum is:", result)

print()
# Exe 5
