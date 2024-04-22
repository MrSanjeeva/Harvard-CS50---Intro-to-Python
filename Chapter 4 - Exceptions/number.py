# ------ Exception handling -------- #
# There are mainly two types of errors -
# 1. SyntaxError - Needs to be fixed
# 2. RuntimeError - Error happens while the code is running and we need to write additional code defensively to detect when those errors happen. Error examples - ValueError, NameError,
# We never know what the user might type into the input, so we need to be ready defensively to accomodate things that they type or mistype

# x = int(input("What's x? "))
# print(f"x is {x}")

# ValueError handling
# We can use 'try' and 'except' to accomodate for runtime errors
# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")

# print(f"x is {x}") # We get a NameError: name x is not defined because the error is occuring in the int function therefore no value is being assigned to the x variable. Therefore the variable x is not being defined.

# NameError handling
# We can use 'try', 'except','else'
# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

# Improving the code by adding a loop to give user multiple opportuinity to enter an int
# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break

# print(f"x is {x}")

# Using function
# def main():
#     x = get_int()
#     print(f"x is {x}")


# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#             # return function will break out of the loop and also returns a value.
#         except ValueError:
#             print("x is not an integer")


# main()

# 'pass' statement
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
            # return function will break out of the loop and also returns a value.
        except ValueError:
            pass  # It catches the exception but passes on it without explicitly stating anything


main()
