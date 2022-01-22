
def login():
    print("Login Function")
#from registration import registeration
import re

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
pass_reg = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
mobile_regex = re.compile(r"^020?[10,11,12]\d{8}")

def registeration():
    while True:
        fname = input("Please, Enter Your First Name: \n")
        if fname.isalpha():
            break
        else:
            print("Invalid First Name")
    while True:
        lname = input("Please, Enter Your Last Name: \n")
        if lname.isalpha():
            break
        else:
            print("Invalid Last Name")
    while True:
        email = input("Please, Enter Your Email: \n")
        if re.fullmatch(email_regex, email):
            break
        else:
            print("Invalid Email")
    while True:
        print("Instructions For Password")
        print("1-Should have at least one number.")
        print("Should have at least one uppercase and one lowercase character.")
        print("Should have at least one special symbol.")
        print("Should be between 6 to 20 characters long.")
        print("------------------------------------------------------")
        password = input("Please, Enter Your Password: \n ")
        # if password match the regex
        mat = re.search(pass_reg, password)
        if mat:
            break
        else:
            print("Invalid Password ! please enter a valid Password")

    while True:
        confirmPassword = input("Please, Enter Confirm Password: \n")
        if confirmPassword == password:
            break
        else:
            print("Passwords don't match")
    while True:
        phonenumber = input("Please, Enter Your Phone Number: \n")
        if not mobile_regex.match(phonenumber):
            print("Invalid Phone Number! please enter a valid Phone Number")
        else:
            break
    # user data list with , between userdata
    userdata = ",".join([fname, lname, email, password, phonenumber])
    print("user data before newline", userdata)
    userdata = userdata + "\n"
    print("user data after newline", userdata)
    # exception handler for file
    try:
        readfile = open("users.txt")
    except:
        print("File Doesnt Exit")
    else:
        # read data from file
        data = readfile.readlines()
        users = []
        for i in data:
            users.append(i.strip("\n"))
            print(users)
        # to check if user email exits or not
        for user in users:
            userdetails = user.split(",")
            if userdetails[2] == email:
                print("Email Already Exits")
                readfile.close()
                registeration()
        else:
            readfile.close()
            try:
                file = open("users.txt", "a")
            except:
                print("File Doesnt Exit")
            else:
                file.write(userdata)
                file.close()
                print("Registration Successfully")

def main():
    print("************************************************")
    print ("******************Crowd Funding****************")
    while True:
        print("Please , Make Your Choice ")
        print("1- Registration")
        print("2- Log in")
        print("3- Exit")
        choice = int(input("so 1 or 2 or 3 \n"))
        if (choice==1):
            registeration()
            break
        elif (choice==2):
            login()
            break
        elif (choice==3):
             exit()
        else:
            print("Wrong Data")
main()

