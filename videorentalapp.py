user_accounts = {}
gameLib = {
    "God Of War": {"copies": 3, "cost": 7},
    "Lethal Company": {"copies": 5, "cost": 4},
    "Palworld": {"copies": 1, "cost": 10},
}
admin_username = "admin"
admin_password = "adminpass"
isLogInAd = False
isLogIn = False
currUser = ''
def SignUp():
    while True:
        try:
            newusername = input("Enter new username:")
            if not newusername : 
                return
            newemail = input("Enter email: ")
            if not newemail :
                return
            newpassword = input("Enter password: ")
            if not newpassword :
                return
            newbalance = input("Enter your balance: ")
            if not newbalance :
                return
            user_accounts[newusername] = {"password":newpassword,"email":newemail,"balance":float(newbalance), "rented": []} 
        except ValueError as e:
            print(e)
        break

def LogIn():
    if not user_accounts:
        print("User Accounts can not be found")
        return
    while True:
        try :
            yourusername = input("Enter your username: ")
            if not yourusername:
                return
            yourpassword = input("Enter your password: ")
            if not yourpassword:
                return
            if yourusername not in user_accounts:
                print("User does not exist")
                continue
            if yourpassword == user_accounts[yourusername]["password"]:
                global isLogIn
                global currUser
                currUser = yourusername
                isLogIn = True
                print("Login Successful")
        except ValueError as e:
            print(e) 
        break           

def AdminLogIn():
    while True:
        usnm = input("Enter username: ")
        passw = input("Enter password: ")
        if usnm == admin_username and passw == admin_password:
            global isLogInAd
            isLogInAd = True      
            print("Admin Log in successful")      
        break

def displayGames():
    if not gameLib:
        print("No Games Found")
    for i,key in enumerate(gameLib):
        print(f"{i+1}. Name: {key}\n    >Copies: {gameLib[key]['copies']}\n    >Cost: {gameLib[key]['cost']}")

def rentAGame():
    displayGames()
    while True:
        try:
            c = input("Enter game name to pick a choice: ")
            if not c:
                return
            if user_accounts[currUser]['balance'] > gameLib[c]['cost'] and gameLib[c]['copies'] > 0:
                user_accounts[currUser]['balance'] -= gameLib[c]['cost']
                gameLib[c]['copies'] -= 1
                user_accounts[currUser]['rented'].append(c)
                print(f"Successfully rented {c}")
        except ValueError as e:
            print(e)
        except KeyError as e:
            print(e)
            continue
        break

def returnItem():
    while True:
        try:
            for i, games in enumerate(user_accounts[currUser]['rented']):
                print(f"{i+1}. {games}")
            c = int(input("Enter choice: "))
            c -= 1
            if c < 0:
                print("enter positive value")
                continue
            if user_accounts[currUser]['rented'][c] in user_accounts[currUser]['rented']:
                if c not in gameLib:
                    print("did not rented here")
                gameLib[user_accounts[currUser]['rented'][c]]['copies'] += 1
                user_accounts[currUser]['rented'].pop(c)

        except ValueError as e:
            print(e)
        except KeyError as e:
            pass
        break

def topUp():
    while True:
        try:
            c = int(input("Enter Amount"))
            if c < 0:
                print("Enter Positive Value")
                continue
            user_accounts[currUser]['balance'] += c
        except ValueError as e:
            print(e)
        break

def addgame():
    while True:
            newgame = input("Enter Game: ")
            if not newgame : 
                return
            copyamt = int (input("Enter Amount: "))
            if not copyamt : 
                return
            gamecost = int (input("Enter Cost: "))
            if not gamecost : 
                return
            gameLib[newgame] = {"copies":copyamt, "cost":gamecost }
            print(gameLib)
            break
    

def main():
    while True:
        while not isLogIn and not isLogInAd:
            print("Welcome to the Game Rental System")
            print("1. Display Available Games")
            print("2. Register User")
            print("3. Login")
            print("4. Admin Login")
            print("5. Exit")
            try:
                c = int(input("Enter your Choice: "))
                if c == 1:
                    displayGames()
                if c == 2:
                    SignUp()
                if c == 3:
                    LogIn()
                if c == 4: 
                    AdminLogIn()
                if c == 5:
                    print("Exiting...")
                    exit(0)
            except ValueError as e:
                print(e)
        while isLogIn:
            print(f"Hello {currUser}")
            print("1.Rent a Game\n2. Return a game\n3. Top-up Account\n4. Display inventory\n5. Check points\n6. Free Game\n7. Logout")
            c = int(input("Enter your choice: "))
            if c == 1:
                rentAGame()
            if c == 2:
                returnItem()
            if c == 3:
                topUp()
            if c == 4:
                displayGames()
        while isLogInAd:
            print(f"Hello Admin")
            print("1. Add game\n2. Logout")
            c = int(input("Enter your choice: "))
            if c == 1:
                addgame()
                


    pass

if __name__ == "__main__":
    returnItem()
    main()