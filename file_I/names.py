'''
names = []

for _ in range(3):
    name = input("What is your name? ")
    names.append(name)

for name in names:
    print(f"Hello, {name}")'''

# using open keyword
# and also writing into the file

'''
name = input("What is your name? ")
file = open("names.txt","w")# just writing inside file
file.write(name)
file.close'''

# In this case the commands are just used to write the code, it will not save the code.
# So we are going to append condition.
'''
name = input("What is your name? ")
file = open("names.txt", "a")
file.write(name)
file.close
'''
# to over come the bug for suprate name, going to include /n
'''
name = input("What is your name? ")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close'''

# To minimize the length and without using of close. Going for "with" keyword.
'''
name = input("What is your name? ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")'''

# Now going to read the lines from the file
'''
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line)'''

# To minimize the length of code and spacings.
'''
with open("names.txt", "r") as file:
    for line in file:
        print("Hello,",line.rstrip())'''

# To arrange the data in specific order, using "sorted" key word.
'''
names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")'''

# To minimize the length of the code
'''
with open("names.txt", "r") as file:
    for line in sorted(file):
        print(f"Hello,",line.rstrip() )'''

# Changing the code for reverse order

with open("names.txt", "r") as file:
    for line in sorted(file, reverse=True):
        print(f"Hello,",line.rstrip())

