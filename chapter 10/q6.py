print("Give me two numbers, and I'll add them together.")
print("Enter 'quit' at any time to exit.\n")

while True:
    first_number = input("Enter the first number: ")
    if first_number.lower() == 'quit':
        break

    second_number = input("Enter the second number: ")
    if second_number.lower() == 'quit':
        break

    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print("Oops! Please enter valid numbers.\n")
        continue  # Loop again for new input
    else:
        print(f"The sum is {result}\n")