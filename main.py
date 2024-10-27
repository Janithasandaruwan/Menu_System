import sys
from user_interface.main_menu_ui import MainMenuUI
from user_interface.create_teams_ui import CreateTeamsUI
from user_interface.update_teams_ui import UpdateTeamsUI
from user_interface.get_teams_data_ui import GetTeamsDataUI
from  user_interface.delete_teams_ui import DeleteTeamsUI

# Define the main function
def main():
    # Display the main menu
    main_menu = MainMenuUI()
    menu_choice = main_menu.handle_options()

    # If user select the create team option
    if int(menu_choice) == 1:
        # Clear the current terminal screen
        main_menu.clear_terminal()
        create_team_ui = CreateTeamsUI()
        create_team_ui.handle_options()
        # Return back to main menu
        main_menu.back_to_main_menu()

    # If user select the option for search a team by ID
    if int(menu_choice) == 2:
        # Clear the current terminal screen
        main_menu.clear_terminal()
        get_team_data_ui = GetTeamsDataUI(query = "ID")
        get_team_data_ui.handle_options()
        # Return back to main menu
        main_menu.back_to_main_menu()

    # If user select the option for search all teams
    if int(menu_choice) == 3:
        # Clear the current terminal screen
        main_menu.clear_terminal()
        get_team_data_ui = GetTeamsDataUI(query="All")
        get_team_data_ui.handle_options()
        # Return back to main menu
        main_menu.back_to_main_menu()

    # If user select the option for search a team by Gender
    if int(menu_choice) == 4:
        # Clear the current terminal screen
        main_menu.clear_terminal()
        get_team_data_ui = GetTeamsDataUI(query="Gender")
        get_team_data_ui.handle_options()
        # Return back to main menu
        main_menu.back_to_main_menu()

    # If user select the update team option
    if int(menu_choice) == 5:
        # Clear the current terminal screen
        main_menu.clear_terminal()
        update_team_ui = UpdateTeamsUI()
        update_team_ui.handle_options()
        # Return back to main menu
        main_menu.back_to_main_menu()

    # If user select the delete team option
    if int(menu_choice) == 6:
        # Clear the current terminal screen
        main_menu.clear_terminal()
        delete_team_ui = DeleteTeamsUI()
        delete_team_ui.handle_options()
        # Return back to main menu
        main_menu.back_to_main_menu()

    # If user select the option for check cancelled participation teams
    if int(menu_choice) == 7:
        # Clear the current terminal screen
        main_menu.clear_terminal()
        get_team_data_ui = GetTeamsDataUI(query="Cancellation")
        get_team_data_ui.handle_options()
        # Return back to main menu
        main_menu.back_to_main_menu()

    # If user select the option for exit the programme
    if int(menu_choice) == 8:
        main_menu.clear_terminal()
        # Exit the running programme
        sys.exit(0)

if __name__ == "__main__":
    # Infinite while loop to run the program until user need to exit the program
    while True:
        # Call the main function
        main()