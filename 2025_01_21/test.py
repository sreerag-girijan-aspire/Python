
employees = [
    {"id": 1, "name": "Alice", "department": "HR"},
    {"id": 2, "name": "Bob", "department": "Engineering"},
    {"id": 3, "name": "Charlie", "department": "HR"},
]

emp_count=dict()
for i in employees:
    if i["department"] not in emp_count:
        emp_count[i["department"]]=1
    else :
        emp_count[i['department']]+=1

print(emp_count)


def arbit_args(*name,**kwarg):
    for i in name:
        print(i)
    for kw in kwarg:
        print(kw,kwarg[kw])   
arbit_args("name1","name2","name3",name1="sree",name2="mathi",name3="alan")