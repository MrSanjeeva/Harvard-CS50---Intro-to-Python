def main():
    name = input("What's your name? ")
    print(hello(name))


def hello(to="world"):
    # print("Hello,", to)
    return f"Hello, {to}"


if __name__ == "__main__":
    main()
