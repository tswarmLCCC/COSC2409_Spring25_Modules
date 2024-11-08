# Example 1: Display menu with default options
print("Example 1: Using display_menu with default options")
options = ["Option 1", "Option 2", "Option 3"]

print("Menu:")
for i, option in enumerate(options, start=1):
    print(f"{i}. {option}")

while True:
    try:
        choice = int(input("Enter your choice: ")) - 1
        if 0 <= choice < len(options):
            print(f"You chose: {choice + 1}\n")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Example 2: Display menu with custom options
print("Example 2: Using display_menu with custom options")
options = ["Start Game", "Load Game", "Settings", "Exit"]

print("Menu:")
for i, option in enumerate(options, start=1):
    print(f"{i}. {option}")

while True:
    try:
        choice = int(input("Enter your choice: ")) - 1
        if 0 <= choice < len(options):
            print(f"You chose: {options[choice]}\n")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Example 3: Get input with default prompt and type
print("Example 3: Using get_input with default prompt and type")
while True:
    try:
        user_input = input("Enter something: ")
        print(f"You entered: {user_input}\n")
        break
    except ValueError:
        print("Invalid input. Please enter a string.")

# Example 4: Get input with custom prompt and type int
print("Example 4: Using get_input with custom prompt and type int")
while True:
    try:
        age = int(input("Enter your age: "))
        print(f"Your age is: {age}\n")
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Example 5: Get input with custom prompt and type float
print("Example 5: Using get_input with custom prompt and type float")
while True:
    try:
        height = float(input("Enter your height in meters: "))
        print(f"Your height is: {height} meters\n")
        break
    except ValueError:
        print("Invalid input. Please enter a float.")