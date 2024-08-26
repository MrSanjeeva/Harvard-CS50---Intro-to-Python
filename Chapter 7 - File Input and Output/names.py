# A program that collects names

# names = []

# for _ in range(3):
#     names.append(input(f"What's your name? "))

# for name in sorted(names):
#     print(f"Hello, {name}")

#  Write names
# name = input("What's your name? ")
# print(f"Hello, {name}")

# Open returns a file handle. Here "w" - write, "r" - read, "a" - append
# file = open("names.txt", "a")
# file.write(f"{name}\n")  # Write the name to the file names.txt
# file.close()  # Close the file and save it

# When we use the with keyword we do not have to manually close the file
# with open("names.txt", "a") as file:
#   file.write(f"{name}\n")  # Write the name to the file names.txt

# Reading names from the txt file and printing them
# with open("names.txt", "r") as file:
#     lines = file.readlines()
# for line in lines:
#     # print("Hello,", line, end="")
#     print("Hello,", line.rstrip())

#  Optimized way of reading lines from the text file and printing them
# with open("names.txt", "r") as file:
#     for line in file:
#         print("Hello,", line.rstrip())

# Sorting names from the txt file by reading them and printing them
# names = []

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"Hello, {name}")

# Optimized sorting
# with open("names.txt") as file:
#     for line in sorted(file):
#         print(f"Hello,", line.rstrip())

# To make changes to the data
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"Hello, {name}")
