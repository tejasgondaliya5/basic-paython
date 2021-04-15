# this programing is costructor in OOP
class Employe:
    holiday = 9

    def __init__(self, aname, asalary, arole):  # that is constructor and this function call automatically
        self.name = aname
        self.salary = asalary
        self.role = arole


harry = Employe("harry", 40000, "data science")  # this line is give direct argument in Employe
tejas = Employe("tejas", 60000, "data analytics") # this line is give direct argument in Employe
print(harry.salary)
print(tejas.salary)
ravi = Employe("ravi", 80000, "java softwaer engineer")
print(ravi.salary)