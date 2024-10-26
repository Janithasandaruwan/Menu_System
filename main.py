import os
from user_interface.main_menu_ui import MainMenuUI
from user_interface.create_teams_ui import CreateTeamsUI
from user_interface.update_teams_ui import UpdateTeamsUI
from user_interface.get_teams_data_ui import GetTeamsDataUI
from  user_interface.delete_teams_ui import DeleteTeamsUI

# Function for clear the screen based on the operating system
def clear_terminal():
    # Check the operating system and clear the screen accordingly
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

def main():
    # Display the main menu
    main_menu = MainMenuUI()
    menu_choice = main_menu.handle_options()

    # If user select the create team option
    if int(menu_choice) == 1:
        clear_terminal()
        create_team_ui = CreateTeamsUI()
        create_team_ui.handle_options()

    # If user select the option for search a team by ID
    if int(menu_choice) == 2:
        clear_terminal()
        get_team_data_ui = GetTeamsDataUI(query = "ID")
        get_team_data_ui.handle_options()

    # If user select the option for search all teams
    if int(menu_choice) == 3:
        clear_terminal()
        get_team_data_ui = GetTeamsDataUI(query="All")
        get_team_data_ui.handle_options()

    # If user select the option for search a team by Gender
    if int(menu_choice) == 4:
        clear_terminal()
        get_team_data_ui = GetTeamsDataUI(query="Gender")
        get_team_data_ui.handle_options()

    # If user select the update team option
    if int(menu_choice) == 5:
        clear_terminal()
        update_team_ui = UpdateTeamsUI()
        update_team_ui.handle_options()

    # If user select the delete team option
    if int(menu_choice) == 6:
        clear_terminal()
        delete_team_ui = DeleteTeamsUI()
        delete_team_ui.handle_options()

    # If user select the option for check cancelled participation teams
    if int(menu_choice) == 7:
        clear_terminal()
        get_team_data_ui = GetTeamsDataUI(query="Cancellation")
        get_team_data_ui.handle_options()


if __name__ == "__main__":
    #team_opeartion = TeamOperations()
    #team_opeartion.create_team("Test_name4", "Mix", 13, True)
    #print(team_opeartion.get_a_team_by_id(1))
    #team_opeartion.delete_team(3)
    #team_opeartion.update_team(1, "Sandaruwan", "Girl", 40, True)
    #print(team_opeartion.get_all_teams())
    #print(team_opeartion.get_a_team_by_gender("boys"))
    # main_menu = MainMenuUI()
    # main_menu.handle_options()
    main()