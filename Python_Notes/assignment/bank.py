import random

users = []

class Bank:
    b_name = "State bank of India"
    ifsc = "SBIN008901"
    __bank_balance = 999999999

    def __init__(self, name, phn_no, email, dob, username, password, acc_no, bal=0, loan_amt=0):
        self.name = name
        self.phn_no = phn_no
        self.email = email
        self.dob = dob
        self.username = username
        self.password = password
        self.acc_no = acc_no
        self.bal = bal
        self.loan_amt = loan_amt
    
    def deposit(self,amount):
        if amount<0:
            print("Check the value entered")
            return
        if self.loan_amt > 0:
            if amount >= self.loan_amt:
                amount -= self.loan_amt
                Bank.__bank_balance +=self.loan_amt
                print(f"Loan of {self.loan_amt} paid")
                self.loan_amt = 0
            else:
                self.loan_amt -+ amount
                Bank.__bank_balance += amount
                print(f"Partial loan paid of {amount}. Remaining loan is: {self.loan_amt} ")
                return
        self.bal += amount
        Bank.__bank_balance += amount
        print(f"Deposited: {amount} and New balance is {self.bal}")

    def withdraw(self,amount):
        if amount <= 0:
            print("Withdrawl amount should be more then Zero(0)")
            return
        if amount <= self.bal:
            self.bal -= amount
            Bank.__bank_balance -= amount
            print(f"Withdraw amount is {amount} and remaining balance is {self.bal}")
        else:
            choice = input(f"Insufficient balance. Do you want to take loan of {amount-self.bal}? (y/n):  ")
            if choice.lower()=="y":
                self.loan_amt = amount - self.bal
                self.bal = 0
                Bank.__bank_balance -= amount
                print(f"Withdrawn {amount} Loan taken {self.loan_amt} and remaining balance is {self.bal}")
            else:
                print("Withdrawl cancelled")

    def show_bal(self):
        print(f"Current balance is {self.bal} and loan amount is {self.loan_amt}")

    def show_acc_no(self):
        print(f"Your account number is {self.acc_no}")

def generate_unique_acc_no():
    while True:
        acc_no = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        if all(user.acc_no != acc_no for user in users):
            return acc_no
        
def register():
    name = input("Enter you name: ").strip()
    if not name :
        print("Name is mandatory.")
        return
    email = input("Enter your Email (optional): ").strip()
    phn_no = int(input("Enter you Phone number: "))
    if not phn_no:
        print("Phone number is mandatory: ")
        return
    dob = input("Enter your Date of birth (DD-MM-YY): ").strip()
    if not dob:
        print("Date of birth is mandatory")
        return
    username = input("Enter your username: ").strip().lower()
    if not username:
        print("username is mandatory")
        return
    password = input("Enter your password: ").strip()
    if not password:
        print("Password is mandatory")
        return
    acc_no = generate_unique_acc_no()
    user = Bank(name, email, phn_no, dob, username, password, acc_no)
    users.append(user)
    print(f"User registered and account created Sucessfully!")
    print(f"Your username is {username} and Account numaber is {acc_no}")
    print("Thank you! for choosing our banking services")

def signin():
    username = input("Enter your username: ").strip().lower()
    password = input("Enter your password: ").strip()
    for user in users:
        if user.username == username and user.password == password:
            print(f"Welcome, {user.name}!")
            return user
    print("Invalid username or password.")
    return None


user1 = Bank("Shohrat",'shohrat@001',1987654321,"01-01-01","shohrat123", "1234", generate_unique_acc_no(), bal = 101)
users.append(user1)

while True:
    choice = input(f"Welcome to {Bank.b_name}\n1. Register\n2. Sign in\n3. Exit\nEnter your choice: ")
    if choice == "1":
        register()
    elif choice == "2":
        user = signin()
        if user:
            while True:
                action = input("\n1. Deposit\n2. Withdraw\n3. Show Balance\n4. Show Account Number\n5. Logout\nEnter your choice: ")
                if action == "1":
                    amount = float(input("Enter amount to deposit: "))
                    user.deposit(amount)
                elif action == "2":
                    amount = float(input("Enter amount to withdraw: "))
                    user.withdraw(amount)
                elif action == "3":
                    user.show_bal()
                elif action == "4":
                    user.show_acc_no()
                elif action == "5":
                    break
                else:
                    print("Invalid choice.")
    elif choice == "3":
        print("Thank you for using our banking system!")
        break
    else:
        print("Invalid choice. Please try again.")
