# Python Oriented Programming - Special (Magic/Dunder) Methods

# We will learn about special methods that we can use within our
# clases and some people call these magic methods

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

    # Anohter two special methods
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    # We try to return a string that I can use to recreate the object

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    # This is more arbitraly, is used to be more readable for an end user

    # (4)
    def __add__(self, other):
        return self.pay + other.pay

    # (7)
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Memo', 'Jimenez', 50000)
emp_2 = Employee('Test', 'User', 60000)

#print(emp_1)

# Overloading is give more than one definition to some operator. That
# definitions depends of the context or objects wich we are working
print(1 + 2)
print('a' + 'b')
# The behavior is not the same with each kind of object

# A lot of people call the methods with double underscores "dunder"

# These are what we are going to use to fix our problem of printing out this
# vague employee object print(emp_1)
# repr(emp_1)
# str(emp_1)

# repr is met to be an unambiguous representation of the object
# and should be used for debugging and logging

# str is met to be more of a readable representation of an object and
# is met to be used as a display to the end-user

# print(repr(emp_1))
# print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())

# These methods permit us to change how our objects are printed and displayed


# There are also a lot of special methods for arithmetic
print(1+2)
print('a' + 'b')
# The dunder method is
print(int.__add__(1, 2))
print(str.__add__('a', 'b'))

# We'll create an add dunder method for Employee, see (4)
print(emp_1 + emp_2)


# There are all kinds of these special methods for arithmetic
# https://docs.python.org/3/reference/datamodel.html
# https://docs.python.org/3/reference/datamodel.html#special-method-names

# Another example
print(len('test'))
print('test'.__len__())

# We'll implement a dunder method len for Employee class which return
# the total number of character of its full name
# See (7)
print(len(emp_1))

# We'll take a look at some real-world examples in the standart library
# datetime.py module there is the dunder add method
# Another one is inside of date class, the dunder method is __repr__ or __str__
