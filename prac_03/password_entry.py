""" Martin Armstrong """


def main():
    min_length = 6
    password = get_password(min_length)
    print_hidden_password(password)


def get_password(min_length):
    password = input("Please enter a password that is at least {} characters: ".format(min_length))
    while len(password) < min_length:
        print("That password is less than {} characters. Please try again.".format(min_length))
        password = input("Please enter a password that is at least {} characters: ".format(min_length))
    return password


def print_hidden_password(password):
    print("*" * len(password))


main()
