userDB = "neo"
passwordDB = "123"
balance = 1000


def login():
    print("Welcome")
    user = input("\tuser: ")
    password = input("\tpassword: ")
    return check(user, password)


def check(user, password):
    return user == userDB and password == passwordDB


def action(option):
    if option == 1:
        amount = int(input("Enter amount to deposit: "))
        return deposite(amount)
    elif option == 2:
        amount = int(input("Enter amount to withdraw: "))
        return withdraw(amount)
    return False, balance


def deposite(amount):
    return True, balance + amount


def withdraw(amount):
    if amount > balance:
        return False, balance
    return True, balance - amount


def execute():
    if not login():
        print("Sorry, user or password incorrect")
        return
    print("How do you want to proceed?")
    option = int(input("1. Deposite o 2. Withdraw "))
    ok, new_balance = action(option)
    if ok:
        print("Action successfully done...")
        print("New balance:", new_balance)
    else:
        print("Action not permitted, saldo:")
        print("New balance:", new_balance)


execute()
