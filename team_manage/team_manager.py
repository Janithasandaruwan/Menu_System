from abc import ABC, abstractmethod

class TeamManager(ABC):
    """Abstract class for manage hockey team data"""

    @abstractmethod
    def create_team(self, name, team_type, number_of_members, fee_paid):
        """Create a new team"""
        pass

    # @abstractmethod
    # def get_a_team_by_id(self, team_id):
    #     """Retrieve details of a specific team by ID"""
    #     pass
    #
    # @abstractmethod
    # def get_a_team_by_gender(self, gender):
    #     """Retrieve details of a specific team by gender (boy/ girl)"""
    #     pass
    #
    # @abstractmethod
    # def get_all_teams(self):
    #     """Retrieve details of all teams"""
    #     pass
    #
    # @abstractmethod
    # def update_team(self, team_id, name=None, team_type=None, number_of_members=None, fee_paid=None):
    #     """Update details of a team"""
    #     pass
    #
    # @abstractmethod
    # def delete_team(self, team_id):
    #     """Delete a team by its ID"""
    #     pass