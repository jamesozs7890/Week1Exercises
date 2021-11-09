"""password = 'abcde'

attempt = 5

while attempt > 0:
    entry = input("Please enter your password:")

    if entry != 'abcde':
        attempt -= 1
        print("Try Again")
    else:
        print("You have gotten the correct password")
        break

if attempt == 0:
    print("Sorry, you have been kicked off the system")"""


#MUST REMEMBER CLOSING BRACKETS


while True:
    userAcc = input("Enter your account ID:")

    if len(userAcc) == 10: #remember check length is len(variable) not variable.len
        break
    else:
        print("Invalid user account ID. Please try again.")

attempt = 3
password = 'abcde'

while attempt > 0:
    userPass = input("Please enter your password:")
    if userPass != password:
        attempt -= 1
        print("Wrong password. Please try again.", attempt, " attempts left.")
    else:
        print("Logging in")
        break

if attempt == 0:
    print("Your account is frozen because of too many failed attempted passwords")
else:
    recpName = input("Enter recipient's name:")

    while True:
        bankName = input('Enter the recipient bank name:')
        bankName = bankName.upper() #Remember upper got bracket
        print(bankName)

        if bankName == 'CIMB' or bankName == 'MBB' or bankName == 'PBB': #Remember string
            break
        else:
            print("Invalid bank name. Please try again. Available bank: CIMB, MBB, PBB")

    while True:
        recipientAcc = input("Enter recipient account number:")
        if len(recipientAcc) == 10:
            break
        else:
            print("Invalid user account ID. Please try again.")

    amount = eval(input("Enter the amount to transfer: RM"))

    print("Transfer is successful")
    print("Recipient Name:", recpName)

    print("Recipient Account Number:", recipientAcc)

    print("Total amount: RM", round(amount, 2))
