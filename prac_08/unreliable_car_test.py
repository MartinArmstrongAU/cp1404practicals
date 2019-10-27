from prac_08.unreliable_car import UnreliableCar


def main():
    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 9)

    for i in range(1, 12):
        print("Attempting to drive {:3}km:".format(i))
        print("{:13} drove {:3}km".format(good_car.name, good_car.drive(i)))
        print("{:13} drove {:3}km".format(bad_car.name, bad_car.drive(i)))

    print(good_car)
    print(bad_car)


if __name__ == '__main__':
    main()