string = "Hello, how are you 123"

"""
# a
print(len(string))

# b

print(string*10)

# c
print(string[0])

# d
print(string[:3])

# e
print(string[-3:])

# f
print(string[::-1])

# g
str = input("Input a string:")
if len(str) < 7:
    print("The string is not long enough")
else:
    print(str[7])

# h
print(string[1:-1])

# i
print(string.upper())

# j
print(string.replace('a','e'))
"""

# k
for i in range(len(string)):
    if not string[i].isalpha():
        print(string[i], end=" ")
