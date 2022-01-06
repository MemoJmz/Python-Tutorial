# Dictionaries - Working with Key-Value Pairs

# Example
students = {'name':'John', 1:25, 'courses':['Math', 'CompSci']}
print(students)
# Acces to some key
print(students['name'])
#or
print(students.get('name'))
# If you put a value like key you will get
print(students[1])
# Keys could be strings or values

# You will get a error if you try to acces with unexisting Keys
# If use the method get you'll get None instead of an error
print(students.get('phone'))
# You can specify the message
print(students.get('phone', 'Not Found'))

# Get a new entry to that dictionary
students['phone'] = '555-5555'
print(students)
# If the key exists, that method just will update the value

# To update mora than one entry use the method update
students.update({'name':'Jane', 'age':26, 'phone':'555-5556'})
print(students)

# Delete a specific key
del students['name']
print(students)
# or use the method pop and get that value
age = students.pop('age')
print(age)
print(students)

# We can loop through our dictionary (the way is seemed as lists)
students = {'name':'John', 'age':25, 'courses':['Math', 'CompSci']}
print(len(students))
print(students.keys())
print(students.values())

print(students.items())

for key in students:
    print(f"key : {key}")

print(' key  ->   value')
for keys, values in students.items():
    print(f"{keys} -> {values}")
