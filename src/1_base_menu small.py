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
