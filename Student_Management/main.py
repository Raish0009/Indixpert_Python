import StudentRegister
import StudentDetails
import StudentSearch

Students=[]

def menu():
    print("*** Student Management ***")
    print("1- Student Registeration")
    print("2- Student Details")
    print("3- Student Search")
    print("4- Exit")

    UserInput()

def UserInput():
    user_data=int(input("Insert user input :- "))
    Management(user_data)



def Management(user_choice):

    if(user_choice==1):
        data=StudentRegister.registeration()
        Students.append(data)
        menu()
    elif(user_choice==2):
        StudentDetails.Details(Students)
        menu()
    elif(user_choice==3):
        StudentSearch.Searching(Students)
        menu()
    elif(user_choice==4):
        exit()
    else:
        print("Error! Insert valid choice")


menu()


