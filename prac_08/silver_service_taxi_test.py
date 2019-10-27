from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Hummer", 200, 4)
    print(taxi)
    print("${:.2f}".format(taxi.get_fare()))

    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print("${:.2f}".format(taxi.get_fare()))


if __name__ == '__main__':
    main()
