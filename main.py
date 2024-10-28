import sys
from user_interface.main_menu_ui import MainMenuUI
from user_interface.create_teams_ui import CreateTeamsUI
from user_interface.update_teams_ui import UpdateTeamsUI
from user_interface.get_teams_data_ui import GetTeamsDataUI
from  user_interface.delete_teams_ui import DeleteTeamsUI
from team_data.file_data_manage import TxtFileDataManage

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

        # If user select the update team option
        if int(self.menu_choice) == 5:
            # Clear the current terminal screen
            self.main_menu.clear_terminal()
            # Create update_team_ui object using UpdateTeamsUI class
            self.update_team_ui = UpdateTeamsUI(self.team_object_list)
            # Call the handle_options() function
            self.update_team_ui.handle_options()
            # Return back to main menu
            self.main_menu.back_to_main_menu()

        # If user select the delete team option
        if int(self.menu_choice) == 6:
            # Clear the current terminal screen
            self.main_menu.clear_terminal()
            # Create delete_team_ui object using DeleteTeamsUI class
            self.delete_team_ui = DeleteTeamsUI(self.team_object_list)
            # Call the handle_options() function
            team_index = self.delete_team_ui.handle_options()
            # Delete team object from the team_object_list list
            if team_index is not None:
                self.team_object_list.pop(team_index)
            # Return back to main menu
            self.main_menu.back_to_main_menu()

        # If user select the option to upload the current data in to a text file
        if int(self.menu_choice) == 8:
            # Clear the current terminal screen
            self.main_menu.clear_terminal()
            # Create upload_data object using TxtFileDataManage class
            self.upload_data = TxtFileDataManage(self.team_object_list)
            # Call the save_data() function
            self.upload_data.save_data([])
            # Return back to main menu
            self.main_menu.back_to_main_menu()

        # If user select the option to download the data from text file to current object list
        if int(self.menu_choice) == 9:
            # Clear the current terminal screen
            self.main_menu.clear_terminal()
            # Create download_data object using TxtFileDataManage class
            self.download_data = TxtFileDataManage(self.team_object_list)
            # Call the create_team_obj_list() function
            team_obj_data = self.download_data.create_team_obj_list()
            # Combine team_object_list and team data list in text file
            self.team_object_list = self.team_object_list + team_obj_data
            print(self.team_object_list)
            # Return back to main menu
            self.main_menu.back_to_main_menu()

         # If user select the option for exit the programme
        if int(self.menu_choice) == 10:
            self.main_menu.clear_terminal()
            # Exit the running programme
            sys.exit(0)

if __name__ == "__main__":
    # Create a menu_system object using MenuSystem class
    menu_system = MenuSystem()
    # Infinite while loop to run the main program until user need to exit the program
    while True:
        # Call the main function
        menu_system.main()