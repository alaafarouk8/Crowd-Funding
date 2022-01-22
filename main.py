from AuthenticationSystem import registeration , login
def main():
    print("************************************************")
    print("******************Crowd Funding****************")
    while True:
        print("Please , Make Your Choice ")
        print("1- Registration")
        print("2- Log in")
        print("3- Exit")
        choice = int(input("so 1 or 2 or 3 \n"))
        if (choice == 1):
            registeration()
            break
        elif (choice == 2):
            login()
            break
        elif (choice == 3):
            exit()
        else:
            print("Wrong Data")


main()