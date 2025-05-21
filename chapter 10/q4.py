print("Enter 'quit' at any time to stop.\n")
while True:
    name = input("What is your name? ")
    if name.lower() == 'quit':
        break
    reason = input("Why do you like programming? ")
    if reason.lower() == 'quit':
        break
    print(f"Thanks, {name}, for your response!")
    with open("guest_book.txt", "a") as file:
        file.write(f"{name}: {reason}\n")

print("All responses have been saved to guest_book.txt.")