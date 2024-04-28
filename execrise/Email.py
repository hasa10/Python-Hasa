answer=input('Do you already have email account').lower()

if answer=="no":
    email=input('Enter you email adress')
    if ("@" in email and ".com" in email) :
        if (email[-9:])=="gmail.com" or (email[-9:])=="yahoo.com":
            if ("gmail" in email or "yahoo" in email):
                password = input('Enter password (There must be at least 7 letter and digit)')

                if (len(password))>=7 and  password.isalnum() and (not password.isalpha()) and (not password.isdigit()):
                    re_enter=input('Re-enter password')
                    if password==re_enter:
                        print("your email account is created")
                    else:
                        print('your password is not matched')
                else:
                    print("")
            else:
                print("There must be at letter 7 letter and digit")
        else:
            print("please enter '.com'")
    else:
        print("There must be '@' and '.com")
elif answer== "yes":
    email=input('Enter you email adress')
    if ("@" in email and ".com" in email):
        input('Enter password')
    else:
        print("some error in your email address")
else:
    print("try again")
