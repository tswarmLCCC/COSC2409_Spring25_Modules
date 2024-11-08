def display_menu(options=None):
    if options is None:
        options = ["Option 1", "Option 2", "Option 3"]
    
    print("Menu:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    while True:
        try:
            choice = int(input("Enter your choice: ")) - 1
            if 0 <= choice < len(options):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_input(prompt="Enter something: ", input_type=str):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a {input_type.__name__}.")

def main():
    # Example 1: Using display_menu with default options
    print("Example 1: Using display_menu with default options")
    choice = display_menu()
    print(f"You chose: {choice + 1}\n")

    # Example 2: Using display_menu with custom options
    print("Example 2: Using display_menu with custom options")
    options = ["Start Game", "Load Game", "Settings", "Exit"]
    choice = display_menu(options)
    print(f"You chose: {options[choice]}\n")

    # Example 3: Using get_input with default prompt and type
    print("Example 3: Using get_input with default prompt and type")
    user_input = get_input()
    print(f"You entered: {user_input}\n")

    # Example 4: Using get_input with custom prompt and type int
    print("Example 4: Using get_input with custom prompt and type int")
    age = get_input("Enter your age: ", int)
    print(f"Your age is: {age}\n")

    # Example 5: Using get_input with custom prompt and type float
    print("Example 5: Using get_input with custom prompt and type float")
    height = get_input("Enter your height in meters: ", float)
    print(f"Your height is: {height} meters\n")

if __name__ == "__main__":
    main()