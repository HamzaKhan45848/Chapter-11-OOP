print("Enter 'quit' at any time to exit.\n")
while True:
    name = input("What is your name? ")
    if name.lower() == 'quit':
        break
    print(f"Hello, {name}! Welcome.")
    with open("guest_book.txt", "a") as file:
        file.write(f"{name}\n")

print("Thanks for visiting!")