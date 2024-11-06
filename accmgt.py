
running = True
accounts = {
    "name":[],
    "number":[],
    "balance": [],
    "phoneno": [],
    "pin": []
}

def readInputInt(message):
    try:
        userInput = int(input(message))
        if str(userInput).isnumeric():
            return userInput
        else:
            print("Name should not have a number")
            readInputInt(message)
    except:
        print("please input a number")
        readInputInt(message)

def readInput(message):
    try:
        userInput = input(message)
        return userInput
    except:
        print("please input as directed")
        readInput(message)


def readInputAlpha(message):
 
        try:
            userInput = input(message)
            if userInput.isalpha():
                return userInput
            else:
                print("Name should not have a number")
                readInputAlpha(message)
        except:
            print("please input a string")
     

    

def createAccount(name, number, balance, phoneno, pin):
    accounts["name"].append(name)
    accounts["number"].append(number)
    accounts["balance"].append(balance)
    accounts["phoneno"].append(phoneno)
    accounts["pin"].append(pin)
        

def options():
    print ("** Account Management System **")
    print("\t1 - Login as Admin")
    print("\t2 - Login as a Customer")
    print("\t3 - Exit")

    userInput = readInputInt("Choose from the options: ")
    return userInput

def admin():
    running = True
    loginGrace = 3
    while loginGrace > 0:
        adminPassword = input("Please input you password: ")
        loginGrace -=1
        if adminPassword == "1234":
            print(" You just logged in as an admin")
        
            while running:
                print("*Administrator*")
                print(" \t 1 - Add account")
                print(" \t 2 - Delete account")
                print(" \t 3 - View account")
                print(" \t 4 - Exit")

                action = readInputInt("Please choose an option: ")
                if action == 1:
                    name = readInputAlpha("Account name: ")
                    number = readInputInt("Account number: ")
                    balance = readInputInt("Account balance: ")
                    phoneno = str(readInputInt("Phone number: "))
                    grace = 3
                    while grace > 0:
                        if len(phoneno) != 11:
                            phoneno = str(readInputInt("Phone number: "))
                            grace -=1
                        elif len(phoneno) == 11: 
                            grace = 0
                            pin = str(readInput("Input 4 digit Pin: "))
                            grace2 = 3
                            while grace2 > 0:
                                if len(pin) != 4:
                                    pin = str(readInput("Input 4 digit Pin: "))
                                    grace2 -=1
                                elif len(pin) == 4:
                                    grace2 = 0
                                    createAccount(name, number, balance,phoneno, pin)
                    print(accounts)

                elif action == 2:
                    delAccount = readInputAlpha("Input the account name: ")
                    if delAccount in accounts["name"]:
                        index = accounts["name"].index(delAccount)
                        del accounts["name"][index]
                        del accounts["number"][index]
                        del accounts["balance"][index]
                        del accounts["phoneno"][index]
                        del accounts["pin"][index]
                elif action == 3:
                    print("name\t\t\tnumber\t\t\tbalance\t\t\tphoneno\t\t\tpin")
                    
                    for i, name in enumerate(accounts["name"]):
                        
                        number = accounts["number"][i]
                        balance = accounts["balance"][i]
                        phoneno = accounts["phoneno"][i]
                        pin = accounts ["pin"][i]

                        print(f"{name}\t\t\t{number}\t\t\t{balance}\t\t\t{phoneno}\t\t\t{pin}")
                elif action == 4: 
                    print("Sucessfully logged out as an Admin\n")
                    running = False 
                    loginGrace =0
        else:
            print("**Input the correct password**")


def customer():
    running = True
    authGrace = 3
    while authGrace > 0:
        customerAccount = input("Please input you account number: ")
        authGrace -= 1
        if customerAccount == "12340":
            authGrace = -1
            while running:
                print(" Welcome Customer")
                print(" \t 1 - Deposit Money ")
                print(" \t 2 - Withdraw Money")
                print(" \t 3 - Exit")

                action = readInputInt("Choose an option: ")
                
                if action == 1:
                    search = readInputAlpha("Input the account name: ")
                    if search in accounts["name"]:
                        index = accounts["name"].index(search)
                        deposit = readInputInt("How much do you want to deposit: ")
                        accounts["balance"][index] += deposit
                        print(f"You have successfully deposited {deposit} to {accounts['name'][index]}")
                    else:
                        print("User not found!")
                elif action == 2:
                    search = readInputAlpha("Input the account name: ")
                    if search in accounts["name"]:
                        index = accounts["name"].index(search)
                        current = accounts["balance"][index]
                        deposit = readInputInt("How much do you want to withdraw: ")
                        if deposit >= current:
                            print("*Insufficient funds *")
                        else:
                            accounts["balance"][index] -= deposit
                            print(f"You have successfully withdrawn {deposit}")
                elif action == 3: 
                    running = False 
                    print("Sucessfully logged out as an customer\n")
        else:
            # running = False
            print("Input a valid Account Number")





while running:
    action = options()
    if action == 1:
        admin()
    elif action == 2:
        customer()
    elif action == 3:
        running = False
