#! /usr/bin/python
# coding = utf-8

class Employee:
	empCount = 0;
	def __init__(self,name,salary):
		self.name = name;
		self.salary = salary
		Employee.empCount +=1;
	def displayCount(self):
		print "Total Employee %d" % Employee.empCount
	
	def displayEmployee(self):
		print "Name:",self.name,",Salary:",self.salary;
	
emp1 = Employee("Zara",20000);

emp1.displayCount()
emp2 = Employee("Jack","18000");

emp1.displayEmployee();
emp2.displayEmployee();
'''
print "Total Employee %d" % Employee.empCount
'''
emp2.displayCount()


emp1.age = 17
emp1.age = 19
del emp1.age 
setattr(emp2,'age',20) 
print hasattr(emp2,'age')
 
print getattr(emp2,'age') 
print delattr(emp2,'age')

