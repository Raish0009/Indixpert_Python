import json

class Students:

    listData=[]

    def __init__(self):
        pass

    def menu(self):
        print("Press 1 - For student registration")
        print("Press 2 - For student searching")
        print("Press 3 - Exit")
        choice=int(input("Enter your choice : "))
        studentData=Students() 
        if choice==1:
            studentData.register()
        elif choice==2:
            studentData.searching()
        elif choice==3:
            exit()
        else:
            print("Enter valid choice!")
            studentData.menu()
    
    def register(self):

        studentDic={}

        studentDic['id']=int(input("Enter student id :"))
        studentDic['name']=input("Enter student name :")
        studentDic['age']=int(input("Enter student age :"))
        studentDic['grade']=input("Enter student grade :")

        studentData=Students() 
        studentData.listData.append(studentDic)

        choice=input("Do you want to add more students yes/no :")

        if choice=='yes':
            studentData.register()
        else:
            studentData.menu()
                

    def searching(self):
        print("Press 1 - Search student by id")
        print("Press 2 - Search student by name")
        print("Press 3 - Search student by age")
        print("Press 4 - Search student by grade")
        print("Press 5 - Go back to menu")
        choice=int(input("Enter your choice :"))
        studentData=Students() 

        if choice==1:
            choice="id"
            val=int(input("Enter student id :"))
        elif choice==2:
            choice="name"
            val=input("Enter student name :")
        elif choice==3:
            choice="age"
            val=int(input("Enter student age :"))
        elif choice==4:
            choice="grade"
            val=input("Enter student grade :")
        elif choice==5:
            studentData.menu()
        else:
            print("Error! Enter a valid choice")
    
        for students in studentData.listData:
            for key,value in students.items():
                if value==val:
                    pretty_data=json.dumps(students,indent=4)
                    print(pretty_data)


        studentData.menu()


data=Students()
data.menu()