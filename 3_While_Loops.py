print("Create New Profile")

defname             = input("Name:")
defsurname          = input("Surname:")
defbirthDate        = input("Birth Date:")
defemail            = input("E-mail:")

while (True):
    defpassword         = input("Create Password:")
    defconfirmPassword  = input("Confirm Password:")

    if (defpassword == defconfirmPassword):
        print("Succesful")
        print("Redirecting to your profile...")
        break
    elif (defpassword != defconfirmPassword):
        print("Password and confirmpassword must be same")

while (True):
    email    = input("E-mail:")
    password = input("Password:")

    if (email == defemail and password == defpassword):
        print("Welcome"," {}".format(defname))
        break
    elif (email == defemail and password != defpassword):
        print("Password is incorrect !!!")
    elif (email != defemail and password == defpassword):
        print("E-mail is incorrect !!!")
    elif (email != defemail and password != defpassword):
        print("E-mail and Password is incorrect. Please contact call center...")
        break












