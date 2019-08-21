""" Martin Armstrong """


def main():
    min_length = 8
    password = get_password(min_length)
    print_hidden_password(password)


def get_password(min_length):
    password = input("Please enter a password: ")
    while len(password) < min_length:
        print("That password is less than 8 characters. Please try again.")
        password = input("Please enter a password: ")
    return password


def print_hidden_password(password):
    for i in range(len(password)):
        print("*", end="")


main()
