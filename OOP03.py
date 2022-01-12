# Python Oriented Programming - Class Methods & Static Methods

# We'll learn about the difference between regular methods,
# class methods & statics methods

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {} '.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Regular methods, in a class, automatically takes the instance
    # as first variable and by convention we were calling this self
    # How we can change it to automatically takes the class instead of the instance?
    # For that we are going to use class methods and turn a regular method
    # into a class method. It is as easy as adding a decorator to the top
    # called class method
    @classmethod
    def set_raise_amt(cls, amount):
        # I took in the class and an amount
        cls.raise_amt = amount

    # Decorator is altering the functionality of our method to where now
    # we receive the class instead of the instance, by convention we use cls

    @classmethod        # We'll use this method as an alternative constructor
    def from_string(cls, emp_str):      # (4)
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)           # (5)

    @staticmethod           # (6)
    def is_workday(day):
        return not day.weekday() == 5 and not day.weekday() == 6     # Saturday or Sunday


# Here are two instances
emp_1 = Employee('Memo', 'Jimenez', 50000)
emp_2 = Employee('Test', 'User', 60000)

# We print class raise_amt & both instances raise_amt
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# We use the class method that we just create
Employee.set_raise_amt(1.05)
# It is the same as Employee.raise_amt = 1.05

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# If we run the class method from the instance still
# changes that class variable and sets all of the class
# variable and both instance
# emp_1.set_raise_amt(1.06)
# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

# Comment :  Some people say that use class methods
# as alternative constructors

# Example
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# We'll creacte an alternative constructor that allows them
# to pass in the string and we can create the employee for them
# first, last, pay = emp_str_1.split('-')
# See (4)

# new_emp_1 = Employee(first, last, pay)      # See (5)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)


# Resumeé
# Regular Mehotds pass automatically the instance as first argument self
# Class Methods pass automatically the class as first argument cls
# Static Methods don't pass anything automatically

# Example
# We want a simple function that would take in a date
# and return whether or not was a workday
# It has a logical relation with the class but actually does not
# depend on any specific instance or class variable
# See (6)

import datetime
my_date = datetime.date(2021, 1, 12)

print("Is today work day? {}".format(Employee.is_workday(my_date)))
