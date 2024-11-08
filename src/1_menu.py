# /d:/LCCC_Curriclulum/Homework/COSC2409_Spring25_Modules/src/menu.py

def display_menu(options=None):
    """
    Display a menu of options and return the user's choice.
    
    :param options: A list of strings representing the menu options (default is a sample menu).
    :return: The index of the chosen option.
    
    Example usage:
    >>> options = ["Option 1", "Option 2", "Option 3", "Exit"]
    >>> choice = display_menu(options)
    >>> print(f"You chose: {options[choice]}")
    """
    if options is None:
        options = ["Option 1", "Option 2", "Option 3", "Exit"]
    
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = input("Please choose an option: ")
    return int(choice) - 1

def get_input(prompt="Enter a value: ", input_type=str):
    """
    Get user input and convert it to the specified type.
    
    :param prompt: The prompt to display to the user (default is "Enter a value: ").
    :param input_type: The type to convert the input to (default is str).
    :return: The user input converted to the specified type.
    
    Example usage:
    >>> age = get_input("Enter your age: ", int)
    >>> print(f"Your age is: {age}")
    """
    return input_type(input(prompt))

def confirm(prompt="Are you sure? (y/n): "):
    """
    Ask the user for a yes/no confirmation.
    
    :param prompt: The prompt to display to the user (default is "Are you sure? (y/n): ").
    :return: True if the user confirms, False otherwise.
    
    Example usage:
    >>> if confirm():
    >>>     print("Confirmed!")
    >>> else:
    >>>     print("Not confirmed.")
    """
    while True:
        choice = input(prompt).lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please respond with 'y' or 'n'.")

def print_header(header="Header"):
    """
    Print a header surrounded by dashes.
    
    :param header: The header text to display (default is "Header").
    
    Example usage:
    >>> print_header("Welcome to the Program")
    """
    print(f"\n{'-' * len(header)}\n{header}\n{'-' * len(header)}\n")

def main():
    options = ["Option 1", "Option 2", "Option 3", "Exit"]
    while True:
        choice = display_menu(options)
        if choice == 3:  # Exit
            break
        print(f"You chose: {options[choice]}")

if __name__ == "__main__":
    main()
    default_options = ["Option 1", "Option 2", "Option 3", "Exit"]