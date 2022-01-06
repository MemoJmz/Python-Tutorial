# Conditionals and Booleans - If, Else and Elif Statements

# Booleans: True or False

if True:
    print('Conditional was True')

if False:
    print('Conditional was False')

language = 'Python'
print(f"language == Python ? {language=='Python'}")

# Comparisons:
# Equal             ==
# Not Equal         !=
# Greater Than      >
# Less Than         <
# Greater or Equal  >=
# Less or Equal     <=
# Object Identity   is

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


# If, elif (like switch), Else
language = 'Java'

if language == 'Python':
    print('Python')
elif language == 'Java':
    print('Java')
elif language == 'JavaScrip':
    print('JavaScrip')
else:
    print('No match')

# And, Or, Not
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print("Admin Page")
elif user == 'Admin' or logged_in:
    print("User or logged_in wrong")
else:
    print("Bad Creds")

# Not
user = 'Admin'
logged_in = True

if not logged_in:
    print("Please Log In")
else:
    print('Welcome')

# Two object can be equal and not be the same object in memory
a = [1, 2, 3]
b = [1, 2, 3]

print(f"a = {a}")
print(f"b = {b}")

# They are equal but not the same object
print(f"a == b ? {a == b}")
print(f"a is b ? {a is b}")

# Build-in method ID, return the locations of the objects
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
b = a
print("b = a")
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print(f"a is b ? {a is b}") # id(a) == id(b) ?
print(f"a == b ? {a == b}")


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. F.e., '', (), [].
    # Any empty mapping (empty dictionary). F.e, {}.

# condition = False
# condition = None
# condition = 0
# condition = ''
# condition = {}

condition = 'Test'

if condition:
    print('\nEvaluated to True')
else:
    print('\nEvaluated to False')

# This way you can check if you object are empty or not without any method
