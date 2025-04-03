def Searching(Student_details):
    username=input("Enter student name :- ")
    for i in range(len(Student_details)):
        if(Student_details[i]['name']==username):
            print(Student_details[i])