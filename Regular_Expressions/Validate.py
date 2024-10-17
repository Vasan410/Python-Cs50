'''
email = input("What is your email? ").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("Valid")
else:
    print("Invalid")'''

# it also as some limitations so overcoming those limitations coming to another way
'''
email = input("What is your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".com"):
    print("Valid")
else:
    print("Invalid")'''

# to overcome some more limitations going for "re" library
# '.' - any character except a newline
# '*' - 0 or more repetitions
# '+' - 1 or more repetitions
# '?' - 0 or 1 repetition
# '{m}' - m repetitions
# '{m,n}' - m to n repetitions
'''
import re

email = input("What is your email? ").strip()

if re.search(r".+@.+\.com", email):# r is used to work with \, is suprating the statements
    print("Valid")
else:
    print("Invalid")'''
    
# ^ - matches the start of the string
# $ - matches the end of the string or just before the newline at the end of the string
'''
import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.com$", email):
    print(f"{email} is Valid")
else:
    print(f"{email} is Invalid")'''

# [] - set of character
# [^] - complementing the set
'''
import re

email = input("What's your email? ")

if re.search(r"^[^@]+@[^@]+\.com$", email):
    print(f"{email} is Valid")
else:
    print(f"{email} is Invalid")'''

# And enhancing the more efficiency by mentioning the words and symbols must be used
'''
import re

email = input("What's your email? ")

if re.search(r"^[a-z0-9_]+@[^@]+\.com$", email):
    print(f"{email} is Valid")
else:
    print(f"{email} is Invalid")'''

# \d - decimal digit
# \D - not a decimal digit
# \s - whitespace characters
# \S - not a whitespace character
# \w - word character...as well as number and underscore
# \W - not a word character
# A|B - either A or B
#(...) - a group
#(?:...) - non-capturing version

import re

email = input("What's your email? ")

if re.search(r"^\w+@\w+\.(com|net|org|edu|gov)$", email):
    print(f"{email} is Valid")
else:
    print(f"{email} is Invalid")

# if i want to ignore any case i can directly add the flag as re.IGNORECASE

