# User's ATM Machine

users = {
    "hari": 1500.0,
    "maya": 25000.0,
    "shyam": 14000.0,
    "binod": 100000.0,
    "karna": 5000.00
}


# check user from user input in user_dict
def response_message(code):
    """
    This function returns MESSAGE according CODE. HINT: ls/lf/wc/nr
    """
    if code == "ls":
        return "Login Success"
    elif code == "lf":
        return "Login Fail"
    elif code == "wc":
        return "Welcome to ** ATM Machine **"
    elif code == "nr":
        return "User not registered"
    elif code == "sa":
        return "Select Action: CHECK / DEPOSIT / WITHDRAW / EXIT \n"
    elif code == "cb":
        return "Your current balance is: "
    elif code == "nb":
        return "You do not have sufficient balance"
    elif code == "ad":
        return "Your amount has been added"
    elif code == "ex":
        return "Thank you for your time. Visit Again"


def checkUser(user):
    """
    This function takes user as input and return boolean value accordingly
    """
    if user in users:
        return True
    return False


def getCurrentBalance(user):
    """
    This function returns current balance of the user
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
    current_balance -= amount
    data = {user: current_balance}
    users.update(data)  # update() - function of dict

def doDeposit(user):
    amount = float(input("Enter amount: "))
    current_balance = getCurrentBalance(user)
    print("How much would you like to deposit? Enter Amount:")
    current_balance += amount
    data = {user: current_balance}
    users.update(data)  # update() - function of dict


def userAction(user):
    action = input(response_message("sa"))
    if action.upper() == "CHECK":
        print(response_message("cb"), getCurrentBalance(user))
        userAction(user)
    elif action.upper() == "WITHDRAW":
        doWithdraw(user)
        userAction(user)
    elif action.upper() == "DEPOSIT":
        doDeposit(user)
        userAction(user)
    elif action.upper() == "EXIT":
        print(response_message("ex"))
        login()


def login():
    username = input("Enter username: ")
    if checkUser(username):
        print(response_message("wc"))
        userAction(username)
    print(response_message("nr"))
    login()


login()