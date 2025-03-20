mainList=[]

StudentData={}

qualificationDict={}

qualificationList=[]

skills=[]


StudentData['Student_id']=int(input("Enter your id :"))

StudentData['student_name']=input("Enter your name :")

StudentData['Experience']=input("Enter your experience :")

skill1=(input("Enter your skill 1:"))
skills.append(skill1)

skill2=(input("Enter your skill 2:"))
skills.append(skill2)

skill3=(input("Enter your skill 3:"))
skills.append(skill3)

skill4=(input("Enter your skill 4:"))

skills.append(skill4)

StudentData["Skills"]=skills

qualificationDict['Qualification name']=input("Enter your Qualification name :")

qualificationDict['Passing year']=input("Enter your Passing year :")

qualificationList.append(qualificationDict)

qualificationDict={}

qualificationDict['qualification name']=input("Enter your Qualification name :")

qualificationDict['qualification year']=input("Enter your Passing year :")

qualificationList.append(qualificationDict)

StudentData['qualification']=qualificationList

mainList.append(StudentData)

StudentData={}

qualificationDict={}

qualificationList=[]

skills=[]

StudentData['Student_id']=int(input("Enter your id :"))

StudentData['student_name']=input("Enter your name :")

StudentData['Experience']=input("Enter your experience :")

skill1=(input("Enter your skill 1:"))
skills.append(skill1)

skill2=(input("Enter your skill 2:"))
skills.append(skill2)

skill3=(input("Enter your skill 3:"))
skills.append(skill3)

skill4=(input("Enter your skill 4:"))

skills.append(skill4)

StudentData["Skills"]=skills

qualificationDict['Qualification name']=input("Enter your Qualification name :")

qualificationDict['Passing year']=input("Enter your Passing year :")

qualificationList.append(qualificationDict)

qualificationDict={}

StudentData['qualification']=qualificationList

mainList.append(StudentData)


print(mainList)

mainList[0]['Experience']=input("update experience 1 :")
mainList[1]['Experience']=input("update experience 2 :")


print("Updated data :- ",mainList)

