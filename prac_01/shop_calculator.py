number = int(input("Number of items: "))
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))

total_price = 0
for i in range(number):
    price_of_item = float(input("Price of Item: "))
    total_price += price_of_item

if total_price > 100:
    discount = total_price / 10
    total_price -= discount

print("Total price for " + str(number) + "items is $" + str(total_price))
