from menu import display_menu, get_input

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
   # print(__name__)
    main()