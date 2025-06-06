import sys


class Banking:
    bank_name = "AB Bank"

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        self.balance = self.balance + amt
        print('After Deposit Available balance is:', self.balance)

    def withdraw(self, amt):
        if amt > self.balance:
            print('Insufficient Balance...Cannot perform this action')
            sys.exit()
        else:
            self.balance = self.balance - amt
            print('After Withdraw Balance is: ', self.balance)


print('Welcome to',Banking.bank_name)
name = input('Enter Your Name: ')
c = Banking(name)
while True:
    count = 0
    print('Choose your option\nd-Deposit\nw-Withdraw\ne-Exit')
    choice = input('Enter your choice: ')
    if choice == 'd':
        amt = float(input('Enter the amount to deposit: '))
        c.deposit(amt)
    elif choice == 'w':
        amt = float(input('Enter the amount to withdraw: '))
        c.withdraw(amt)
    elif choice == 'e':
        print('Thanks for Banking')
        sys.exit()
    else:
        print('Choose valid option')




