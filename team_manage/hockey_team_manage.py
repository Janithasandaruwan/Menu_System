import json
import os
from team_manage.hockey_team import HockeyTeam
from team_manage.team_manager import TeamManager
from team_data.file_data_manage import HockeyTeamDataManage
from team_data.temporary_data_mange import TemporaryTeamDataManage

class TeamOperations(TeamManager):
    """Concrete implementation of the team operations using the TeamManager abstract class"""

    # Define __init__ method, class constructor
    def __init__(self, team_objects):
        # Define data_operation object using TemporaryTeamDataManage class for data save and read
        self.data_operation = TemporaryTeamDataManage(team_objects)

    def create_team(self, team_name : str, team_type : str, total_players : int, fee_paid : bool):
        """Creates a new team and save hockey team data temporary"""
        # Call get_next_team_ID() function for get next Team ID
        team_id = self.data_operation.get_next_team_ID()
        # Define the team object from HockeyTeam class with user input data
        team_obj = HockeyTeam(team_id, team_name, team_type, total_players, fee_paid)
        # Return team object
        return team_obj

    def get_a_team_by_id(self, team_id):
        """Get team data by its team ID"""
        # Read all the team data by using read_data() function
        team_data  =  self.data_operation.read_data()
        # Handle errors when user input invalid team ID
        try:
            # Filter the team data by the team_id using generator expression
            filtered_data = (team_data[idx] for idx, data in enumerate(team_data) if data["Team ID"] == team_id)
            # Return the data in the generator using next() function
            return next(filtered_data)
        except Exception as e:
            return []

    def get_all_teams(self):
        """Retrieve details of all teams"""
        # Handle errors when getting all the team data
        try:
            # Read all the team data by using read_data() function
            team_data = self.data_operation.read_data()
            # Get the total team count
            total_team_count = len(team_data)
            # Get the count of fee paid Teams
            fee_paid_teams = len([data for idx, data in enumerate(team_data) if data["Fee Paid Status"] == "True"])
            # Get the percentage of fee paid teams
            percent_fee_paid = (fee_paid_teams / total_team_count) * 100
            # Get all current team IDs
            current_team_ID = [data["Team ID"] for data in team_data]
            # Return all the team data, team count and percentage of fee paid teams
            return team_data, total_team_count, f"{round(percent_fee_paid, 2)} %", current_team_ID
        except Exception as e:
            # Return empty data when no records in the data.txt file
            return ([], 0, 0, [])

    def get_a_team_by_gender(self, gender):
        """Retrieve details of a specific team by gender (boy/ girl)"""
        # Read all the team data by using read_data() function
        team_data = self.data_operation.read_data()
        # Handle errors when user input invalid gender type
        try:
            # Filter the team data by the gender and create a new list for filtered data
            filtered_data = [team_data[idx] for idx, data in enumerate(team_data) if data["Team Type"].lower() == gender.lower()]
            # Return the filtered data list
            return filtered_data
        except Exception as e:
            return []

    def update_team(self, team_id, team_name, team_type, total_players, fee_status, cancellation_date):
        """Update details of a team"""
        # Create new updated data dictionary
        updated_data_dict = {
            "Team Name": team_name,
            "Team Type": team_type,
            "Total Players": total_players,
            "Fee Paid Status": fee_status,
            "Cancellation Date": cancellation_date,
        }
        # Update a team by Team ID using update_data() function
        self.data_operation.update_data(team_id, updated_data_dict)

    def delete_team(self, team_id):
        """Delete a team by its ID"""
        # Delete a team by Team ID using delete_data() function
        team_index = self.data_operation.delete_data(team_id)
        # Return the team index
        return team_index




if __name__ == "__main__":
    team_operator = TeamOperations()
    team_operator.create_team(1, "Test_name", "Boys", 10, 200, True)