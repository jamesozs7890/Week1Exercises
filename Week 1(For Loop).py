# Q7
for i in range(9):
    print("A", end="")

for i in range(7):
    print("B", end="")

for i in range(4):
    print("C", end="")
    print("D", end="")

print("E", end="")

for i in range(6):
    print("F", end="")

print("G", end="\n\n")

# Fibonacci
print("Fibonacci Program")

while True:
    try:
        n = int(input("Enter the number of elements to be printed:"))
        break
    except ValueError as e:
        print("Ony accept integer value.")

x = int(0)
y = int(1)
z = x + y

for i in range(n):

    if i == 0:
        print(x, y, sep=",", end=",")
    else:
        if i == n - 1:
            print(z)
        else:
            print(z, end=",")

        x = y
        y = z
        z = x + y
