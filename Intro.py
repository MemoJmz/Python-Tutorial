# Integers and FLoats - Working with Numeric Data

# Variables
num = 3
num2 = 3.14

# Return the data type
print(type(num))
print(type(num2))

# Arithmetic Operators: +, -, *, /, Foor Division //, Exponent **, Modulus %

# The fisrt four are well know for us
print("Floor Division 3//2 =", 3//2)
print("Exponent 3**2 = ", 3**2)
print("Modulus 3%2 = ", 3%2)

# Another examples about modulus
print(3%2)
print(4%2)
print(5%2)

# Order of operations
print("3*2+1 = ", 3*2+1)

# Incrementing a Variable
num = 1
num += 1
# or num = num + 1
# num *= 10
print(num)

# Methods
print(f"|-4| = {abs(-4)}")
print(f"Round of 0.463552 = {round(0.463552)}") # You can choose the number of digits with a second parameter
print(f"Round of 0.463552 = {round(0.463552, 3)}")

# Comparison Operators: ==, !=, >, <, >=, <=
# These kind of operators return a boolean value True or False

var_1 = 0.54
var_2 = 5.67

print(f"var_1 == var_2 ? {var_1 == var_2}")
print(f"var_1 != var_2 ? {var_1 != var_2}")
print(f"var_1 > var_2 ? {var_1 > var_2}")
print(f"var_1 < var_2 ? {var_1 < var_2}")

# Note the next
num_1 = '100'
num_2 = '200'
print(f"num_1 = {num_1}")
print(f"num_2 = {num_2}")

print(f"num_1 + num_2 = {num_1 + num_2}")
# Here the operator + is not the normal additions with numbers
# Here it is a concatenation of strings
# So you need maybe do a cast
num_1 = int(num_1)
num_2 = int(num_2)
print(f"num_1 + num_2 = {num_1 + num_2}")
