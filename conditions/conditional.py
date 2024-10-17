#compare
#using if
'''x = int(input("wht is x? "))
y = int(input("wht is y? "))
if x > y:
    print("x is greater than y")
if x < y:
    print("x is less than y")
if x == y:
    print("x is equal to y")'''

#using elif for much faster result
'''x = int(input("wht is x? "))
y = int(input("wht is y? "))
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
elif x == y:
    print("x is equal to y")'''

#using else musch more faster result
'''x = int(input("wht is x? "))
y = int(input("wht is y? "))
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")'''

#or
'''x = int(input("wht is x? "))
y = int(input("wht is y? "))
if x > y or x < y:
    print("x is not equal to y")
else:
    print("x is equal to y")
'''
#simplifing the program
x = int(input("wht is x? "))
y = int(input("wht is y? "))
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")