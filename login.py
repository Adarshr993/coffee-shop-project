import mysql.connector
import mainmenu
import users;

while True:
    x=users.login()
    if(x==-1):
        print("Invalid User Name/Password")
    else:
        mainmenu.MainMenu("MainMenu")
