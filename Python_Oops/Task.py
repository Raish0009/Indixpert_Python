import json
listData=[]
class Students:

    def __init__(self):
        self.id=int(input("Enter student id :"))
        self.name=input("Enter student name :")
        self.age=int(input("Enter student age :"))
        self.grade=input("Enter student grade :")

    def register(self):

        studentDic={}

        studentDic['id']=self.id
        studentDic['name']=self.name
        studentDic['age']=self.age
        studentDic['grade']=self.grade

        listData.append(studentDic)

        choice=input("Do you want to add more students yes/no :")

        if choice=='yes':
            mydata=Students()
            mydata.register()
        
    
    def display_info(self):
        StudentsData=json.dumps(listData,indent=4)
        print(StudentsData)

data=Students()

data.register()

data.display_info()