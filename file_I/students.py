'''
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")'''

# Converting the code into much readable formate
'''
with open("students.csv") as file:
    for line in file:
        name, city = line.rstrip().split(",")
        print(f"{name} is in {city}")'''

# Arranging the in a order
'''
with open("students.csv") as file:
    for line in sorted(file):
        name, city = line.rstrip().split(",")
        print(f"{name} is in {city}")'''

# Revercing the order
'''
with open("students.csv") as file:
    for line in sorted(file, reverse=True):
        name, city = line.rstrip().split(",")
        print(f"{name} is in {city}")'''

# To create a code that can be use both the name and city for the arrangment
# the sorted function can't directly used in dict
# So going to approch the key
'''
students = []

with open("students.csv") as file:
    for line in file:
        name, city = line.rstrip().split(",")
        student = {"name": name, "city": city}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['city']}")'''

# Changing the code for odering by the city name
'''
students = []

with open("students.csv") as file:
    for line in file:
        name, city = line.rstrip().split(",")
        student = {"name": name, "city": city}
        students.append(student)

def get_city(student):
    return student["city"]

for student in sorted(students, key=get_city):
    print(f"{student['name']} is in {student['city']}")
'''
# minimizing the length and not using function
# using the lambda
'''
students = []

with open("students.csv") as file:
    for line in file:
        name, city = line.rstrip().split(",")
        student = {"name": name, "city": city}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):# student["city"] o/p: cities order
    print(f"{student['name']} is in {student['city']}")'''

# importing csv modules to work with csv file with diffent symbol
# impoving with the corner cases
'''
import csv

students = []

with open("student1.csv") as file:
    reader = csv.reader(file)
    for name, city in reader:
        students.append({"name": name, "city": city})
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['city']}")'''

# improving by the DictReader for better understanding
'''
import csv

students = []
with open("student1.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "city": row["city"]})

for student in sorted(students, key= lambda student: student["name"]):
    print(f"{student['name']} is from {student['city']}")'''

# Writing in csv file
'''
import csv

name = input("What is your name? ")
city = input("What is your city? ")

with open("students2.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, city])'''

# Improve the performance going for Dictwriter

import csv

name = input("What is your name? ")
city = input("What is your city name? ")

with open("students2.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "city"])
    writer.writerow({"name": name, "city": city})
