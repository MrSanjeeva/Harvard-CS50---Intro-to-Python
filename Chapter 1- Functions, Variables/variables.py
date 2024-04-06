# --------- Variables ----------- #

# Ask user for their name
# Here = will assign the return value of the input function to name variable
name = input("What's your name? ").strip().title()

# Remove whitespace from str and capital user's name
# name = name.strip().title()

# Capitalize user's name
# name = name.capitalize()

# # Capitalize user's full name
# name = name.title()

# Split user's name into first name and last name
first, last = name.split(" ")

# # Say hello to user
# # print("Hello, " + name) # A one big argument is passed into the print function
# # print ("Hello,",name) # Here two arguments are passed
# print("Hello, ",end='') # Here Hello is a positional parameters and end/sep is a named parameters
# print(name)
print(f"Hello, {name}")


# Escpaing #
# print("Hello,\"friend\"") # or print('Hello, "friend"')
