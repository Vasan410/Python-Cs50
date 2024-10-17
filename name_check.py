import re

username = input("What's your name? ").strip()
name = re.search(r"^(.+) (.+)$",username,re.IGNORECASE)

print(f"Name:", name.group(1))
