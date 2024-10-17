# tuple
'''
def main():
    #name, city = get_student()
    student = get_student()
    #print(f"{name} from {city}")
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    city = input("City: ")
    return (name,city) # comma represent as tuple

if __name__ == "__main__":
    main()'''

# Classes and Object 
'''
class Student:
    ...# empty place will give the error, so passing using the ...
    
def main():
    student = get_student()
    print(f"{student.name} from {student.city}")

def get_student():
    student = Student() # creating a object for the class
    student.name = input("Name: ")
    student.city = input("City: ")
    return student

if __name__ == "__main__":
    main()'''

# Methods
# __init__ is used to make content on object within the class
'''
class Student:
    def __init__(self, name, city):# initialize the content of object
        self.name = name #instict variable
        self.city = city #instict variable

def main():
    student = get_student()
    print(f"{student.name} from {student.city}")

def get_student():
    name = input("Name: ")
    city = input("City: ")
    student = Student(name, city)
    return student

if __name__ == "__main__":
    main()
'''
# "raise" it is used for Value errors 
'''
class Student:
    def __init__(self, name, city):# self is an arrgument
        if not name: # if name == ""
            raise ValueError("Missing name")
        if city not in ["Cuddalore", "Pondy", "Villupuram"]:
            raise ValueError("Invalid city")
        self.name = name
        self.city = city
                

def main():
    student = get_student()
    print(f"{student.name} from {student.city}")

def get_student():
    name = input("Name: ")
    city = input("City: ")
    return Student(name,city)

if __name__ == "__main__":
    main()'''

# __str__ it is a method defined in class. any time the user calls the function it will occur

class Student:
    def __init__(self, name, city):
        if not name:
            raise ValueError("Missing name")
        if city not in ["Cuddalore", "Pondy", "Villupuram"]:
            raise ValueError("Invalid city")
        self.name = name
        self.city = city

    def __str__(self):
        return (f"{self.name} from {self.city}")
    
def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    city = input("City: ")
    return Student(name,city)

if __name__ == "__main__":
    main()
        
# Properties