# int
'''x = int(input("what is x? "))
y = int(input("what is y? "))
print(x + y)'''
# float
'''x = float(input("what is x? "))
y = float(input("what is y? "))
print(x + y)'''
# round
# build in lib: docs.python.org/3/library/function.html#round
# round(number[, ndigits])
'''x = float(input("what is x? "))#999
y = float(input("what is y? "))#1
z = round(x + y)
print(z)'''
#print(f"{z:,}") 
#o/p: 1,000'''
x = float(input("what is x? "))#2
y = float(input("what is y? "))#3
z = x / y #0.6666666666666666
z1 = round(x / y, 2) #0.67
print(z)
# another way of print
print(f"{z:.2f}")

