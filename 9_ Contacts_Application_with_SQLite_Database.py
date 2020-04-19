import sqlite3

con = sqlite3.connect("Contacts_Application.db")

cursor = con.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS Contact (Number INT, Name TEXT, Surname)")
    con.commit()
create_table()

def add_new_record_for_admin():         # This function is create for admin only.
    cursor.execute("Insert into Contact Values (?,'?','?')")
    con.commit()                        #Admin can run the function and enter the values in parentheses.

def menu():
    print("Menu")
    print("", "1-Add New Record")
    print("", "2-Search Record in Contact")
    print("", "3-Delete Record from Contact")
    print("", "4-Settings")

def search_record_contact():
    print("Search Record")
    print("", "5-Search by Number")
    print("", "6-Search by Name")
    print("", "7-Search by Surname")

def delete_record_contact():
    print("Delete Record")
    print("", "8-Delete by Number")
    print("", "9-Delete by Name")
    print("", "10-Delete by Surname")


def add_new_record(number, name, surname):
    cursor.execute("Insert into Contact Values (?,?,?)", (number, name, surname))
    con.commit()


def search_by_number(number):
    cursor.execute("Select * From Contact Where Number = ?", (number,))
    Contact = cursor.fetchall()
    if (len(Contact) == 0):
        print("No Record Founds.")
    else:
        for i in Contact:
            print(i)


def search_by_name(name):
    cursor.execute("Select * From Contact Where Name = ?", (name,))
    Contact = cursor.fetchall()
    if (len(Contact) == 0):
        print("No Record Founds.")  # If the user wants to search for records and this record is not in the...
        # ...contacts list, we can show the user that the record he is looking for
        # ... cannot be found with this function
    else:
        for i in Contact:
            print(i)


def search_by_surname(Surname):
    cursor.execute("Select * From Contact Where Surname = ? ", (Surname,))
    Contact = cursor.fetchall()
    if (len(Contact) == 0):
        print("No Record Founds.")
    else:
        for i in Contact:
            print(i)

def delete_by_number(number):
    cursor.execute("Delete From Contact where Number = ?", (number,))
    con.commit()

def delete_by_name(name):
    cursor.execute("Select * From Contact where Name = ?", (name,))
    if ( len(list(cursor)) > 1):
        cursor.execute("Select * From Contact Where Name = (?)", (name,))
        Contact = cursor.fetchall()
        for i in Contact:
            print(i)
        delete_number = input("Which Number of Records Are Deleted:")
        cursor.execute("Delete From Contact where Name = ? and Number = ?", (name, delete_number))
        con.commit()
    else:
        cursor.execute("Delete From Contact where Name = ?", (name,))
        con.commit()

def delete_by_surname(surname):
    cursor.execute("Select * From Contact where Surname = ?", (surname,))

    if (len(list(cursor)) > 1):
        cursor.execute("Select * From Contact Where Surname = (?)", (surname,))
        Contact = cursor.fetchall()
        for i in Contact:
            print(i)
        delete_number = input("Which Number of Records Are Deleted:")
        cursor.execute("Delete From Contact where Surname = ? and Number = ?", (surname, delete_number))
        con.commit()

    else:
        cursor.execute("Delete From Contact where Surname = ?", (surname,))
        con.commit()

def settings():
    cursor.execute("Select * From Contact")
    Contact = cursor.fetchall()
    for con in Contact:
        print(con)

while (True):
    defAdd              = "1"
    defSearch           = "2"
    defDelete           = "3"
    defPrint            = "4"
    defSearchbyNumber     = "5"
    defSearchbyName       = "6"
    defSearchbySurname    = "7"
    defDeletebyNumber     = "8"
    defDeletebyName       = "9"
    defDeletebySurname    = "10"

    menu()
    defProcess = input("Select Your Process:")

    cursor.execute("Select * From Contact")
    Contact = cursor.fetchall()
    if (defProcess == defAdd):
        print("Add Record")

        while(True):            # Here, we want to from the user to enter values.
            number = input("Enter Record Number:")

            try:
                number  = int(number)   # If the user enters text instead of a numeric value, we get a ValueError error.
            except ValueError:
                print("Record Number Must Be Numbers.")

            else:               # Without this error output, we can allow the user to enter numeric values.
                                # The loop will continue until the user enters a numeric value.
                break
        name    = input("Enter Record Name:")
        surname = input("Enter Record Surname:").upper()
        add_new_record(number,name,surname)
        print("Create Record Successful.")

    elif (defProcess == defSearch):
        search_record_contact()
        deffind = input("Select Search Criteria:")

        if (deffind == defSearchbyNumber):
            print("Search by Number")
            findNumber = input("Enter The Number You Want To Search:")
            search_by_number(findNumber)

        elif (deffind == defSearchbyName):
            print("Search by Name")
            findName = input("Enter the Name You Want To Search:")
            search_by_name(findName)

        elif (deffind == defSearchbySurname):
            print("Search by Surname")
            findSurname = input("Enter the Surname You Want To Search:").upper()
            search_by_surname(findSurname)

        else:
            print("Only Select The Process You Want To Do")

    elif (defProcess == defDelete):
        delete_record_contact()
        deleteRecord = input("Select Delete Criteria:")

        if (deleteRecord == defDeletebyNumber):
            askNumber = int(input("Enter The Number You Want To Delete:"))
            delete_by_number(askNumber)
            print("Record Deleted Successfully .")
        elif (deleteRecord == defDeletebyName):
            askName = input("Enter The Name You Want To Delete:")
            delete_by_name(askName)
            print("Record Deleted Successfully .")
        elif (deleteRecord == defDeletebySurname):
            askSurname = input("Enter The Surname You Want To Delete:")
            delete_by_surname(askSurname)
            print("Record Deleted Successfully .")
        else:
            print("Only Select The Process You Want To Do")

    elif (defProcess == defPrint):
        print("Print Record")
        printContact = input("Do You Confirm Printing The Record (Y/N) :").upper()
        Y = str("Y")
        N = str("N")
        if (printContact == Y):
            settings()
        elif (printContact == N):
            print("Your Transaction Has Been Canceled")
        else:
            print("Only Select The Process You Want To Do")

    else:
        print("!!! Only Enter The Number of The Process !!!")

