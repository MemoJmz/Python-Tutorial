# Import Modules and Exploring The Standard Library

# To import a module
# import my_module
# my_module is in the same directory as my Intro09.py
# so we can directly import it and use it all code in that file

# or
# import my_module as mm

# courses = ['History', 'Math', 'Physics', 'CompSci']

# We can use functions in the module in this way
# index = mm.find_index(courses, 'Math')
# print(index)

# To import a particular function of a module
# from my_module import find_index
# We don't need writte
# mm.find_index(courses, 'Math') -> find_index(courses, 'Math')

# Int he same way, add an nickname to that function
# from my_module import find_index as fi

# To import more than one function of a module use comma
# from my_module import find_index as fi, test
# print(test)

# Another way is importing everything without use the name of the module is
# form my_module import *
# it is not recommendable because there would be probems with functions
# with the same name

# How python find the module if we do not include any path?
# When we import a module it checks multiple locations and the
# locations that it's checks is within a list called 'sys.path'
# We can actually see this list if we import the sys module

# import sys
# print(sys.path)

# The first value is hte directory where I am currently running the script
# from and the my module python file that that we were importing is within that
# directory

# So, what directories are added to this sys.path list?
# Directories are added in this order
# 1.- The directory containing the script that we're running
# https://youtu.be/CqvZ3vGoGs0?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&t=452


# If que do not have the module in the same location as our file
# import sys
# sys.path.append('Users/....')

# from module import functions


# Standard Library
import random       # generate & manipulate random numbers
import math         # mathematical operations
import datetime     # work with date & time
import calendar
import os           # This is going to give us access to the underlying
                    # operating system


courses = ['History', 'Math', 'Physics', 'CompSci']

# random
random_course = random.choice(courses)
print(random_course)

# math
rads = math.radians(90)
print(rads)
print(math.sin(rads))

# datetime
today = datetime.date.today()
print(today)

#calendar
print(calendar.isleap(2022))

# os
# if I wanted to see what directory we are currently working
print(os.getcwd())


# We can find the location of each Python module, each one is itself a python file
print(os.__file__)

# Joke of Python Community
# import webbrowser
# import hashlib

# webbrowser.open("https://xkcd.com/353/")
