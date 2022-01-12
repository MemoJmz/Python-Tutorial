# Python Oriented Programming, Class Variables

class Employee:

    # (2)
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

        # (3)
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {} '.format(self.first, self.last)

    def apply_raise(self):
        # (1)
        # self.pay = int(self.pay * Employee.raise_amount)
        # This gives us the ability to change that amount for a single instance if we wanted
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps)

emp_1 = Employee('Memo', 'Jimenez', 50000)
emp_2 = Employee('Test', 'User', 60000)

# emp_1 instance of the class Employee
# attribute  = class variable

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# For example, we do not want to change the porcent manually
# See (1)
# raise_amount is a class Variable
# It will give us a error, that we need to do is writte
# Employee.raise_amount
# or self.raise_amount

# What is going on?

print(emp_1.__dict__)           # There is no raise_amount there
print(Employee.__dict__)        # It does contains it

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# We can access to the class variable from my class itself as well as
# from both instances

Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.raise_amount = 1.06
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# When we made this assignment it actually created the raise_amount
# attribute within Employee one
print(emp_1.__dict__)

# F.e. the number of employees would be the same for al instances
# See (2)
# We'll create a new method each time that I created a new employee
# See (3)

print(Employee.num_of_emps)
