from team_manage.hockey_team_manage import TeamOperations
from user_interface.user_interface import UserInterface

class GetTeamsDataUI(UserInterface):
    """Concrete implementation of the get teams data UI using User_Interface abstract class"""

    # Define the __init__ method
    def __init__(self, query, team_objects):
        # Create a team_operation object using TeamOperations class
        self.team_operation = TeamOperations(team_objects)
        # Get the user query for get teams data for different options
        self.query  = query

    # Function for display one team data
    def display_one_team_data(self, all_team_data):
        # Loop through the data and display the data
        for data in all_team_data:
            print("\n")
            print(f"** Team ID : {data["Team ID"]}")
            print(f"** Registered Date : {data["Registered Date"]}")
            print(f"** Team Name : {data["Team Name"]}")
            print(f"** Team Type (Girls/ Boys/ Mix) : {data["Team Type"]}")
            print(f"** Total Players : {data["Total Players"]}")
            print(f"** Total Fee : {data["Total Fee"]} SEK")
            print(f"** Fee Paid Status : {data["Fee Paid Status"]}")
            print(f"** Cancellation Date : {data["Cancellation Date"]}")
            print("=" + "=" * 40 + "=")


    def get_user_input(self):
        """Get the user's input for get team data"""

        # If user need to get all the team data
        if self.query == "All":
            # Call the get_all_teams() method to read all team data
            all_team_data = self.team_operation.get_all_teams()[0]
            # Display all team information
            self.display_UI()
            # Check whether data is not empty
            if len(all_team_data) > 0:
                self.display_one_team_data(all_team_data)
            else:
                print("No Data Records!!!!!")

        # If user need to get team data by ID
        if self.query == "ID":
            # Infinite while loop to get the correct team ID
            while True:
                # Current all team IDs
                current_team_IDs = self.team_operation.get_all_teams()[3]
                print(f"***Current Team ID List : {current_team_IDs}")
                # Get the team ID from the user
                team_id = input("Enter the team ID that you need to view : ")

                # Check whether team ID is a numeric value
                if not team_id.isnumeric():
                    print("Please Enter the Valid Team ID!!!!!")
                else:
                    # Check whether team ID existing in the current data
                    if int(team_id) not in current_team_IDs:
                        print("Team ID Not Found!!!!!")
                    else:
                        # Call the get_a_team_by_id() method to read team data by ID
                        team_data = self.team_operation.get_a_team_by_id(int(team_id))

                        """Display the one team data UI with borders and vertical lines."""
                        print("\n" + "=" + "=" * 40 + "=")
                        print("|" + " " * 5 + f"Information Of The Team ID : {int(team_id)}" + " " * 5 + "|")
                        print("=" + "=" * 40 + "=")
                        self.display_one_team_data([team_data])
                        break

        # If user need to get team data by Team Type
        if self.query == "Gender":
            # Infinite while loop to get the correct team type
            while True:
                # Display the current team type
                print("Select Team Type To Filter Data: \n Enter 1: Boys, 2: Girls, 3: Mix\n")
                team_type = input("Enter Your Choice Here: ")
                # Team type should be int and it should be 1, 2, 3
                if not team_type.isdigit() or team_type not in ["1", "2", "3"]:
                    print("Please Select A Valid Choice!!!!!\n")
                else:
                    # Get the correct team type according to the user input choice
                    team_type = next(types for idx, types in enumerate(["Boys", "Girls", "Mix"]) if idx + 1 == int(team_type))
                    # Call the get_a_team_by_gender() method to read team data by team type
                    team_data = self.team_operation.get_a_team_by_gender(team_type)

                    """Display the one team data UI with borders and vertical lines."""
                    print("\n" + "=" + "=" * 40 + "=")
                    print("|" + " " * 5 + f"Information Of The {team_type} Type Teams" + " " * 1 + "|")
                    print("=" + "=" * 40 + "=")

                    #Check whether data is not empty
                    if len(team_data) > 0:
                        self.display_one_team_data(team_data)
                    else:
                        print("No Data Records!!!!!")
                    break

        # If user need to get participation cancelled teams data
        if self.query == "Cancellation":
            # Call the get_all_teams() method to read all team data
            all_team_data = self.team_operation.get_all_teams()[0]
            # Filter the participation cancelled teams
            cancelled_teams = [team for team in all_team_data if team["Cancellation Date"] is None]
            # Check whether data is not empty
            if len(cancelled_teams) > 0:
                """Display the one team data UI with borders and vertical lines."""
                print("\n" + "=" + "=" * 40 + "=")
                print("|" + " " * 5 + f"Participation Cancelled Teams" + " " * 6 + "|")
                print("=" + "=" * 40 + "=")
                self.display_one_team_data(cancelled_teams)
            else:
                print("No Data Records!!!!!")

    def display_UI(self):
        """Display the all teams data UI with borders and vertical lines."""
        print("\n" + "=" + "=" * 40 + "=")
        print("|" + " " * 10 + "All Teams Information" + " " * 9 + "|")
        print("=" + "=" * 40 + "=")

    def handle_options(self):
        """Handle the option selected by the user"""
        # Call the get_user_input function
        user_input = self.get_user_input()

    def __str__(self):
        """string representation of the GetTeamsDataUI class"""
        return f"Get data query type : {self.query}"

if __name__ == "__main__":
    main_menu = GetTeamsDataUI("All")
    main_menu.handle_options()
    #main_menu.get_user_input()
    #print(main_menu)