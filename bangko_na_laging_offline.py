from turtle import clear
newBalance = 0.00
balance = 1000.00
chances = 0
print('Welcome to Banko na laging offline!\n')
while chances < 3:
    print('Enter 4-digit PIN: ')
    chances = chances + 1
    pin = input()
    if pin == '1234':
        print('Press 1 to Check Balance.')
        print('Press 2 to Quit')
        print('Press 3 to Deposit Cash')
        print('Press 4 to Withdraw Cash')
        menu = input()
        if menu == '1':
            print('Your Balance is ' , balance)
        elif menu == '2':
            print('Thank you for banking with us!')
            exit()
        elif menu == '3':
            print('How much would you like to deposit?')
            cashDeposit = input()
            print('Deposit ' , cashDeposit , '. Confirm?')
            prompt = input()
            if prompt == 'y':
                newBalance = float(balance) + float(cashDeposit)
                print('Your new balance is ' , newBalance)
        elif menu == '4':
            print('How much would you like to withdraw?')
            cashWithdraw = input()
            print('Withdraw' , cashWithdraw , '?')
            prompt = input()
            if prompt == 'y':
                if float(balance) < float(cashWithdraw):
                    print('Insufficient balance.')
                else:
                    newBalance = float(balance) - float(cashWithdraw)
                    print('Your new balance is ' , newBalance)
        else:
            print('Please enter the correct number!')
        break
    elif chances == 3:
        print('You have exceeded the maximum attempts. Closing.')
        from time import sleep
        sleep(3)
    else:
        print('Incorrect PIN! Please try again.')
        print('Attempts: ' + str(chances) + '\n')