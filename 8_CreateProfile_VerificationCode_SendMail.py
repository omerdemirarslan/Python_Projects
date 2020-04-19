import smtplib
import random
import sqlite3

con = sqlite3.connect("Personal_data.db")
cursor = con.cursor()
def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS INFORMATIONS  (Name TEXT, Surname TEXT, Birthdate INT,eMail TEXT,Profile Password INT)")
    con.commit()
create_table()

verificationCode = str(random.randint(100000,999999))
content   = "Hello Okan DINC." + "\n" + "WELCOME TO YOUR NEW FAMILY" + "\n" + "You can use this code for enter your profile" + "\n" +\
          verificationCode

def send_verification_code():
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("omerdemirarsln@gmail.com", "sender password")
    mail.sendmail("omerdemirarsl@gmail.com", "recipient email", content)

def add_new_record (defname, defsurname, defbirthdate, defemail, defpassword):
    cursor.execute("Insert into INFORMATIONS Values (?,?,?,?,?)", (defname, defsurname, defbirthdate, defemail, defpassword))
    con.commit()

print("Create New Profile")

defname                 = input("Name:")
defsurname              = input("Surname:")
defbirthDate            = input("Birth Date:")
defemail                = input("E-mail:")

while (True):
    defpassword         = input("Create Password:")
    defconfirmPassword  = input("Confirm Password:")

    if (defpassword == defconfirmPassword):
        add_new_record(defname, defsurname, defbirthDate, defemail, defpassword)
        print("Succesful")
        print("Redirecting to your profile...")
        break

    elif (defpassword != defconfirmPassword):
        print("Password and confirmpassword must be same")

while (True):
    email    = input("E-mail:")
    password = input("Password:")

    if (email == defemail and password == defpassword):
        send_verification_code()
        defcode = input("Please Enter Your Verification Code:")

        if (defcode == verificationCode):
            print("Welcome"," {}".format(defname))
            break
        elif (defcode != verificationCode):
            print("Verification Code Incorrect.")

    elif (email == defemail and password != defpassword):
        print("Password is incorrect !!!")

    elif (email != defemail and password == defpassword):
        print("E-mail is incorrect !!!")

    elif (email != defemail and password != defpassword):
        print("E-mail and Password is incorrect.")