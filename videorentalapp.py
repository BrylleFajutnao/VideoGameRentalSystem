user_accounts = {}
gameLib = {
    "Helldivers 2": {"copies": 3, "cost": 15},
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
            if newusername in user_accounts:
                print(f"User {newusername} has been already been registered")
            user_accounts[newusername] = {"password":newpassword,"email":newemail,"balance":0.0,"points":0.0, "rented": []} 
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
def logOut():
    while True:
        try:
            c = input("Are you sure you want to Log out Y/n: ")
            if c == 'Y':
                global currUser
                global isLogIn
                currUser=''
                isLogIn = False
            else:
                return
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
    checkBalance()
    while True:
        try:
            c = input("Enter game name to pick a choice: ")
            if not c:
                return
            if user_accounts[currUser]['balance'] > gameLib[c]['cost'] and gameLib[c]['copies'] > 0:
                user_accounts[currUser]['balance'] -= gameLib[c]['cost']
                gameLib[c]['copies'] -= 1
                user_accounts[currUser]['rented'].append(c)
                user_accounts[currUser]['points'] += gameLib[c]['cost']//5
                print(f"Successfully rented {c}")
            else:
                print(f"No {c} available at this time")
                continue
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
def checkBalance():
    print(f'Current Balance: {user_accounts[currUser]['balance']}\n')
def checkPoints():
    print(f'Current Point Balance: {user_accounts[currUser]['points']}\n')
def freeGames():
    while True:
        try:
            displayGames()
            checkPoints()
            c = input("Enter your free game using points: ")
            if not c:
                return
            if c not in gameLib:
                print(f"No game found as {c}")
                continue
            if user_accounts[currUser]['points'] < gameLib[c]['cost']:
                print(f"You have no points for this game")
                continue
            if gameLib[c]['copies'] <= 0:
                print(f"No {c} available at the moment: ")
            user_accounts[currUser]['points'] -= gameLib[c]['cost']
            gameLib[c]['copies'] -= 1
            user_accounts[currUser]['rented'].append(c)
        except ValueError as e:
            print(e)
        break
            
    pass
def addNewGame():
    while True:
        try:
            newGame = input("Enter new Game: ")
            if not newGame:
                return
            cost = float(input("Enter Cost: "))
            copies = int(input("Enter number of copies: "))
            if newGame in gameLib:
                print(f"{newGame} is already on the shelf")
                continue
            gameLib[newGame] = {'cost': cost, 'copies': copies}
        except ValueError as e:
            print(e)
        break
    pass
def editGameDetails():
    displayGames()
    while True:
        try:
            gameToEdit = input("Enter game name to edit")
            if not gameToEdit:
                return
            if gameToEdit not in gameLib:
                print(f"{gameToEdit} not in the list")
                continue
            print(f"Name: {gameToEdit}\n    >Copies(1): {gameLib[gameToEdit]['copies']}\n    >Cost(2): {gameLib[gameToEdit]['cost']}")
            c = int(input("Choose and attribute to edit: "))
            if c == 1:
                while True:
                    try:
                        newCopies = int(input("Enter new number of copies "))
                        if newCopies <= 0:
                            print("Enter a postive value")
                            continue
                        gameLib[gameToEdit]['copies'] = newCopies
                    except ValueError as e:
                        print(e)
                    break
            if c == 2:
                while True:
                    try:
                        newCost = float(input("Enter new cost: "))
                        if newCost <= 0:
                            print("Enter a positive value")
                            continue
                        gameLib[gameToEdit]['cost'] = newCost
                    except ValueError as e:
                        print(e)
                    break
        except ValueError as e:
            print(e)
        break
def adminLogOut():
    while True:
        try:
            confirmation = input("Are you sure you want to log out? Y/n: ")
            if not confirmation:
                return
            if confirmation == 'Y':
                global isLogInAd
                isLogInAd = False
            elif confirmation.lower() == 'n':
                return
            else:
                print("try again")
        except ValueError as e:
            print(e)
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
            print("1.Rent a Game\n2. Return a game\n3. Top-up Account\n4. Display inventory\n5. Check balance\n6. Check Points\n7. Free Game\n8. Logout")
            c = int(input("Enter your choice: "))
            if c == 1:
                rentAGame()
            if c == 2:
                returnItem()
            if c == 3:
                topUp()
            if c == 4:
                displayGames()
            if c == 5:
                checkBalance()
            if c == 6:
                checkPoints()
            if c == 7:
                freeGames()
            if c == 8:
                logOut()
        while isLogInAd:
            print(f'Hello {admin_username}')
            print('1. Add new Game\n2.Edit Game Details\n3.Logout')
            c = int(input('Enter your choice: '))
            if c == 1:
                addNewGame()
            if c == 2:
                editGameDetails()
            if c == 3:
                adminLogOut()
    pass

if __name__ == "__main__":
    returnItem()
    main()