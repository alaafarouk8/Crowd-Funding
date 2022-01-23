import re
import datetime
format = "%d-%m-%Y"
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
pass_reg = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
mobile_regex = re.compile(r"^020?[10,11,12]\d{8}")
class useroperations:
    # def __init__(self,  fname, lname, email,passowrd, phonenumber):
    #     self.id = id
    #     self.fname = fname
    #     self.lname = lname
    #     self.email = email
    #     self.passowrd = passowrd
    #     self.phonenumber = phonenumber
    def registeration(self):
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
            print("2-Should have at least one uppercase and one lowercase character.")
            print("3-Should have at least one special symbol.")
            print("4-Should be between 6 to 20 characters long.")
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
        userdata = userdata + "\n"
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
            # to check if user email exits or not
            for user in users:
                userdetails = user.split(",")
                if userdetails[2] == email:
                    print("Email Already Exits")
                    readfile.close()
                    self.registeration()
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

    def login(self):
        while True:
            email = input("Please, Enter Your Email: \n")
            if re.fullmatch(email_regex, email):
                break
            else:
                print("Invalid Email")
        while True:
            password = input("Please, Enter Your Password: \n ")
            # if password match the regex
            mat = re.search(pass_reg, password)
            if mat:
                break
            else:
                print("Invalid Password ! please enter a valid Password")

        readfile = open("users.txt")
        data = readfile.readlines()
        users = []
        for i in data:
            users.append(i.strip("\n"))
        for user in users:
            userdetails = user.split(",")
            if userdetails[2] == email and userdetails[3] == password:
                print("Logged in Successfully")
                mainMenu.projectmenu(email)
                readfile.close()
                break
        else:
            print("User Doesnt Exit")
            self.login()
class projectOperations:
    # def __init__(self, id, title, details, total_target, start_date, end_date,owner_project):
    #     self.id=id
    #     self.title = title
    #     self.details = details
    #     self.total_target = total_target
    #     self.start_date = start_date
    #     self.end_date = end_date
    #     self.project_raiser = owner_project
    def createproject(self,email):
        print("--------------Create Project------------------")
        while True:
            id = input("Please, Enter Project Id \n")
            if id.isdigit():
                break
            else:
                print("Invalid Id")
        while True:
            title = input("Please, Enter Project Title \n")
            if title.isalpha():
                break
            else:
                print("Invalid Title")
        while True:
            details = input("Please, Enter Project Details \n")
            if details.isalpha():
                break
            else:
                print("Invalid details")
        while True:
            target = input("Please, Enter Project Target \n")
            if target.isdigit():
                break
            else:
                print("Invalid Target")

        while True:
            pro_startdate = input("Please, Enter Project Start Date:\n")
            try:
                datetime.datetime.strptime(str(pro_startdate), format)
            except ValueError:
                print("This is the incorrect date string format. It should be DD-MM-YYYY")
            else:
                start_date = datetime.datetime.strptime(str(pro_startdate), format)
                datenow = datetime.datetime.today()
                if (datenow > start_date):
                    print("Start Date cant be less than ", datenow)
                else:
                    break;
        while True:
            pro_enddate = input("Please, Enter Project End Date:\n")
            try:
                datetime.datetime.strptime(str(pro_enddate), format)
            except ValueError:
                print("This is the incorrect date string format. It should be DD-MM-YYYY")
            else:
                end_date = datetime.datetime.strptime(str(pro_enddate), format)
                if (end_date < start_date):
                    print("Start Date cant be less than ", start_date)
                else:
                    break;
        # project data list with , between project data
        projectdata = ",".join([id, title, details, target, pro_startdate, pro_enddate, email])
        projectdata = projectdata + "\n"
        try:
            readfile = open("projects.txt")
        except:
            print("File Doesnt Exit")
        else:
            # read data from file
            data = readfile.readlines()
            projects = []
            for i in data:
                projects.append(i.strip("\n"))
            for project in projects:
                projectsdetails = project.split(",")
                if projectsdetails[0] == id:
                    print("Project Already Exits")
                    readfile.close()
                    self.createproject(email)
            else:
                readfile.close()
                try:
                    file = open("projects.txt", "a")
                except:
                    print("File Doesnt Exit")
                else:
                    file.write(projectdata)
                    file.close()
                    print("Project Have been Created Successfully")
                    mainMenu.projectmenu(email)


# ------------------------------------------------------------------------------------------ #
    def View(self,email):
        print("------------View Project----------------")
        try:
            readfile = open("projects.txt")
        except:
            print("File Doesnt Exit")
        else:
            # read data from file
            data = readfile.readlines()
            projects = []
            for i in data:
                projects.append(i.strip("\n"))
            for project in projects:
                projectsdetails = project.split(",")
                if projectsdetails[6] == email:
                    print("----------------Projects----------------")
                    print(f"{projects}")
                    readfile.close()
                    mainMenu.projectmenu(email)
            else:
                 print("This user doesnt have any projects to view")
                 main.projectmenu(email)


# ------------------------------------------------------------------------------------------ #
    def Search(self,email):
        print("------------Search Project----------------")

        while True:
            print("Please , Make Your Choice ")
            print("1- Search By Name")
            print("2- Search By Date")
            print("3- back")
            choice = int(input("so 1 or 2 or 3 \n"))
            if (choice == 1):
                while True:
                    project_name = input("Please, Enter Project Name \n")
                    if project_name.isalpha():
                        break
                    else:
                        print("Invalid Title")
                try:
                    readfile = open("projects.txt")
                except:
                    print("File Doesnt Exit")
                else:
                    # read data from file
                    data = readfile.readlines()
                    projects = []
                    for i in data:
                        projects.append(i.strip("\n"))
                    for project in projects:
                        projectsdetails = project.split(",")
                        if projectsdetails[1] == project_name and projectsdetails[6] == email:
                            print("----------------Projects----------------")
                            print(f"{project}")
                            readfile.close()
                            mainMenu.projectmenu(email)
                    else:
                        print("This Project Doesnt Exit")
                        self.Search(email)
            elif (choice == 2):
                try:
                    projectfile = open("projects.txt")
                except:
                    print("file not found")
                else:
                    data = projectfile.readlines()
                    projects = []
                    for item in data:
                        projects.append(item.strip("\n"))
                    project_start_date = input("enter start date \n")
                    project_end_date = input("enter end date \n")
                    for project in projects:
                        projectdetails = project.split(",")
                        if projectdetails[4] == project_start_date and projectdetails[5] == project_end_date:
                            if projectdetails[6] == email:
                                print(f"{project}")
                                projectfile.close()
                                break
                        # break
                    else:
                        print("## you entered wrong date of project search again ! ##")
                        self.Search(email)
            elif (choice == 3):
                mainMenu.projectmenu(email)
            else:
                print("Wrong Data")

# ------------------------------------------------------------------- #
    def Delete(self,email):
        print("------------Delete Project----------------")
        while True:
            project_name = input("Please, Enter Project Name \n")
            project_id = input("Please, Enter Project id \n")
            if project_name.isalpha() and project_id.isdigit():
                break
            else:
                print("Invalid Title or Invalid Id")
        try:
            projectfile = open("projects.txt")
        except:
            print("file not found")
        else:
            data = projectfile.readlines()
            projects = []
            for item in data:
                projects.append(item.strip("\n"))
            for project in projects:
                projectdetails = project.split(",")
                if projectdetails[0] == project_id and projectdetails[6] == email:
                    print(project)
                    projects.remove(project)
                    print("Project Has Been Deleted Successfully!")
                    projectfile.close()
                    wfile = open("projects.txt", "w")
                    for pro in projects:
                        wfile.write(pro + "\n")
                    wfile.close()
                    mainMenu.projectmenu(email)
            else:
               print("This Project Doesnt Exit")
               self.Delete(email)

user = useroperations()
project=projectOperations()
class mainMenu:
    def main(self):
        print("------------------------------------------")
        print("---------------Crowd Funding--------------")
        while True:
            print("Please , Make Your Choice ")
            print("1- Registration")
            print("2- Log in")
            print("3- Exit")
            choice = int(input("so 1 or 2 or 3 \n"))
            if (choice == 1):
                 user.registeration()
                 break
            elif (choice == 2):
                user.login()
                break
            elif (choice == 3):
                exit()
            else:
                print("Wrong Data")

    def projectmenu(email):
        print("------------------------------------------")
        print("----------------Project Menu--------------")
        while True:
            print("Please , Make Your Choice ")
            print("1- Create Project")
            print("2- View Project")
            print("3- Search")
            print("4- Delete")
            print("5- Back")
            print("6- Exit")
            choice = int(input("so 1 or 2 or 3 or 4 or 5 or 6\n"))
            if (choice == 1):
                project.createproject(email)
                break
            elif (choice == 2):
                project.View(email)
                break
            elif (choice == 3):
                project.Search(email)
                break
            elif (choice == 4):
                project.Delete(email)
                break
            elif (choice == 5):
                main.main()
                break
            elif (choice == 6):
                exit()
            else:
                print("Wrong Data")
main = mainMenu()
main.main()


