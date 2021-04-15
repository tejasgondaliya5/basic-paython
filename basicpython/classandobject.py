class Student:  # Student is class  but "S"  is capital is good practice but not compulsory
    pass


raj = Student()  # harry and larry is object
ravi = Student()

raj.std = 12  # harry.std and harry.name is instance variable
raj.name = "raj"

ravi.std = 10

print(raj, ravi)
print(raj.name, ravi.std)


class Employe:
    holiday = 9
    pass


harry = Employe()
tejas = Employe()

harry.name = "harry"
harry.salary = 40000
harry.role = "data science"

tejas.name = "tejas"
tejas.salary = 60000
tejas.role = "data analytics"

print(harry.name, tejas.name, harry.salary, tejas.salary)
print(Employe.holiday)
print(harry.holiday)
print(tejas.holiday)
print()

print(Employe.__dict__)
print()
print(tejas.__dict__)
print(harry.__dict__)
print()

Employe.holiday = 7  # it is change all employee holiday because employee holiday is not private
print(Employe.holiday)
print(harry.holiday)
print(tejas.holiday)
print()

tejas.holiday = 8  # it is change only tejas holiday because this is tejas private instance variable
print(tejas.holiday)
print(Employe.holiday)
print(harry.holiday)
print()

print(Employe.__dict__)
print()
print(tejas.__dict__)
print(harry.__dict__)
