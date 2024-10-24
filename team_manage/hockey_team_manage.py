import json
import os
from team_manage.hockey_team import HockeyTeam
from team_manage.team_manager import TeamManager
from team_data.hockey_team_data import HockeyTeamDataManage

class TeamOperations(TeamManager):
    """Concrete implementation of the team operations using the TeamManager abstract class"""

    # Define __init__ method, class constructor
    def __init__(self):
        # Define file_operation object using HockeyTeamDataManage class for file save and read
        self.file_operation = HockeyTeamDataManage()


    def create_team(self, team_id : int, team_name : str, team_type : str, total_players : int, total_fee : int, fee_paid : bool):
        """Creates a new team and save hockey team data"""
        # Define the team object from HockeyTeam class with user input data
        team = HockeyTeam(team_id, team_name, team_type, total_players, total_fee, fee_paid)
        # Create the hockey data dictionary using getter methods of each attributes
        hockey_data = {
            "Team ID" : team.team_id,
            "Date Registered" : team.date_created,
            "Team Name" : team.team_name,
            "Team Type (Girl/Boy/Mix)" : team.team_type,
            "Total Players" : team.total_players,
            "Total Fee" : f"{team.total_fee} SEK",
            "Fee Status" : team.fee_paid
        }
        # Save user input data
        self.file_operation.save_data(hockey_data)

    def get_a_team_by_id(self, team_id):
        """Get team data by its team ID"""
        # Read all the team data by using read_data() function
        team_data  =  self.file_operation.read_data()
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
            team_data = self.file_operation.read_data()
            # Get the total team count
            total_team_count = len(team_data)
            # Get the count of fee paid Teams
            fee_paid_teams = len([data for idx, data in enumerate(team_data) if data["Fee Status"] == True])
            # Get the percentage of fee paid teams
            percent_fee_paid = (fee_paid_teams / total_team_count) * 100
            # Return all the team data, team count and percentage of fee paid teams
            return team_data, total_team_count, percent_fee_paid
        except Exception as e:
            return []

    def get_a_team_by_gender(self, gender):
        """Retrieve details of a specific team by gender (boy/ girl)"""
        # Read all the team data by using read_data() function
        team_data = self.file_operation.read_data()
        # Handle errors when user input invalid gender type
        try:
            # Filter the team data by the gender and create a new list for filtered data
            filtered_data = [team_data[idx] for idx, data in enumerate(team_data) if data["Team Type (Girl/Boy/Mix)"].lower() == gender.lower()]
            # Return the filtered data list
            return filtered_data
        except Exception as e:
            return []

    def update_team(self, team_id, name=None, team_type=None, number_of_members=None, fee_paid=None):
        """Update details of a team"""
        # Get existing team data
        team_data = self.get_a_team_by_id(team_id)
        # Create new updated data dictionary while checking None values
        update_data = {
            'Team Name' : name if name is not None else team_data["Team Name"],
            'Team Type (Girl/Boy/Mix)' : team_type if team_type is not None else team_data["Team Type (Girl/Boy/Mix)"],
            'Total Players' : number_of_members if number_of_members is not None else team_data['Total Players'],
            #'Total Fee' : number_of_members if number_of_members is not None else team_data['Total Fee'],
            'Fee Status' : fee_paid if fee_paid is not None else team_data['Fee Status']
        }
        # Update a team by Team ID using delete_data() function
        self.file_operation.update_data(team_id, update_data)

    def delete_team(self, team_id):
        """Delete a team by its ID"""
        # Delete a team by Team ID using delete_data() function
        self.file_operation.delete_data(team_id)




if __name__ == "__main__":
    team_operator = TeamOperations()
    team_operator.create_team(1, "Test_name", "Boys", 10, 200, True)