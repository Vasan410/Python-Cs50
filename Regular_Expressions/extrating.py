# twitter
'''
url = input("URL: ").strip()
print(url)'''

# printing the username from the url
'''
url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")'''

# Too overcome some errors going for importing lib
'''
import re 

url = input("URL: ").strip()
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")'''

# it is not more efficient so going for re.search
'''
import re

url = input("URL: ").strip()
if username := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", username.group(2))'''

# changing to little more comfortable

import re 
url = input("URL: ").strip()
if username := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_])+$", url, re.IGNORECASE):
    print(f"Username:", username.group(1) )

