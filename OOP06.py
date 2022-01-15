# Python Oriented Programming - Property Decorators
# Getters, Setters, and Deleters

# We'll learn how to use the property decorator
# This allows us to give our class attributes getter, setter and leader fucntionality

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {} '.format(self.first, self.last)

    @fullname.setter        # (2) We need to create another metod with the same name
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter        # (3)
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')

emp_1.first = 'Jim'
# This will not change the email, the fullname methods does not have this problem

print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname())

# The reason is email is made when we create the instance, if we only change the name,
# the email still remains the same, que fullname methods changes because it checks
# the current attribute first

# We want to change the email automatically each time that the name changes
# We change email from attribute to be a method

# print(emp_1.first)
# print(emp_1.email())
# print(emp_1.fullname())

# def email(self):
#     return '{}.{}@email.com'.format(self.first, self.last)

# We do nor want to change our code in this way
# To keep the order as print(emp_1.email), this means, to keep as attribute
# We can just add a property decorator above this method '@property'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# Run the code to see that that works
# email is a methods but we're able to access it like an attribute
# We can do the same for fullname method

# Now, we want to set
# emp_1.fullname = 'Corey Schafer'
# If we run this, we'll see that we can't set the attibute
# We use a setter, for this we use the decorator the name of the property
# See (2)

emp_1.fullname = 'Juan Marcos'
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# We can also make a deleter in the same way
# (3)

del emp_1.fullname
