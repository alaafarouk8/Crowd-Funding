from main import main
def createpost():
    print("create post")
def View():
    print("view post")
def Search():
    print("Search post")
def Delete():
    print("Delete post")
def Back():
    print("Back post")

def projectmenu():
    print("------------------------------------------")
    print("----------------Project Menu--------------")
    while True:
        print("Please , Make Your Choice ")
        print("1- Create project")
        print("2- View Project")
        print("3- Search")
        print("4- Delete")
        print("5- Back")
        print("6- Exit")
        choice = int(input("so 1 or 2 or 3 or 4 or 5 or 6\n"))
        if (choice == 1):
            createpost()
            break
        elif (choice == 2):
            View()
            break
        elif (choice == 3):
            Search()
            break
        elif (choice == 4):
            Delete()
            break
        elif (choice == 5):
            main()
            break
        elif (choice == 6):
            exit()
        else:
            print("Wrong Data")