# print("meow")
# print("meow")
# print("meow")
# print("meow\n" * 3, end="")

# -- While Loop
# i = 3
# while (i != 0):
#     print("meow")
#     i -= 1

# i = 0
# while (i < 3):
#     print("meow")
#     i += 1

# -- for loop
# for i in [0, 1, 2]:
#     print("meow")

# for _ in range(3):  # range goes upto 3 but not 3
#     print("meow")
# We can use _ instead of i as we need it but we don't use it anywhere else
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for i in range(n):
#     print("meow")

def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        x = int(input("What's x? "))
        if x > 0:
            return x


def meow(n):
    for _ in range(n):
        print("meow")


main()
