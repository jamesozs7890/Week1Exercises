# Q2
sen = input("Enter a sentence:")
wCount = 0

for i in range(len(sen.rstrip())):
    if sen[i] == " ":
        wCount += 1

print("Word Count = ", wCount+1)

# Q3


# Q4
word = input("Enter a word:")

count = 0

for i in range(len(word)):
    if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u':
        count += 1

print("There are", count, "vowels in", word, end="\n")

# Reverse a word & Q7
a = input("Enter a word:")
rev = a[::-1]

print(rev)

if a.lower() == rev.lower():
    print("Palindrome = True")
else:
    print("Palindrome = False")