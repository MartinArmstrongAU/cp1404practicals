output_file = open("name.txt", "w")
user_name = input("Please enter your name: ")
print(user_name, file=output_file)
output_file.close()

input_file = open("name.txt", "r")
name = input_file.read().strip()
print("Your name is", name)
input_file.close()

input_file = open("numbers.txt", "r")
first_number = int(input_file.readline())
second_number = int(input_file.readline())
numbers_combined = first_number + second_number
print(numbers_combined)
input_file.close()

input_file = open("numbers.txt", "r")
total = 0
for line in input_file:
    number = int(line)
    total += number
print(total)
input_file.close()
