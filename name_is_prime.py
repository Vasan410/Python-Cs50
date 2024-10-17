name = input("enter your name: ")
n = len(name)
count = 0
for i in range(1,n+1):
    if n%i == 0:
        count += 1
if count == 2 :
    print(name,"is prime")
else:
    print(name, "not a prime")