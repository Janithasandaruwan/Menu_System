import pickle
import os
from hockey_team import HockeyTeam
from team_manage import TeamManager

class TeamOperations(TeamManager):
    """Concrete implementation of the team operations using the TeamManager abstract class"""

    def __init__(self, file_name="teams_data.pkl"):
        self.file_name = file_name
        self.teams = self.load_teams()

    def load_teams(self):
        """Loads teams from a file using pickle."""
        if os.path.exists(self.file_name):
            with open(self.file_name, 'rb') as file:
                try:
                    return pickle.load(file)
                except EOFError:
                    return {}  # Return empty dict if file is empty or corrupted
        else:
            return {}

    def save_teams(self):
        """Saves the current teams to a file using pickle."""
        with open(self.file_name, 'wb') as file:
            pickle.dump(self.teams, file)

    def create_team(self, name, type_, number_of_members, fee):
        """Creates a new team and adds it to the collection."""
        team = Team(name, type_, number_of_members, fee)
        self.teams[team.id] = team
        print(f"Team '{team.name}' (ID: {team.id}) created successfully.")
        self.save_teams()

    def read_team(self, team_id):
        """Displays details of a specific team."""
        team = self.teams.get(team_id)
        if team:
            print(team)
        else:
            print(f"Team with ID {team_id} does not exist.")

    def read_all_teams(self):
        """Displays details of all teams."""
        if self.teams:
            for team in self.teams.values():
                print(team)
                print("-" * 40)
        else:
            print("No teams registered.")

    def update_team(self, team_id, name=None, type_=None, number_of_members=None, fee=None, fee_paid=None):
        """Updates the details of an existing team."""
        team = self.teams.get(team_id)
        if team:
            if name: team.name = name
            if type_: team.type = type_
            if number_of_members: team.number_of_members = number_of_members
            if fee: team.fee = fee
            if fee_paid is not None: team.fee_paid = fee_paid

            print(f"Team '{team.name}' (ID: {team.id}) updated successfully.")
            self.save_teams()
        else:
            print(f"Team with ID {team_id} does not exist.")

    def delete_team(self, team_id):
        """Deletes a team by its ID."""
        if team_id in self.teams:
            team_name = self.teams[team_id].name
            del self.teams[team_id]
            print(f"Team '{team_name}' deleted successfully.")
            self.save_teams()
        else:
            print(f"Team with ID {team_id} does not exist.")
