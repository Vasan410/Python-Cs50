'''
name =  input("What is your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"

print(f"hello, {name}")
'''
# to overcome some limitations going for importing "re" library
'''
import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")'''

# to overcome with the space limitation going for another method
'''
import re 

name = input("What's your name? ")
matches = re.search(r"^(.+), *(.+)$", name)

if matches:
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello, {name}")'''

# and also using a := to reduce the length of program

import re

name = input("What's your name? ")
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello, {name}")