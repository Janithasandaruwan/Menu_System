from abc import ABC, abstractmethod


# Abstract Base Class for CRUD operations
class TeamManager(ABC):

    @abstractmethod
    def create_team(self):
        pass

    @abstractmethod
    def read_team(self):
        pass

    @abstractmethod
    def update_team(self):
        pass

    @abstractmethod
    def delete_team(self):
        pass

    @abstractmethod
    def list_teams(self):
        pass


# Concrete Class for the Team
class Team:
    team_id_counter = 1  # Class variable to auto-increment team IDs

    def __init__(self, name, gender, coach_name):
        self.team_id = Team.team_id_counter
        self.name = name
        self.gender = gender  # Either 'boys' or 'girls'
        self.coach_name = coach_name
        Team.team_id_counter += 1

    def __str__(self):
        return f"ID: {self.team_id}, Name: {self.name}, Gender: {self.gender}, Coach: {self.coach_name}"

    def update_team(self, name=None, gender=None, coach_name=None):
        if name:
            self.name = name
        if gender:
            self.gender = gender
        if coach_name:
            self.coach_name = coach_name


# Concrete Class implementing the abstract CRUD methods
class UserInterface(TeamManager):

    def __init__(self):
        self.teams = []  # List to store Team objects

    # Implements the abstract create method
    def create_team(self):
        name = input("Enter team name: ")
        gender = input("Enter gender (boys/girls): ")
        coach_name = input("Enter coach name: ")
        team = Team(name, gender, coach_name)
        self.teams.append(team)
        print(f"Team '{team.name}' created successfully with ID {team.team_id}.\n")

    # Implements the abstract read method
    def read_team(self):
        try:
            team_id = int(input("Enter team ID to view: "))
            team = next((t for t in self.teams if t.team_id == team_id), None)
            if team:
                print(team)
            else:
                print("Team not found.\n")
        except ValueError:
            print("Invalid input. Please enter a valid team ID.\n")

    # Implements the abstract update method
    def update_team(self):
        try:
            team_id = int(input("Enter team ID to update: "))
            team = next((t for t in self.teams if t.team_id == team_id), None)
            if team:
                name = input(f"Enter new name for '{team.name}' (press Enter to skip): ")
                gender = input(f"Enter new gender (boys/girls) for '{team.gender}' (press Enter to skip): ")
                coach_name = input(f"Enter new coach name for '{team.coach_name}' (press Enter to skip): ")
                team.update_team(name, gender, coach_name)
                print(f"Team '{team.name}' updated successfully.\n")
            else:
                print("Team not found.\n")
        except ValueError:
            print("Invalid input")
