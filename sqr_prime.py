import math as M
n = int(input("enter a number: "))
count = 0
for i in range(1,int(M.sqrt(n)) + 1):
    if n % i == 0:
        print(i)
        if n/i != i:
            print(n/i)
            print("prime")
        else:
            print("Repeat")
    else:
        print("not prime")