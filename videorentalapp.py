user_accounts = {}
gameLib = {
    "God Of War": {"copies": 3, "cost": 7},
    "Lethal Company": {"copies": 5, "cost": 4},
    "Palword": {"copies": 1, "cost": 10},
}
admin_username = "admin"
admin_password = "adminpass"
isLogInAd False
isLogIn = False
currUser = ''
def SignUp():
    while True:
        try:
    
            newusername = input("Enter new username:")
            if not newusername : 
                return
            newemail = input("Enter email")
            if not newemail :
                return
            newpassword = input("Enter password")
            if not newpassword :
                return
            newbalance = input("Enter your balance")
            if not newbalance :
                return
            user_accounts[newusername] = {"password":newpassword,"email":newemail,"balance":float(newbalance)} 
        except ValueError as e:
            print(e)
        break

def LogIn():
    if not user_accounts:
        print("User Accounts can not be found")
        return
    while True:
        try :
            yourusername = input("Enter your username")
            if not yourusername:
                return
            yourpassword = input("Enter your password")
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
        usnm = input("Enter username")
        passw = input("Enter password")
        if usnm == admin_username and passw == admin_password:
            global isLogInAd
            isLogInAd = True      
            print("Admin Log in successful")      


def main():
    while True:
        while not isLogIn and not isLogInAd:
            print("Welcome to the Game Rental System")
            print("1. Display Available Games")
            print("2. Register User")
            print("3. Login")
            print("4. Admin Login")
            print("5. Exit")
            c = int(input("Enter your Choice"))

            if c == 2:
                SignUp()
            if c == 3:
                LogIn()
            if c == 4: 
                AdminLogIn()
        while isLogIn:
            print(f"Hello {currUser}")
            print("1.Rent a Game\n2. Return a game\n3. Top-up Account\n4. Display inventory\n5. Check points\n6. Free Game\n7. Logout")
            

            
    
    pass

if __name__ == "__main__":
    main()