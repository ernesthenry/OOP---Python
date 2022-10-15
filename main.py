class Employee:
    EmpCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.EmpCount += 1

    def displayCount(self):
        print("Employee count %d" % Employee.EmpCount)

    def displayEmployee(self):
        print("Name : ", self.name  ,"Salary : ", self.salary)



emp1 = Employee("Ernest", 5000000)
emp2 = Employee("Henry", 10000000)

emp1.displayEmployee()
emp2.displayEmployee()

print("Total  employee %d" % Employee.EmpCount)


