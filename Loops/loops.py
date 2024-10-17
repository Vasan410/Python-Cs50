# While loop
'''i = 3
while i != 0:
    print("meow")
    i -= 1'''

# Another way
'''i = 0
while i < 3:
    print("meow")
    i += 1'''

# for loop
'''for i in [0, 1, 2]:
    print("meow")'''

# Another type
'''for i in range(3):
    print("meow")'''
# print("meow\n" * 3)

# using both loops to avoid invalid inputs
'''while True:
    n = int(input("What is n? "))
    if n > 0 :
        break
for _ in range(n):
    print("meow")'''

# using functions

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()

