import random

Nouns_Used      = ["free","joker","hawk","bad","deadly","warmachine","fastdead","fox006","bond","gunpowder",
                  "sniper0","hulk","captain","pablo","singledeadh","black","paw5","snake","knight","winter"]

Soldiers        = ["joker","captain","deadly","sniper0",]
Terrorists      = ["free","winter","warmachine","paw5"]
Password_Data   = []

defeposta = input("E-mail:")
E_Mail = defeposta

class FreedomWar():

    def User_registration():

        while (True):
            defusername = input("Create user name:").lower()

            if (defusername in Nouns_Used):
                print("This username is active. Try a new username.")

            elif (defusername not in Nouns_Used):
                print("{} username succesful".format(defusername))
                break

        while (True):
            defpassword = input("Crate password:")
            defconfirmpassword = input("Confirm password:")

            if (defpassword == defconfirmpassword):
                print("Registration Successful")
                break
            elif (defpassword != defconfirmpassword):
                print("Password and confirmpassword must be same")
            else:
                print("You have to create password")

        while (True):
            Team1 = "soldiers"
            Team2 = "terrorists"
            print("Teams: Soldiers or Terrorists")
            defchooseteam = input("Choose your team:").lower()

            if (defchooseteam == Team1):
                Soldiers.append(defusername)
                break

            elif (defchooseteam == Team2):
                Terrorists.append(defusername)
                break
            else:
                print("You have to choose your team")
    User_registration()









