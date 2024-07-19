# # Nesting a function - Here return value of input function becomes the arg of the int function
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# add = round(x+y)
# # divide = round(x / y, 2)
# divide = x/y

# print(f"{add:,}")
# print(f"{divide:.2f}")

def main():
    x = int(input("What's x? "))
    print("x square is", square(x))


def square(num):
    return pow(num, 2)


main()
