from random import randint

"""L = eval(input("Enter anything"))

for i in range(len(L)):
    print(L[i])"""

#finding min and max
a = [1,2,3,4]

print(min(a))
print(max(a))

# sum list

b = [5,6,7,8]

print(a+b)

# append
a.append(9)
print(a)

x = 12
a.append(x)
print(a)

# test
a = ['a','b','c','b']
b = [1,2,3,2,3,2,5,6]

print(a.count('b'))

print(b.count(2))

# index
print(a.index('b'))

# reverse
a.reverse()
print(a)

# remove
b.remove(2)
print(b)

# pop
a.pop(1)
print(a)

#clear
a.clear()
print(a)

#copy
a = [1,2,3,4,5]
b = a

b[1] = 9

print(a)
print(b)
print("a is affected too")

# to avoid a getting affected
a=[1,2,3,4,5] #original list
b=a[:]
b[1]=9
print(a)
print(b)

a=[1,2,3,4,5] #original list
b=a.copy()
b[1]=8
print(a)
print(b)

# rand list
L = []
count = 0

for i in range(10):
    L = L + [randint(1,100)]

    if L[i] > 50:
        count += 1

print("There are", count, " numbers larger than 50 in ", L)

# Frequencies
L=[1,2,3,3,7,7,9,3]
frequencies = []
for i in range(1,11):
    frequencies.append(L.count(i))

print(frequencies)

# Example
questions = ['What is the capital of France?', 'Which state has only one neighbor?']
answers = ['Paris','Maine']

num_right = 0
for i in range(len(questions)):
    guess = input(questions[i])
    if guess.lower()==answers[i].lower():
        print('Correct')
        num_right=num_right+1
    else:
        print('Wrong. The answer is', answers[i])
        print('You have', num_right, 'out of', i+1, 'right.')