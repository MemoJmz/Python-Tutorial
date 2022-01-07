# Functions

# hello function whithout parameters
def hello_func():
    pass

# We can leave completely in blanck the body of the function
# we use pass for that

# For run a function
print(hello_func())

# To get its location in memory
print(hello_func)


def hello_func():
    print('Hello Function!!')

hello_func()

# Fucntions are useful to avoid repeat code

def hello_func():
    return 'Hello Function.'

hello_func()
print(hello_func())

# Example
print(f"len('Test') = {len('Test')}")
print(f"hello_func().upper() = {hello_func().upper()}")

# Send parameters
def hello_func(greeting):
    return '{} Function.'.format(greeting)

print(hello_func('Hello'))

# name is a parameter which if it is not especify takes 'You' by default
def hello_func(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)

print(hello_func('Hello'))
print(hello_func('Hi', 'Memo'))
# or
print(hello_func('Hi', name = 'Memo'))

# When you don't know how many variables you will be using
# This way is useful to send several argument, the name args &
# kwargs is just a convention
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name = 'John', age=22)

# Sometimes you may see a function call with arguments using the star or double star
# now, when it is used in that context it will actually unpack a sequence or dictionary
# and pass those values into the function individually

courses = ['Math', 'Art']
info = {'name':'John', 'age':22}

# We want to pass courses like positional arguments
# & info like keyword arguments
student_info(courses, info)         # wrong way
student_info(*courses, **info)      # correct way


##### ---- ##### More examples ##### ----- #####

# Number of days per month. Fist value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(f"is_leap(2017) ? {is_leap(2017)}")
print(f"is_leap(2020) ? {is_leap(2020)}")

print(f"days_in_month(2017, 2) = {days_in_month(2017, 2)}")
