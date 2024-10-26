from datetime import datetime
from team_manage.hockey_team_manage import TeamOperations
from user_interface.user_interface import UserInterface


class UpdateTeamsUI(UserInterface):
    """Concrete implementation of the update teams UI using User_Interface abstract class"""

    # Define the __init__ method
    def __init__(self):
        # Define update teams steps as a python list
        self.update_team_steps = [
            "a) Enter the New Team Name: \n",
            "b) Change Team Type: \n Enter 1: Boys, 2: Girls, 3: Mix\n",
            "c) Enter New Total Number Of Players: \n",
            "d) Total Fee: ",
            "e) Update Fee Paid Status: \n Enter 1: True, 2: False\n",
            "f) Cancellation Date: YYYY-MM-DD Format\n",
        ]

        # Get the current data of the existing team
        self.team_opeartion = TeamOperations()

    def get_user_input(self):
        """Get the user's data for update a new team"""
        # Infinite while loop to update the correct team ID
        while True:
            # Get the team ID from the user
            team_id = input("Enter the team ID that you need to update : ")

            # Check whether team ID is a numeric value
            if not team_id.isnumeric():
                print("Please Enter the Valid Team ID!!!!!")
            else:
                # Check whether team ID existing in the current data
                # Current all team IDs
                current_team_IDs = self.team_opeartion.get_all_teams()[3]
                if int(team_id) not in current_team_IDs:
                    print("Team ID Not Found!!!!!")
                    print(f"***Current Team ID List : {current_team_IDs}")
                else:
                    # Get the current team data
                    current_team_data = self.team_opeartion.get_a_team_by_id(int(team_id))
                    break

        # Infinite while loop to update the correct team name
        while True:
            # Display the current team name
            print("\n")
            print(self.update_team_steps[0])
            print(f"***Current Team Name : {current_team_data["Team Name"]}")
            print("If You Dont Need To Change, Please Press Enter.......")
            team_name = input("Enter Your Data Here: ")

            # Check whether user press enter
            if team_name != "":
                # Team name should be not a number
                try:
                    # Attempt to convert the team name to a float
                    team_name_numeric = float(team_name)
                    print("Team Name Cannot be a Number!!!!!")
                except:
                    break
            else:
                # If user not update the filed, keep the previous values
                team_name = current_team_data["Team Name"]
                break

        # Infinite while loop to update the correct team type
        while True:
            # Display the current team type
            print("\n")
            print(self.update_team_steps[1])
            print(f"***Current Team Type : {current_team_data["Team Type"]}")
            print("If You Dont Need To Change, Please Press Enter.......")
            team_type = input("Enter Your Choice Here: ")

            # Check whether user press enter
            if team_type != "":
                # Team type should be int and it should be 1, 2, 3
                if not team_type.isdigit() or team_type not in ["1", "2", "3"]:
                    print("Please Select A Valid Choice!!!!!")
                else:
                    # Get the correct team type according to the user input choice
                    team_type = next(types for idx, types in enumerate(["Boys", "Girls", "Mix"]) if idx + 1 == int(team_type))
                    break
            else:
                # If user not update the filed, keep the previous values
                team_type = current_team_data["Team Type"]
                break

        # Infinite while loop to update the correct total number of players
        while True:
            # Display the current number of players
            print("\n")
            print(self.update_team_steps[2])
            print(f"***Current Total Players : {current_team_data["Total Players"]}")
            print("If You Dont Need To Change, Please Press Enter.......")
            total_players = input("Enter Your Data Here: ")

            # Check whether user press enter
            if total_players != "":
                # Total number of players should be int and greater than zero
                if not total_players.isdigit():
                    print("Player Count Should be Positive Number!!!!!")
                elif int(total_players) <= 0:
                    print("Player Count Should be Positive Number!!!!!")
                else:
                    # Convert number of players in to integer value
                    total_players = int(total_players)
                    break
            else:
                # If user not update the filed, keep the previous values
                total_players = current_team_data["Total Players"]
                break

        # Display the total fee based on the team count
        print("\n")
        total_fee = 100 * total_players
        print(f"{self.update_team_steps[3]}{total_fee} SEK")

        # Infinite while loop to update the correct fee paid status
        while True:
            # Display the current paid status
            print("\n")
            print(self.update_team_steps[4])
            print(f"***Current Fee Paid Status : {current_team_data["Fee Status"]}")
            print("If You Dont Need To Change, Please Press Enter.......")
            fee_status = input("Enter Your Choice Here: ")

            # Check whether user press enter
            if fee_status != "":
                # Fee status should be a number and it should be 1, 2
                if not fee_status.isdigit() or fee_status not in ["1", "2"]:
                    print("Please Select A Valid Choice!!!!!")
                else:
                    # Get the correct fee status according to the user input choice
                    fee_status = "Paid" if int(fee_status) == 1 else "Not-Paid"
                    break
            else:
                # If user not update the filed, keep the previous values
                fee_status = current_team_data["Fee Status"]
                break

        # Infinite while loop to update the Cancellation date
        while True:
            # Display the current cancellation date
            print("\n")
            print(self.update_team_steps[5])
            # Current cancellation date
            current_date = current_team_data["Cancellation Date"]
            print(f"***Current Cancellation Date : {"No" if current_date == None else current_date}")
            print("If You Dont Need To Change, Please Press Enter.......")

            cancellation_date = input("Enter Your Choice Here: ")

            # Check whether user press enter
            if cancellation_date != "":
                # Check whether user enter the date as expected format
                try:
                    datetime.strptime(cancellation_date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Enter the Date In Expected Format!!!!!")

            else:
                # If user not update the filed, keep the previous values
                cancellation_date = current_date
                break

        # Return all the user input data
        return [int(team_id), team_name, team_type, total_players, total_fee, fee_status, cancellation_date]

    def display_UI(self):
        """Display the update teams UI with borders and vertical lines."""
        print("\n" + "=" + "=" * 40 + "=")
        print("|" + " " * 10 + "Update Team Data" + " " * 14 + "|")
        print("=" + "=" * 40 + "=")


    def handle_options(self):
        # Display the update team UI
        self.display_UI()
        user_input = self.get_user_input()
        # Print New Line
        print("\n")
        # Call the update_team() method to update data
        self.team_opeartion.update_team(team_id = user_input[0],
                                        team_name = user_input[1],
                                        team_type = user_input[2],
                                        total_players = user_input[3],
                                        total_fee = user_input[4],
                                        fee_status = user_input[5],
                                        cancellation_date = user_input[6])

    def __str__(self):
        """string representation of the UpdateTeamsUI class"""
        return f"Update A Team Steps: {self.update_team_steps}"


if __name__ == "__main__":
    main_menu = UpdateTeamsUI()
    main_menu.handle_options()
    #main_menu.get_user_input()
    #print(main_menu)