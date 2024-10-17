# sys.argv
# command line argument
'''import sys

print("hello, my name is", sys.argv[1])'''

# to avoiding the error using the "try" & "except"
 
'''import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few argument")'''

# using the "if" condition overcoming the error

'''import sys
if len(sys.argv) > 2:
    print("Too many argument")
elif len(sys.argv) < 2:
    print("Too many argument") 
else:
    print("hello, my name is", sys.argv[1])'''

# modifing the code

'''import sys
if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Too many argument")
else:
    print("Hello, my name is", sys.argv[1])
'''
# sys.exit

'''import sys

if len(sys.argv) > 2 or len(sys.argv) < 2:
    sys.exit("Too many aargument")
print("Hello, my name is", sys.argv[1])'''

# Using for loop

'''import sys
if len(sys.argv) < 2:
    sys.exit("Too many argument")
for arg in sys.argv:
    print("Hello, my name is", arg)'''

# to overcome the bug the slice : is used

import sys

if len(sys.argv) < 2:
    sys.exit("Too many argument")
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)