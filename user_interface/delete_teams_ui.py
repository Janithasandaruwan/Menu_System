from datetime import datetime
from team_manage.hockey_team_manage import TeamOperations
from user_interface.user_interface import UserInterface

class DeleteTeamsUI(UserInterface):
    """Concrete implementation of the delete teams UI using User_Interface abstract class"""

    # Define the __init__ method
    def __init__(self, team_objects):
        # Create a team_operation object using TeamOperations class
        self.team_operation = TeamOperations(team_objects)

    def get_user_input(self):
        """Get the team ID from the user for delete a team"""
        # Infinite while loop to get the correct team ID for delete
        while True:
            # Check whether team ID existing in the current data
            # Current all team IDs
            current_team_IDs = self.team_operation.get_all_teams()[3]
            print(f"***Current Team ID List : {current_team_IDs}")
            # Get the team ID from the user
            team_id = input("Enter the team ID that you need to Delete : ")

            # Check whether team ID is a numeric value
            if not team_id.isnumeric():
                print("Please Enter the Valid Team ID!!!!!")
            else:
                if int(team_id) not in current_team_IDs:
                    print("Team ID Not Found!!!!!")
                else:
                    # Delete the team from the data
                    # Ask the confirmation
                    print("\n")
                    print(f"Confirm The Delete Team ID : {team_id}\n")
                    print("Press 1 : Yes, 2 : No")
                    confirm_input = input()
                    # Check whether user select correct option
                    try:
                        confirm_input = int(confirm_input)
                        if confirm_input not in [1, 2] :
                            print("Please Select A Valid Option!!!!!")
                        else:
                            if confirm_input == 1:
                                team_index = self.team_operation.delete_team(int(team_id))
                                return team_index
                            else:
                                print(f"Team ID : {team_id} Deletion Discard!!!!!")
                                return None
                    except ValueError:
                        print("Please Select A Valid Option!!!!!")

    def display_UI(self):
        """Display the delete teams UI with borders and vertical lines."""
        print("\n" + "=" + "=" * 40 + "=")
        print("|" + " " * 10 + "Delete Team Data" + " " * 14 + "|")
        print("=" + "=" * 40 + "=")


    def handle_options(self):
        # Display the update team UI
        self.display_UI()
        team_index = self.get_user_input()
        return team_index

    def __str__(self):
        """string representation of the DeleteTeamsUI class"""
        return f"Delete A Team Data"


if __name__ == "__main__":
    main_menu = DeleteTeamsUI()
    main_menu.handle_options()
    #main_menu.get_user_input()
    #print(main_menu)