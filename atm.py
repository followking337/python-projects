userDB = "neo"
passwordDB = "123"
balance = 1000


def execute():
    option = int(input(
        """\nHow do you want to proceed?
    1. Deposite
    2. Withdraw
    3. Exit
    your option --> """))
    global balance
    ok, balance = action(option)
    if ok:
        print("Action successfully done...")
        print("New balance:", balance)
    else:
        print("Action not permitted...")
        print("Balance:", balance)


def login():
    print("Welcome")
    user = input("\tuser: ")
    password = input("\tpassword: ")
    return user == userDB and password == passwordDB


def action(option):
    if option == 1:
        amount = int(input("Enter amount to deposit: "))
        return True, balance + amount
    elif option == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            return False, balance
        return True, balance - amount
    elif option == 3:
        quit('Goodbye!!!')
    return False, balance


if login():
    while True:
        execute()
else:
    print("Sorry, user and/or password are incorrect...")

