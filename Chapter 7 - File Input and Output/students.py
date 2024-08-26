# Sorting the list from students names

# import csv

# with open("students.csv") as file:
#     for line in sorted(file):
#         # row = line.rstrip().split(",")
#         name, house = line.rstrip().split(",")  # Split function comes with str
# print(f"{name} is in {house}")
#  Here the sorting happen with the print statement and not with the name of the student

# Sorting with the name of the student first and then printing

# students = []

# with open("students.csv") as file:
#     for line in file:
#         # name, house = line.rstrip().split(",")
#         name, home = line.rstrip().split(",")
#         # student = {}
#         # student["name"] = name
#         # student["house"] = house
#         # Optimised way of writing and filling a dictionary
#         # Dictionary comprehension to create student dictionary from line.split(",")
#         # student = {"name": name, "house": house}
#         student = {"name": name, "home": home}
#         # students.append(student)  # This would append the entire dictionary, not just the key-value pairs (AI Generated comment)
#         students.append(student)


# def get_name(student):
#     return student["name"]


# def get_house(student):
#     return student["house"]


# for student in sorted(students, key=get_name):
#     # We need to differentiate between the line and key so we use single quotes for keys(name, house)
#     print(f"{student['name']} is in {student['house']}")

# print("\n")

#  Sorting with the house name first and then printing
# for student in sorted(students, key=get_house):
#     # We need to differentiate between the line and key so we use single quotes for keys(name, house)
#     print(f"{student['name']} is in {student['house']}")

# for student in sorted(students, key=lambda student: student["name"]):
#     # We need to differentiate between the line and key so we use single quotes for keys(name, house)
#     print(f"{student['name']} is in {student['house']}")
# key = lambda student: student["name"] is the same as  get_name function defined earlier. If we use the function once and never call it again we can use a lambda function(anonymous function) instead of creating a function

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

# CSV reader
# with open("students.csv") as file:
#     reader = csv.reader(file) # Reader returns a list
#     for name, home in reader:
#         students.append({"name": name, "home": home})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

# CSV dictionary -  For this we need to mention the column names in the csv file
# with open("students.csv") as file:
#     reader = csv.DictReader(file)  # DictReader returns Dictionary
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})
#         students.append(row)

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

# Using user input date to create a csv

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

# # CSV Writer
# with open("yournames.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

# CSV DictWriter
with open("yournames.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
