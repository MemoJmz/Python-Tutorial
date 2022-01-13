# Python Oriented Programming - Inheritance - Creating Subclasses

# Inheritance allows us to inherit attributes and methods from a parent class.
# It is useful to create subclasses and get all the functionality of our parent
# class and then we can overwrite or add completely new functionality without
# affecting the class in any way

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {} '.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

# Create a subclass
# Between the parentesis we specify what classes that we want to inherit
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # Instead of copy & paste the code of __init__ method
        super().__init__(first, last, pay)
        # or Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

# We get all the functionality of Employee class in Developer class just
# adding a little line

# We'll create another subclass called Manager
class Manager(Employee):
    # I am going to give the option of passing in a list of employees that this
    # manager supervises
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

        # You never want to pass mutable data types, like a list or a dictionary,
        # as default arguments that's the reason because I do not just pass in
        # an empty as default parameter instead of None

    # We'll create two (regular) methods
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Memo', 'Jimenez', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'JavaScript')

# Good Information
# print(help(Developer))

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)
# mgr_1.print_emps()

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()

# Python has two built-in functions called is instance & is subclass
# Instance - Class
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

# Class - Class
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Developer, Developer))
print(issubclass(Manager, Developer))

# One practical real-world examples, easier, could be within the exceptions
# module of Python exceptions library
