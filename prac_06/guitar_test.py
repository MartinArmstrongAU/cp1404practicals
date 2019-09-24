from prac_06.guitar import Guitar


def run_test():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)

    print("{} get_age() - expected 97. got {}".format(guitar.name, guitar.get_age()))
    print("{} is_vintage() - expected True. got {}".format(guitar.name, guitar.is_vintage()))


if __name__ == '__main__':
    run_test()
