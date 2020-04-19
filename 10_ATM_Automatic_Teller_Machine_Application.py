import sqlite3
import smtplib
import datetime

con = sqlite3.connect("Customer_Information.db")
cursor = con.cursor()


def create_table():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Informations (Name TEXT, Surname TEXT, eMail TEXT, CardPin TEXT, Balance INT)")
    con.commit()


create_table()


def database_manager(Name, Surname, eMail, CardPin, Balance):
    cursor.execute("Insert into Informations  Values (?,?,?,?,?)",
                   (Name, Surname, eMail, CardPin, Balance))
    con.commit()


def process():
    print("Main Menu")
    print(" ", "Please Press 1 For Balance")
    print(" ", "Please Press 2 For Withdrawal")
    print(" ", "Please Press 3 For Deposit Money")
    print(" ", "Please Press 4 For Return Card", "\n")


def show_balance(defEnterPin):
    cursor.execute("Select * From Informations  Where CardPin = ? ", (defEnterPin,))
    Informations = cursor.fetchall()
    for inf in Informations:
        print(inf[4])


def update_balance_withdrawal(totalQuantity, defEnterPin):
    cursor.execute("UPDATE Informations SET Balance = ? Where CardPin = ?",
                   (totalQuantity, defEnterPin,))
    con.commit()


def update_balance_deposit(totalQuantity, defEnterPin):
    cursor.execute("UPDATE Informations SET Balance = ? Where CardPin = ?",
                   (totalQuantity, defEnterPin,))
    con.commit()


def send_information(CardPin):
    global name
    global surname
    global email
    today = datetime.datetime.now()
    dateAndtime = datetime.datetime.strftime(today, "%c")

    cursor.execute("Select * From Informations  Where CardPin = ? ", (CardPin,))
    Informations = cursor.fetchall()
    for inf in Informations:
        name = inf[0]
        surname = inf[1]
        email = inf[2]

    content = "Dear {} {}".format(name, surname) + "\n" + \
              "Your card has been processed on {} date.".format(dateAndtime) + "\n" + \
              "If this process is not yours." + "Please contact your bank representative."

    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("omerdemirarsln@gmail.com", "Omersabina090816")
    mail.sendmail("omerdemirarsln@gmail.com", email, content)


def total_quantity_withrawal(defEnterPin):
    defwithdrawal = int(input("How Much Would You Like to Withdrawal?:"))
    global totalQuantity

    cursor.execute("Select * From Informations  Where CardPin = ? ", (defEnterPin,))
    Informations = cursor.fetchall()
    for inf in Informations:
        if (defwithdrawal < inf[4]):
            totalQuantity = inf[4] - defwithdrawal

            send_information(defEnterPin)

        elif (defwithdrawal > inf[4]):
            print("Your Account Balance Is Not Enough")
            break


    update_balance_withdrawal(totalQuantity, defEnterPin)


def total_quantity_deposit(defEnterPin):
    defquantity = int(input("How Much Would You Like to Deposit? :"))
    global totalQuantity
    cursor.execute("Select * From Informations  Where CardPin = ? ", (defEnterPin,))
    Informations = cursor.fetchall()
    for inf in Informations:
        totalQuantity = inf[4] + defquantity

    update_balance_deposit(totalQuantity, defEnterPin)


def control_pin(CardPin):
    cursor.execute("Select * From Informations  Where CardPin = ? ", (CardPin,))
    Informations = cursor.fetchall()

    if (len(Informations) == 0):
        print("Pin Incorrect")

    elif (len(Informations) > 0):

        while (True):
            process()

            defOption = input("Please Select Your Option:")

            if (defOption == "1"):

                show_balance(defEnterPin)

            elif (defOption == "2"):

                total_quantity_withrawal(defEnterPin)

            elif (defOption == "3"):

                total_quantity_deposit(defEnterPin)


            elif (defOption == "4"):
                print("We wish you a nice day.", "\n", "Please wait whilst your card is Returned...")
                break

            else:
                print("Only Enter The Number of The Process")


while (True):
    global defEnterPin

    print("""""*******************************************************
                                                        *
                    Welcome to FastBank                 *
                                                        *
                  Please Insert Your Card               *
                                                        *
*********************************************************""")


    print("Your card is being identified, please wait.", "\n")
    defloop = 0

    while (defloop < 3):
        defloop += 1

        defEnterPin = input("Please Enter Your 4 Digit Pin:")

        control_pin(defEnterPin)

    if (defloop == 3):

        print("The card password was entered incorrectly 3 times.", "\n", "\n",
              "Please contact your bank branch for your card retrieve.")
        break
