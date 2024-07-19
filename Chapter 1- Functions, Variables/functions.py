# --------- Functions -------- #

# A function needs to be defined at the top of the file

# def is short for define used to create functions
def main():
    hello()
    name = input("What's your name? ").title()
    hello(name)

# Define a function to say hello


def hello(to="World"):  # Here the argument to is given a default value if the function is called without any arguments
    print(f"Hello! {to}")


main()
