# Loops and Iterations - For/While Loops

nums = [1, 2, 3, 4, 5]

# Easy for loop
for num in nums:
    print(num)

# Break And Continue
# break ends with the loop
# continue jumps and ends with the actual iteration

# Example 1
for num in nums:
    print(num)
    if num == 3:
        print("Found!")
        break

# Example 2
for num in nums:
    if num == 3:
        print("Found!")
        continue
    print(num)

# Example 3
for num in nums:
    for letter in 'abc':
        print(f"<num, letter> = <{num}, {letter}>")


# Range Function
for i in range(10):
    print('i = ', i)
# It does not include 10

# To start in 1
for i in range(1, 11):
    print('i = ', i)


# While loop
x = 0
while x < 10:
    if x==5:
        break
    print(x)
    x += 1

# If you want a infinite loop
j = 0
while True:
    print(j)
    j += 1


# To cancel the loop Ctrl + c
# Be careful, writte a break condition
