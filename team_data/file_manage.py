from abc import ABC, abstractmethod

class FileManage(ABC):
    """Abstract class for file manage, store data and retrieve data"""

    @abstractmethod
    def read_data(self):
        """Read data in the file"""
        pass

    @abstractmethod
    def save_data(self, team_data):
        """Save data in the file"""
        pass

    @abstractmethod
    def update_data(self, team_id, update_data):
        """Update data in the file"""
        pass

    @abstractmethod
    def delete_data(self, team_id):
        """Delete data in the file"""
        pass

    @abstractmethod
    def get_next_team_ID(self):
        """Read all team IDs in the existing data and return team ID for next new team creation"""
        pass

