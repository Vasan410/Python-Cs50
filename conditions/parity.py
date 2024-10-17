'''x = int(input("What is x? "))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")'''

# using function

def main():
    x = int(input("What is X? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0
    #return True if n % 2 == 0 else False
''' if n % 2 == 0:
# using the boolen :
        return True
    else:
        return False'''

main()