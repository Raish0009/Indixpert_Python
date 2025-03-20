mainList=[]

mydata={}

qualificationDict={}

qualificationList=[]

skills=[]

mydata['Student_id']=int(input("Enter your id :"))

mydata['student_name']=input("Enter your name :")

mydata['Experience']=input("Enter your experience :")

skill1=(input("Enter your skill :"))
skills.append(skill1)

skill2=(input("Enter your skill :"))
skills.append(skill2)

skill3=(input("Enter your skill :"))
skills.append(skill3)

skill4=(input("Enter your skill :"))

skills.append(skill4)

mydata["Skills"]=skills

qualificationDict['Qualification name']=input("Enter your Qualification name :")

qualificationDict['Passing year']=input("Enter your Passing year :")

qualificationList.append(qualificationDict)

qualificationDict={}

qualificationDict['qualification name']=input("Enter your Qualification name :")

qualificationDict['qualification year']=input("Enter your Passing year :")

qualificationList.append(qualificationDict)

mydata['qualification']=qualificationList

mainList.append(mydata)

mydata={}

qualificationDict={}

qualificationList=[]

skills=[]

mydata['Student_id']=int(input("Enter your id :"))

mydata['student_name']=input("Enter your name :")

mydata['Experience']=input("Enter your experience :")

skill1=(input("Enter your skill :"))
skills.append(skill1)

skill2=(input("Enter your skill :"))
skills.append(skill2)

skill3=(input("Enter your skill :"))
skills.append(skill3)

skill4=(input("Enter your skill :"))

skills.append(skill4)

mydata["Skills"]=skills

qualificationDict['Qualification name']=input("Enter your Qualification name :")

qualificationDict['Passing year']=input("Enter your Passing year :")

qualificationList.append(qualificationDict)

qualificationDict={}

qualificationDict['qualification name']=input("Enter your Qualification name :")

qualificationDict['qualification year']=input("Enter your Passing year :")

qualificationList.append(qualificationDict)

mydata['qualification']=qualificationList

mainList.append(mydata)


print(mainList)

