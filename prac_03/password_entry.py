""" Martin Armstrong """

min_length = 8
password = input("Please enter a password: ")
while len(password) < min_length:
    print("That password is less than 8 characters. Please try again.")
    password = input("Please enter a password: ")

for i in range(len(password)):
    print("*", end="")
