from user_interface.user_interface import UserInterface
from team_manage.hockey_team_manage import TeamOperations

class MainMenuUI(UserInterface):
    """Concrete implementation of the main menu using User_Interface abstract class"""

    # Define the __init__ method
    def __init__(self):
        # Define main menu options in a python dictionary
        self.main_menu_options = {
            "01" : "Create a New Team",
            "02" : "Search a Team By ID",
            "03" : "Search All Teams",
            "04" : "Search Teams By Gender",
            "05" : "Update a Team",
            "06" : "Delete a Team",
            "07": "Teams Cancellation Details",
            "O8" : "Exit"
        }

        # Get all current team data using TeamOperations class
        all_team_data = TeamOperations()
        data_tuple = all_team_data.get_all_teams()
        # Get total number of teams registered
        self.total_teams = data_tuple[1]
        # Get the percentage of paid teams
        self.paid_percentage = data_tuple[2]

    def get_user_input(self):
        """Get the user's main menu choice"""
        # Infinite while loop to get the correct user input
        while True:
            # Check whether user enter a valid option
            try:
                # Get the user input for main menu option
                choice = int(input("\nSelect Your Option From Above Menu: "))
                # Convert user selected option same way as main_menu_options dict keys
                option = "0" + str(choice)
                # Check whether user enter option is include in main menu options
                if option in self.main_menu_options.keys():
                    return choice
                else:
                    print("Invalid option entered! Please Try Again")

            # If user entered invalid option, display a warning message
            except ValueError:
                print("Please Enter Valid Option!")

    def display_UI(self):
        """Display the main menu with borders and vertical lines."""
        print("\n" + "=" + "=" * 40 + "=")
        print("|" + " " * 15 + "Main Menu" + " " * 16 + "|")
        print("=" + "=" * 40 + "=")
        # Display the menu options in the UI
        for key, value in self.main_menu_options.items():
            print(f"|  {key}  | {value.ljust(32)}|")
        print("=" + "=" * 40 + "=")
        print(f"    Total Teams Registered : {self.total_teams}")
        print("=" + "=" * 40 + "=")
        print(f"    Percentage of Paid Teams: {self.paid_percentage}")
        print("=" + "=" * 40 + "=")

    def handle_options(self):
        # Display the main menu options
        self.display_UI()
        user_input = self.get_user_input()
        return user_input

    def __str__(self):
        """string representation of the MainMenuUI class"""
        return f"Main Menu Options: {self.main_menu_options}"


if __name__ == "__main__":
    main_menu = MainMenuUI()
    main_menu.display_UI()
    main_menu.get_user_input()
    #print(main_menu)