from prac_06.guitar import Guitar


def main():
    guitars = []

    print("My Guitars!")
    name = input("Names: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input(("Cost ($): ")))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print("{} added".format(guitar_to_add))
        name = input("Names: ")


if __name__ == '__main__':
    main()