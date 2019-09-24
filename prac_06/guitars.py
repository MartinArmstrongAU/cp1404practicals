from prac_06.guitar import Guitar


def main():
    guitars = []

    print("My Guitars!")
    # name = input("Names: ")
    # while name != "":
    #     year = int(input("Year: "))
    #     cost = float(input("Cost ($): "))
    #     guitar_to_add = Guitar(name, year, cost)
    #     guitars.append(guitar_to_add)
    #     print("{} added.".format(guitar_to_add))
    #     name = input("Names: ")

    guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        guitars.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print(
                "Guitar {}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {}".format(i, vintage_string,
                                                                                                      guitar=guitar))
    else:
        print("No guitars :( Quick, go and buy one!")


if __name__ == '__main__':
    main()
