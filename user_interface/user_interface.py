from abc import ABC, abstractmethod

class UserInterface(ABC):
    """Abstract class for row-oriented user interface"""

    @abstractmethod
    def display_UI(self):
        """Display the UI and user options"""
        pass

    @abstractmethod
    def get_user_input(self):
        """Get user input from the user"""
        pass

    @abstractmethod
    def handle_options(self):
        """Handle the option selected by the user"""
