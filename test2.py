import os

class MenuSystem:
    def __init__(self):
        self.menu_options = {
            1: 'Do something',
            2: 'Do something else',
            3: 'Another option',
            4: 'Quit'
        }

    def clear_console(self):
        """Clears the terminal screen if the environment supports it."""
        if 'TERM' in os.environ:
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("\n" * 100)  # Print multiple newlines as an alternative to clear the screen

    def display_menu(self):
        """Displays the menu with borders and vertical lines."""
        print("\n" + "+" + "-" * 38 + "+")
        print("|" + " " * 13 + "Main Menu" + " " * 13 + "|")
        print("+" + "-" * 38 + "+")
        for key, value in self.menu_options.items():
            print(f"|  {key}  | {value.ljust(30)}|")
        print("+" + "-" * 38 + "+")

    def get_user_input(self):
        try:
            choice = int(input("\nSelect an option (1-4): "))
            if choice in self.menu_options:
                return choice
            else:
                print("Invalid option. Please try again.")
                return None
        except ValueError:
            print("Please enter a valid number.")
            return None

    def handle_option(self, choice):
        if choice == 4:
            print("\nThank you for using the program. Goodbye!")
            return False
        else:
            print(f"\nYou selected: {self.menu_options[choice]}")
            input("\nPress Enter to return to the menu...")
            return True

    def run(self):
        running = True
        while running:
            self.clear_console()
            self.display_menu()
            choice = self.get_user_input()
            if choice:
                running = self.handle_option(choice)

if __name__ == "__main__":
    menu = MenuSystem()
    menu.run()
