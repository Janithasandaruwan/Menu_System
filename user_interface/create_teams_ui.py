from team_manage.hockey_team_manage import TeamOperations
from user_interface.user_interface import UserInterface

class CreateTeamsUI(UserInterface):
    """Concrete implementation of the creation teams UI using User_Interface abstract class"""

    # Define the __init__ method
    def __init__(self, team_objects):
        # Define create teams steps as a python list
        self.create_team_steps = [
            "a) Enter Your Team Name: \n",
            "b) Select Team Type: \n Enter 1: Boys, 2: Girls, 3: Mix\n",
            "c) Enter Total Number Of Players: \n",
            "d) Total Fee: ",
            "e) Fee Paid: \n Enter 1: True, 2: False\n"
        ]
        # Create a team_operation object using TeamOperations class
        self.team_operation = TeamOperations(team_objects)

    def get_user_input(self):
        """Get the user's data for create a new team"""
        # Infinite while loop to get the correct team name
        while True:
            # Get the team name
            print(self.create_team_steps[0])
            team_name = input("Enter Your Data Here: ")
            # Team name should be not empty
            if team_name == "":
                 print("Team Name Cannot be Empty!!!!!\n")
            # Team name should be not a number
            elif team_name.isdigit():
                print("Team Name Cannot be a Number!!!!!\n")
            else:
                break

        # Infinite while loop to get the correct team type
        while True:
            # Get the team type
            print("\n")
            print(self.create_team_steps[1])
            team_type = input("Enter Your Choice Here: ")
            # Team type should be int and it should be 1, 2, 3
            if not team_type.isdigit() or team_type not in ["1", "2", "3"]:
                print("Please Select A Valid Choice!!!!!\n")
            else:
                # Get the correct team type according to the user input choice
                team_type = next(types for idx, types in enumerate(["Boys", "Girls", "Mix"]) if idx + 1 == int(team_type))
                break

        # Infinite while loop to get the correct total number of players
        while True:
            # Get the total number of players
            print("\n")
            print(self.create_team_steps[2])
            number_of_players = input("Enter Your Data Here: ")
            # Total number of players should be int and greater than zero
            if not number_of_players.isdigit():
                print("Player Count Should be Positive Number!!!!!\n")
            elif int(number_of_players) <= 0:
                print("Player Count Should be Positive Number!!!!!\n")
            else:
                # Convert number of players in to integer value
                number_of_players = int(number_of_players)
                break

        # Display the total fee based on the team count
        print("\n")
        print(f"{self.create_team_steps[3]}{100 * number_of_players} SEK")

        # Infinite while loop to get the correct fee paid status
        while True:
            # Get the fee paid status
            print("\n")
            print(self.create_team_steps[4])
            fee_status = input("Enter Your Choice Here: ")
            # Fee status should be a number and it should be 1, 2
            if not fee_status.isdigit() or fee_status not in ["1", "2"]:
                print("Please Select A Valid Choice!!!!!\n")
            else:
                # Get the correct fee status according to the user input choice
                fee_status = "Paid" if int(fee_status) == 1 else "Not-Paid"
                break

        # Return all the user input data
        return [team_name, team_type, number_of_players, fee_status]

    def display_UI(self):
        """Display the create teams UI with borders and vertical lines."""
        print("\n" + "=" + "=" * 40 + "=")
        print("|" + " " * 10 + "Create a New Team" + " " * 13 + "|")
        print("=" + "=" * 40 + "=")


    def handle_options(self):
        """Handle the option selected by the user"""
        # Display the creation team UI
        self.display_UI()
        user_input = self.get_user_input()
        # Call the create_team() method to save the data
        team_object = self.team_operation.create_team(team_name = user_input[0],
                                   team_type = user_input[1],
                                   total_players = user_input[2],
                                   fee_paid = user_input[3])
        print("\n")
        print("Data Successfully Saved!!!!!")
        return team_object


    def __str__(self):
        """string representation of the CreateTeamsUI class"""
        return f"Create New Team Steps: {self.create_team_steps}"


if __name__ == "__main__":
    main_menu = CreateTeamsUI()
    main_menu.display_UI()
    #main_menu.get_user_input()
    #print(main_menu)