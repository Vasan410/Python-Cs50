#syntaxError
#print("hello world)

# Value error
'''x = int(input("What is x? "))# input - cat
print(f"x is {x}")# output error
'''
# to manage these error using "try" & "except"

'''try:
    x = int(input("What is x? "))
    print(f"x is {x}")
except ValueError:
    print("The input of x in not an integer")'''

#NameError

'''try:
    x = int(input("What is x? "))
except ValueError:
    print("The input of x in not an integer")
# if the input is an string the error will be shown
print(f"x is {x}")
'''
# handling the error using the else

'''try:
    x = int(input("What is x? "))
except ValueError:
    print("the input is not an integer")
else:
    print(f"x is {x}")'''

# handling the error using the loop

'''while True:
    try:
        x = int(input("What is x? "))
    except ValueError:
        print("x is not an integer0")
    else:
        break
print(f"x is {x}")'''

# using the function

'''def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What is x? "))
        except ValueError:
            print("x is not an integer")   
        else:
            return x
main()'''

# using pass to handling the error

def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            x = int(input("What is x? "))
            return x
        except ValueError:
            pass
main()  