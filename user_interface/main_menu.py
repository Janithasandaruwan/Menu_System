from user_interface import UserInterface

class MainMenu(UserInterface):
    """Concrete implementation of the main menu using User_Interface abstract class"""

    # Define the __init__ method
    def __init__(self):
        # Define main menu options in a python dictionary
        self.main_menu_options = {
            "01" : "Create A New Team",
            "02" : "Search A Team By ID",
            "03" : "Search All Teams",
            "04" : "Search Teams By Gender",
            "05" : "Update A Team",
            "06" : "Delete A Team",
            "O7" : "Exit"
        }

    def get_user_input(self):
        """Get the user's main menu choice"""
        # Check whether user enter a valid option
        try:
            # Get the user input for main menu option
            choice = int(input("\nSelect Your Option: "))
            # Convert user selected option same way as main_menu_options dict keys
            option = "0" + str(choice)
            # Check whether user enter option is include in main menu options
            if option in self.main_menu_options.keys():
                return option
            else:
                print("Invalid option entered! Please Try Again")
                return None
        # If user entered invalid option, display a warning message
        except ValueError:
            print("Please Enter Valid Option!")
            return None

    def display_UI(self):
        """Displays the main menu with borders and vertical lines."""
        print("\n" + "=" + "=" * 40 + "=")
        print("|" + " " * 15 + "Main Menu" + " " * 16 + "|")
        print("=" + "=" * 40 + "=")
        # Display the menu options in the UI
        for key, value in self.main_menu_options.items():
            print(f"|  {key}  | {value.ljust(32)}|")
        print("=" + "=" * 40 + "=")
        print(f"    Total Teams Registered : {1026}")
        print("=" + "=" * 40 + "=")
        print(f"    Percentage of Paid Teams: {10}%")
        print("=" + "=" * 40 + "=")

    def handle_options(self):
        pass

    def __str__(self):
        """string representation of the Maine_Menu class"""
        return f"Main Menu Options: {self.main_menu_options}"



if __name__ == "__main__":
    main_menu = MainMenu()
    #main_menu.display_UI()
    #main_menu.get_user_input()
    print(main_menu)