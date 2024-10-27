import sys
from user_interface.main_menu_ui import MainMenuUI
from user_interface.create_teams_ui import CreateTeamsUI
from user_interface.update_teams_ui import UpdateTeamsUI
from user_interface.get_teams_data_ui import GetTeamsDataUI
from  user_interface.delete_teams_ui import DeleteTeamsUI

# Define the MenuSystem class
class MenuSystem:
    """Menu based system for manage hockey team data"""
    # Define __init__ method, class constructor
    def __init__(self):
        # Define a python list to save team data object temporary
        self.team_object_list = []

    # Define the main function
    def main(self):
        # Display the main menu
        self.main_menu = MainMenuUI(self.team_object_list)
        # Call the handle_options() function
        self.menu_choice = self.main_menu.handle_options()

        # If user select the create team option
        if int(self.menu_choice) == 1:
            # Clear the current terminal screen
            self.main_menu.clear_terminal()
            # Create create_team_ui object using CreateTeamsUI class
            self.create_team_ui = CreateTeamsUI(self.team_object_list)
            # Call the handle_options() function
            team_object = self.create_team_ui.handle_options()
            # Append the team object to the team_object_list
            self.team_object_list.append(team_object)
            # Return back to main menu
            self.main_menu.back_to_main_menu()

        # If user select the option for search get team data by ID, All Data, Gender, cancelled participation teams
        if int(self.menu_choice) in [2, 3, 4, 7]:
            # Define the query dict
            query_dict = {2 : "ID", 3 : "All", 4 : "Gender", 7 : "Cancellation"}
            # Get the relevant query
            query = next(val for key, val in query_dict.items() if int(self.menu_choice) == key)
            # Clear the current terminal screen
            self.main_menu.clear_terminal()
            # Create get_team_data_ui object using GetTeamsDataUI class
            self.get_team_data_ui = GetTeamsDataUI(query = query, team_objects = self.team_object_list)
            # Call the handle_options() function
            self.get_team_data_ui.handle_options()
            # Return back to main menu
            self.main_menu.back_to_main_menu()

        # # If user select the update team option
        # if int(menu_choice) == 5:
        #     # Clear the current terminal screen
        #     main_menu.clear_terminal()
        #     update_team_ui = UpdateTeamsUI()
        #     update_team_ui.handle_options()
        #     # Return back to main menu
        #     main_menu.back_to_main_menu()
        #
        # # If user select the delete team option
        # if int(menu_choice) == 6:
        #     # Clear the current terminal screen
        #     main_menu.clear_terminal()
        #     delete_team_ui = DeleteTeamsUI()
        #     delete_team_ui.handle_options()
        #     # Return back to main menu
        #     main_menu.back_to_main_menu()
        #
        # # If user select the option for check cancelled participation teams
        # if int(menu_choice) == 7:
        #     # Clear the current terminal screen
        #     main_menu.clear_terminal()
        #     get_team_data_ui = GetTeamsDataUI(query="Cancellation")
        #     get_team_data_ui.handle_options()
        #     # Return back to main menu
        #     main_menu.back_to_main_menu()
        #
        # # If user select the option for exit the programme
        # if int(menu_choice) == 10:
        #     main_menu.clear_terminal()
        #     # Exit the running programme
        #     sys.exit(0)




if __name__ == "__main__":
    # Create a menu_system object using MenuSystem class
    menu_system = MenuSystem()
    # Infinite while loop to run the main program until user need to exit the program
    while True:
        # Call the main function
        menu_system.main()