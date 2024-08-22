#  Command-line arguments
# sys module
import sys

# sys.argv -> argv is short for argument vector. This is a list.

# if len(sys.argv) < 2:
#     print("Usage: python name.py <your_name>")
# elif len(sys.argv) > 2:
#     print("Too many arguments.")
# else:
#     print("Hello, my name is", sys.argv[1])

# try:
#   print("Hello, my name is", sys.argv[1])
# except IndexError:
#   print("Usage: python name.py <your_name>")

# # Check for errors
# if len(sys.argv) < 2:
#     sys.exit("Usage: python name.py <your_name>")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments.")

# # Print name tags
# print("Hello, my name is", sys.argv[1])

# Check for errors
if len(sys.argv) < 2:
    sys.exit("Usage: python name.py <your_name>")

# Print name tags
# If we do not use slice we will get four elements starting from arg[0]
# Here [1:] takes the slice of the list from 1st element to the end
# We can also use [1:-1] which will count from the end of the list to the beginning hence ommiting the last name
for arg in sys.argv[1:-1]: 
    print("Hello, my name is", arg)

# In python if we want to take a subset of list we use slices.
# Slice is subset of a data structure like a list
