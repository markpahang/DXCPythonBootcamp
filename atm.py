print('Welcome to Jalton ATM Bank Phils')
restart=('Y')
chances = 3
balance = 1000.00
while chances >= 0:
    pin = int(input('\nPlease Enter You 4 Digit Pin: '))
    if pin == (1234):
        print('Pin Verified!\n')
        while restart not in ('n','NO','no','N'):
            print('************* MENU *************\n')
            print('Please Type 1 Check Your Balance\n')
            print('Please Type 2 To Make a Withdrawal\n')
            print('Please Type 3 To Deposit Money\n')
            print('Please Type 4 To Quit \n')
            option = int(input('What Would you like to choose? = '))
            if option == 1:
                print('Your Balance is ₱',balance,'\n')
                restart = input('Would You you like to go back to the menu? Type y for yes and n for no: ')
                if restart in ('n','NO','no','N'):
                    print('Thank you for choosing Jalton Bank')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How Much Would you like to withdraw? ₱10 ₱20 ₱40 ₱60 ₱80 ₱100 for other enter 1: '))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawl
                    print ('\nYour Balance is now ₱',balance)
                    restart = input('Would You you like to go back to the menu? Type y for yes and n for no: ')
                    if restart in ('n','NO','no','N'):
                        print('Thank you for choosing Jalton Bank')
                        break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print('Invalid Amount, Please Re-try\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('Please Enter Desired amount:'))    

            elif option == 3:
                Pay_in = float(input('How Much Would You Like To Pay In? '))
                balance = balance + Pay_in
                print ('\nYour Balance is now ₱',balance)
                restart = input('Would You you like to go back to the menu? Type y for yes and n for no: ')
                if restart in ('n','NO','no','N'):
                    print('Thank you for choosing Jalton Bank')
                    break
            elif option == 4:
                print('Please wait whilst your card is Returned...\n')
                print('Thank you for you service')
                break
            else:
                print('Please Enter a correct number. \n')
                restart = ('y')
    elif pin != ('1234'):
        print('Incorrect Pin')
        chances = chances - 1
        if chances == 0:
            print('3 Attempts Alert, No more tries')
            break