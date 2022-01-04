# Print Welcome Message

# String
message = 'Hello World'

print(message)

# We can know the lenght of the String
print(len(message))
# We can also acces to each character
print(message[0])
# Or part of the string
print(message[0:5])
print(message[6:])
# Message in lower
print(message.lower())
# The count of strings "l" in message
print(message.count('l'))

# Return the index position of the string in message
print(message.find('llo'))

# Replace Method, return a new string, it needs two parameters
message2 = message.replace('World', 'Universe')

print(message)
print(message2)

# Concatenate strings
greeting = 'Hello'
name = 'Michael'
lastname = 'Jimenez'

message = greeting + ', ' + name + ' ' + lastname + '. Welcome!'
print(message)

# For the last case it is better use a formatted strings
message = '{}, {} {}. Welcome!'.format(greeting, name, lastname)
print(message)

# If we are using Python 3.6 or above we can use f strings
message = f'{greeting}, {name} {lastname}. Welcome!'
print(message)

# Something more amazing is we can use methods inside the placeholder
message = f'{greeting}, {name.lower()} {lastname.upper()}. Welcome!'
print(message)

# dir function
# If we use this function it will show us all of the attributes and methods that
# we have access
print(dir(name))
# or print(dir(str))

# After seeing all of the methods and attibutes available to this variable
# we notices that we can get more information about its use
# For that reason exist the help function
# print(help(str))
# for an exact definition
print(help(str.lower))
