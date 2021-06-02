stud_info={'A':56.35,'B':85.55}
'''
nofs=int(input("Enter number of students : "))
i=0
while i<nofs:
    name=input("Enter student name : ").strip()
    stud_info[name]=float(input("Enter percentage : ").strip())
    i=i+1
print(stud_info)
print("Sum of percentae : ",sum(stud_info.values()))
for i in stud_info.keys():
    print('Name : ',i,' Percentage : ',stud_info.get(i),'%')

print("Student is : ",stud_info.get('A','Absent'))
print(stud_info.pop('C'))
print(stud_info)
'''
for k,v in stud_info.items():
    print(k,' has got : ',v,'%')