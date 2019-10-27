from prac_06.guitar import Guitar


def run_test():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other_guitar = Guitar("Another Guitar", 2012, 1512.9)

    print("{} get_age() - expected 97. got {}".format(guitar.name, guitar.get_age()))
    print("{} is_vintage() - expected True. got {}".format(guitar.name, guitar.is_vintage()))

    print("{} get_age() - expected 7. got {}".format(other_guitar.name, other_guitar.get_age()))
    print("{} is_vintage() - expected False. got {}".format(other_guitar.name, other_guitar.is_vintage()))


if __name__ == '__main__':
    run_test()
