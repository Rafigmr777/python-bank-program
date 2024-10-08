def withdrawl(balance):
    #print('Option 1: Withdrawal selected')
    #print(f"Please")
    print('**************************')
    amount = float(input("Please enter the amount to withdraw"))
    if amount > balance:
        print('**************************')
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print('**************************')
        print("Please enter a valid number")
        return 0
    else:
        print('**************************')
        print (f"withdraw is successfull for the sum of ${amount:.2f}")
        return amount
def show_balance(balance):
    #print('Option 2: Show Balance selected')
    print('**************************')
    print(f"Your current balance is ${balance:.2f}")
    #return balance
def deposit():
    #print('Option 3: Deposit selected')
    print('**************************')
    sum = float(input("Please enter the amount to be deposited:"))
    if sum < 0:
        print('**************************')
        print('Please enter valid amount')
        return 0
    else:
        print('**************************')
        print(f"your sum of ${sum:.2f} is deposited successfully ")
        return sum

def main():
    balance = 0
    is_running = True

    while is_running:
        print('**************************')
        print('     Banking options     ')
        print("Press 1 for withdrawal")
        print("Press 2 for show balance")
        print("Press 3 for deposit")
        print("Press 4 for exit")
        print('**************************')

        choice = input("Please enter option type: ")

        if choice == '1':
            balance -= withdrawl(balance)
        elif choice == '2':
            show_balance(balance)
        elif choice == '3':
            balance += deposit()
        elif choice == '4':
            is_running = False
        else:
            print('**************************')
            print('Please enter a valid number between 1 to 4')
    print('**************************')
    print('Thank you for the banking')
    print('**************************')


if __name__ == '__main__':
    main()

