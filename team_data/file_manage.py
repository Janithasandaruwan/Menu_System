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