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
            "Total PLayers" : team.total_players,
            "Total Fee" : f"{team.total_fee} SEK",
            "Fee Status" : team.fee_paid
        }
        # Save user input data
        self.file_operation.save_data(hockey_data)




if __name__ == "__main__":
    team_operator = TeamOperations()
    team_operator.create_team(1, "Test_name", "Boys", 10, 200, True)