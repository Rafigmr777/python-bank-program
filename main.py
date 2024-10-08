def withdrawl():
    print('Option 1: Withdrawal selected')

def show_balance():
    print('Option 2: Show Balance selected')

def deposit():
    print('Option 3: Deposit selected')

is_running = True

while is_running:
    print('Enter the banking option:')
    print("Press 1 for withdrawal")
    print("Press 2 for show balance")
    print("Press 3 for deposit")
    print("Press 4 for exit")

    choice = input("Please enter option type: ")

    if choice == '1':
        withdrawl()
    elif choice == '2':
        show_balance()
    elif choice == '3':
        deposit()
    elif choice == '4':
        is_running = False
    else:
        print('Please enter a valid number between 1 to 4')

print('Thanks')
