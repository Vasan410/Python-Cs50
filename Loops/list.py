'''students  = ["vasan", "jo", "keerthi"]
print(students[0])
print(students[1])
print(students[2])
'''
# Using loop 

'''students = ["vasan", "jo", "keerthi"]
for i in students:
    print(i)'''

# modifing the code

'''students = ["vasan", "jo", "keerthi"]
for i in range(len(students)):
    print(i + 1, students[i])
'''

# using dict

'''students = {
            "Vasan": "Cuddalore",
            "Jo": "Pondy",
            "Keerthi": "Cuddalore"
            }
print(students["Vasan"])
print(students["Jo"])
print(students["Keerthi"])'''

# using loop in dict

'''students = {
    "Vasan": "Cuddalore",
    "Jo": "Pondy",
    "Keerthi": "Cuddalore"
    }
for i in students:
    print(i, students[i], sep = ",")'''

# Creating dict in list

students = [
    {"Name": "Vasan","City": "Cuddalore","Age": "20"},
    {"Name": "Jo", "City": "Pondy", "Age": "21"},
    {"Name": "Keerthi", "City": "Coddalore", "Age": None}
]
for student in students:
    print(student["Name"], student["City"], student["Age"], sep = ",")
    