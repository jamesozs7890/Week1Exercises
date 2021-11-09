from random import randint

# 2

aNum = []

for i in range(20):
    aNum.append(randint(1, 100))

# a
print(aNum)


# b
print("Average:", sum(aNum)/20)

# c
print("Max:", max(aNum))
print("Min", min(aNum))

# d
aNum.sort()

print("Sorted:", aNum)

print("Second largest:", aNum[-2])
print("Second smallest", aNum[1])

# e
count = 0

for i in range(20):
    if aNum[i] % 2 == 0:
        count += 1

print("Even number:", count)

# 3

# 4
L = []

for i in range(12):
    entry = eval(input("Enter any numbers:"))

    if entry > 10:
        entry = 10

    L.append(entry)

print(L)
