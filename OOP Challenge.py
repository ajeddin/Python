# Bank Account with 2 Attributes & 2 Methods
# Owner & Balance
# Deposit & Withdraw


def create_bank():
    print('Welcome to Cyprus National Bank')
    name = ''
    balance=''
    nametrue=False
    balancefalse=False
    while nametrue == False:
        name = input("Start with your name: ")
        if name.replace(" ","").isalpha()==False:
            print('Your name should not include numbers, right?')
        else:
            name = name.title()
            nametrue=True
    while balancefalse == False:
        balance= input('How much money do you want to deposit today: ')
        if balance.isdigit() == False:
            print("Only insert digits")
        else:
            balancefalse=True
        
    return (name,int(balance))

(x,y)=create_bank()


class Bank():
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,dep_amt):
        balance = balance+ dep_amt
        print(f"Added {dep_amt} to balance")
    def withdraw(self,with_amt):
        if self.balance >= with_amt:
            self.balance= self.balance-with_amt
            print(f"Withdrawal Accepted\nCurrent Balance: {self.balance}")
        else:
            print('Sorry not enough funds!')
    def __str__(self):
        return f'Owner:  {self.owner}\nBalance: {self.balance} '
a = Bank(x, y)
# print(str(a))
def func():
    amount= 0
    withd=False
    depositd=False
    mychoice = ''
    choices= ['D','W']
    
    print(f'Owner:  {a.owner}\nBalance: {a.balance} ')
    while withd == False and depositd==False:
        mychoice= input('Do you want to deposit or withdraw from your account? (D or W) ' ) 
        if  mychoice not in choices:
            print('(D or W)')
        while mychoice == 'D':
            depositd= True
            amount= str(input('How much money do you want to deposit? '))
            if amount.isdigit()==False:
                print('Please enter number')
            else:
                amount = int(amount)
                a.balance=a.balance+amount
                print(f'Added to Balance\nCurrent Balance: {a.balance}')
                break
        while mychoice == 'W':
            withd= True
            print('Current Balance: {}'.format(a.balance))
            amount= str(input(f'How much money do you want to withdraw? '))
            if amount.isdigit()==False:
                print('Please enter number')
            elif int(amount) > a.balance:
                print(f"Has to be under {a.balance}")
            else:
                amount = int(amount)
                a.balance=a.balance-amount
                print(f'Withdrew from balance\nCurrent Balance: {a.balance}')
                break
func()
againtwo = False

def again():
    againtwo = False
    choice=''
    choices = ['Y','N']
    while againtwo==False:
        choice= input('Do you want to deposit or withdraw again? (Y or N) ')
        if choice not in choices:
            print('(Y or N)')
        elif choice == 'Y':
            func()
        else:
            print('Thanks for using Cyrpus National Bank\nSee you later')
            break
again()
# money = int(input("How much would you like to withdraw from your account? "))
# a.withdraw(money)