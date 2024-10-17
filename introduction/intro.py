#variable exp
'''x = input("what's your name? ")
#printing x
print("hello",x)
print("ki")'''
#various arguments in print
# print(*object, sep=' ', end='\n', file=sys.stdout, flush=False)"""

#diff way 
'''name = input("Whats your name? ")
#print("hello", name)
#this can replace as
print(f"hello, {name}")'''

#str
'''name = input("Whats your name? ")
# remove whitespace from str
name = name.strip()
# capitalize name
name = name.capitalize()
# and also use
#name = name.title()
print(f"hello, {name}")'''
# minimizing length
name = input("enter your name? ").strip().title()
#split user name
print(f"hello,{name}")