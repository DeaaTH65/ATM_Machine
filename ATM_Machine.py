users = {
    "hari": 1500.0,
    "maya": 25000.0,
    "shyam": 14000.0,
    "binod": 100000.0,
    "karna": 5000.00
}


def response_message(code):
    """
    This function returns MESSAGE according to CODE.
    """
    messages = {
        "ls": "Login Success",
        "lf": "Login Fail",
        "wc": "Welcome to ** ATM Machine **",
        "nr": "User not registered",
        "sa": "Select Action: CHECK / DEPOSIT / WITHDRAW / EXIT \n",
        "cb": "Your current balance is: ",
        "nb": "You do not have sufficient balance",
        "wd": "Amount has been withdrawn",
        "ad": "Your amount has been added",
        "ex": "Thank you for your time. Visit Again"
    }
    return messages.get(code, "Invalid code")


def checkUser(user):
    """
    This function checks if the user exists in the user's dictionary.
    """
    return user in users


def getCurrentBalance(user):
    """
    This function returns the current balance of the user.
    """
    if checkUser(user):
        return users[user]
    else:
        print(response_message("nr"))


def doWithdraw(user):
    amount = float(input("Enter amount: "))
    current_balance = getCurrentBalance(user)
    if amount > current_balance:
        print(response_message("nb"))
    else:
        current_balance -= amount
        users[user] = current_balance
        print(response_message("wd"))


def doDeposit(user):
    amount = float(input("Enter amount: "))
    current_balance = getCurrentBalance(user)
    print("How much would you like to deposit? Enter Amount:")
    current_balance += amount
    users[user] = current_balance
    print(response_message("ad"))


def userAction(user):
    while True:
        action = input(response_message("sa"))
        if action.upper() == "CHECK":
            print(response_message("cb"), getCurrentBalance(user))
        elif action.upper() == "WITHDRAW":
            doWithdraw(user)
        elif action.upper() == "DEPOSIT":
            doDeposit(user)
        elif action.upper() == "EXIT":
            print(response_message("ex"))
            login()
            return  # Exit the function
        else:
            print("Enter the correct action.")


def login():
    username = input("Enter username: ")
    if checkUser(username):
        print(response_message("ls"))
        print(response_message("wc"))
        userAction(username)
    else:
        print(response_message("lf"))
        print(response_message("nr"))
        login()


login()
