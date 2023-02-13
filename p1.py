empno=int(input("Enter employee number : "))
ename=input("Enter employee name : ")
esal=float(input("Enter employee salary : "))

ann_sal=esal*12
bonus=ann_sal*20/100

print("\t\t Employee  Bonus  Report ")
print("-" * 50)
print("\t Employee Number    :  ",empno)
print("\t Employee Name      :  ",ename)
print("\t Employee Salary    :  ",esal)
print("\n\t Anuual Salary    :  ",ann_sal)
print("\t EmployeeBonus      :  ",bonus)
print("-" * 50)
