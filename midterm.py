print("Welcome to ABC Bank ATM")

password = 1234
balance = 1080.50
attempt = 0

while attempt <= 3:
    pEntry = eval(input("Please enter your 4 digit pin:"))

    if pEntry == password:
        break
    else:
        print("Incorrect Password")
        attempt += 1

if attempt == 3:
    print("No more tries")
else:
    print("Please Press 1 for Checking Balance")
    print("Please Press 2 To Make Withdrawal")
    choice = eval(input("What would you like to choose?"))

    while True:
        if choice == 1:
            print("Your balance is:", balance)
            break
        elif choice ==2:
            while True:
                amount = eval(input("Enter withdrawal amount:"))
                if amount == 50 or amount == 100 or amount == 200 or amount == 500 or amount == 1000 or amount == 1500:
                    break
                else:
                    print("Invalid entry")

            if amount > balance:
                print("INSUFFICIENT BALANCE")
                break
            else:
                print("Your balance is now:", balance-amount)
                break

        else:
            print("Invalid entry")