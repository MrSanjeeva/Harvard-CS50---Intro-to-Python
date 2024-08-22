# Creating own module/library

def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"Hello, {name}")


def goodbye(name):
    print(f"Goodbye, {name}")


# Because of this conditional main will not get called if this module is imported in a different file
if __name__ == "__main__":
    main()
