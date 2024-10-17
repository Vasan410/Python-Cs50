'''print("#")
print("#")
print("#")'''

# using loop for printing "#"

'''for i in range(3):
    print("#")
'''
# using functions and loop for printing column "#"

'''def main():
    print_column(3)

def print_column(height):
    #for _ in range(height):
        print("#\n" * height)

main()
'''
# using functions for printing row "#"

'''def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()'''

# Creating a square

'''def main():
    print_square(5)

def print_square(size):
    # For each row in sqaure
    for i in range(size):
        # For each brick in row
        for j in range(size):
            #printing brick
            print("#", end="")
        #printing the brick in row
        print()
        
main()'''

# Optimizing the code size

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)

main()                    