# Python Object-Oriented Programming

# We will learning the basics of creating and instantiating simple classes
# (1)
# class Employee:
#     # If you want a function or class empty use pass
#     # and Python will kwon that you just want to skip that for now
#     pass
#     # Here is a simple class with no attributes or methods

# emp_1 = Employee()
# emp_2 = Employee()
#
# They have different memory locations
# print("emp_1 = {}".format(emp_1))
# print("emp_2 = {}".format(emp_2))

# Instance variables contain data that is unique to each instance
# We can create manually instansce variables
# emp_1.first = 'Memo' # (3)
# emp_1.last = 'Jimenez'
# emp_1.email = 'mastergajf@gmail.com'
# emp_1.pay = 50000
#
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@gmail.com'
# emp_2.pay = 60000

# Now each of these instances have attributes that are unique of them
# print("emp_1.email = {}".format(emp_1.email))
# print("emp_2.email = {}".format(emp_2.email))

# Set up that automatically when we create the employee
# We are going to use a special init method
# See (2)

# (2)
class Employee:
    # __init__ method. It is like a constructor in other language
    def __init__(self, first, last, pay):
    # When we create methods whitin a class they receive the instance
    # as the first argument automatically. By convention we should call
    # the instance self.
    # After self, we can specify what other arguments that we want to accept.
        self.first = first # It is equals
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

        # These do not need to be the same as our arguments
        # f.e. self.fname = first

    # (4) Define a method inside of the class employee
    # Each method within a class automatically takes the instance
    # as first argument. In this case we only need the instance as argument
    def fullname(self):
        return '{} {} '.format(self.first, self.last)


emp_1 = Employee('Memo', 'Jimenez', 50000)
emp_2 = Employee('Test', 'User', 60000)
# When we run these lines the __init__ method runs automatically
# emp_1 will be passed as self as first parameter of the method

print("emp_1.email = {}".format(emp_1.email))
print("emp_2.email = {}".format(emp_2.email))

# Instead of use print('{} {} '.format(emp_1.first, emp_1.last))
# for each employee we define the method (4)
print('emp_1 : ' + emp_1.fullname())
print('emp_2 : ' + emp_2.fullname())

# One common mistake creating methods is forgetting the self
# argument for the instance

# We can also run this method using the class name itself
emp_1.fullname()            # (5)
Employee.fullname(emp_1)    # (6)

# The lines (5) & (6) do the exact thing

# (5) We use emp_1, which is an instance, and I call the method
# I do not need to pass in self, it does automatically

# (6) When we call the method on the class, and it doesn't know  what instance
# that we want to run that method with. So we do have to pass in the instance

# The program, in fact, transforms emp_1.fullname() into Employee.fullname(emp_1)
