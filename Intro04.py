# List, Tuples & Sets

# Listas has more functionality that the other data types
courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses)
print(len(courses))

# To acces to values in our List
print(courses[0])
print(courses[-1]) # Access the last item

# Return the values of the list in reverse order
print(courses[::-1])

# Return a sublist
print(courses[:2]) # The second item is not including

# To add a item in our list we use the append method
courses.append('Music')
print(courses)
# And for add it in a specific location we use a insert method and a second parameter (first) with the position
courses.insert(0, 'Art')
print(courses)

# Extend method is another way to add items
# We use it when we need to add multiple values to our List
courses_2 = ['Art', 'Language']
# If we use insert method, it inserts the courses_2 list to courses list
courses.insert(0, courses_2)
print(courses)
print(courses[0])


courses = ['History', 'Math', 'Physics', 'CompSci']
courses.extend(courses_2)
print(courses)

# To remove some values of our list
courses.remove('Math')
print(courses)

# or we use the method pop and get that item
# by defult this removes the last value of our list
# It is helpful if we want to use our list like a stack or queue
courses.pop()
popped = courses.pop() # to get the last item like a object
print(courses) # and do this until our list will be empty
print(popped)

# To reverse our list, and does not only get the item in reverse order
courses.reverse()
print(courses)

courses.extend(['Literature', 'Music'])

# For sort our list
courses.sort()
print(courses) # the list is sorted by alphabetical order

nums = [4, 1, 2, 5, 7, 8, 3]
nums.sort()
print(nums)

# To sort the list in descending order
nums.sort(reverse=True)
print(nums)

# We do not need to reset our variables when we call most of these methods
# We can get a new list with the original sorted
nums = [4, 1, 2, 5, 7, 8, 3]
print(f'nums = {nums}')
sorted_nums =  sorted(nums)
print(sorted_nums)

# min, max & sum
print(f'min(nums) = {min(nums)}')
print(f'max(nums) = {max(nums)}')
print(f'sum(nums) = {sum(nums)}')



courses = ['History', 'Math', 'Physics', 'CompSci']
print(f'courses = {courses}')
# Find the index of certain value
print(f"courses.index('CompSci') = {courses.index('CompSci')}")

# Something interesting
print(f"'Art' in courses = {'Art' in courses}")
print(f"'Math' in courses = {'Math' in courses}")

# We can also use a loop through values of our list
for item in courses:
    print(f"'{item}' in courses = {item in courses}")
    print(item)

# Enumerate function
for index, course in enumerate(courses):
    print(f"<index, course> = <{index}, {course}>")

# we can also start the index with another value enumerate(courses, start=1)

# It is common turning lists to strings
courses = ['History', 'Math', 'Physics', 'CompSci']
# for that we'll use a string method called join
course_str = ', '.join(courses)
print(course_str)
# or ' - '
course_str = ' - '.join(courses)
print(course_str)

# A reverse method of the previous
# We get a list from a string
new_list = course_str.split(' - ')
print(new_list)


##########
##########
# Tuples & Sets

# Tuples are similar to List but we can't modify tuyples
# List are mutable
# Tuples are immutable

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

# Return the same list because the are both the same mutable object
# If you want a list of values that does not change you really need a tuple

# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art' # This line produces a error

print(tuple_1)
print(tuple_2)

# Since a tuple is immutable it does not have nearly as many methods as a list
# We can use loop with list, access to values, but we can't mutate values


#######
#######
# Sets are values that are unordered
# and also have no duplicates

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}

print(cs_courses)
# You will get a different result wiht each execution

# Sets are useful to remove duplicate values
# membership test: Sets are used to test whether a value is part of the set
# and sets do that more efficently than lists or tuples
print('Math' in cs_courses)
# Sets also do quikly is determine what values they share or do not share with other sets

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

# What courses these sets had in common?
# We use the Itersection Method
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))


# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Set
empty_set = {} # This isn't right. It's a dict
empty_set = set()
