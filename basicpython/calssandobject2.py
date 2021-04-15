class Employe:
    holiday = 9

    def printdetails(self):  # this is method and method call (object name.function name())
        return f"Name is {self.name}, salary is {self.salary}, role is {self.role}"


harry = Employe()
tejas = Employe()

harry.name = "harry"
harry.salary = 40000
harry.role = "data science"

tejas.name = "tejas"
tejas.salary = 60000
tejas.role = "data analytics"

print(harry.name, harry.salary, harry.role, tejas.name)

print(harry.printdetails())
print(tejas.printdetails())
