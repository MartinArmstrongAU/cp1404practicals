import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_LINE = 6


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        row_numbers_generated = calculate_row_numbers()
        row_numbers_generated.sort()
        print(" ".join("{:2}".format(number) for number in row_numbers_generated))


def calculate_row_numbers():
    numbers = []
    for i in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in numbers:
            number = random.randint(MINIMUM, MAXIMUM)
        numbers.append(number)
    return numbers


main()
