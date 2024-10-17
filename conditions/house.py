'''name = input("Wht is your name? ")
if name == "Harry":
    print("Gryffindor")
elif name == "Hermoine":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
#if name == "Harry" or name == "Hermoine" or name == "Ron":
    #print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")'''
# using Match keyword:
'''name = input("What is your name? ")
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermoine":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")'''

# Modifing the code much easy

name = input("What is your name? ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")