import json
from file_manage import FileManage

class HockeyTeamDataManage(FileManage):
    """Concrete implementation of the hockey team data manage using FileManage abstract class"""

    # Define in the __init__ method
    def __init__(self):
        # File path for store hockey team data
        self.__file_name = "hockey_team_data.txt"

    def read_data(self):
        """Read data in the file"""
        # Reading data from the .txt file using JSON
        # Handling the errors when encountering the data retrieving
        try:
            # Open the .txt file in read mode
            with open(self.__file_name, "r") as file:
                # Deserialize the JSON data
                loaded_data = json.load(file)
            # Print the successful read message
            print("Data Successfully Retrieved!********************")
            # Return all the loaded data
            return loaded_data
        except Exception as e:
            # Print error message and the warning
            print(f"Error occurred while reading data###########\nError : {e}")


    def save_data(self, team_data):
        """Save data in the hockey_team_data.txt file"""
        # Saving data to a .txt file using JSON
        # Handling the errors when encountering the data saving
        try:
            # Open the .txt file in write mode
            with open(self.__file_name, "w") as file:
                # Serialize and save data as JSON (with indentation for readability)
                json.dump(team_data, file, indent = 4)
            # Print the successful saved message
            print("Data Successfully Saved!********************")
        except Exception as e:
            # Print error message and the warning
            print(f"Error occurred while saving data###########\nError : {e}")


    def __str__(self):
        """String representation of the HockeyTeamDataManage class"""
        return f"Hockey team data file path: {self.__file_name}"



if __name__ == "__main__":
    hockey_team_data = HockeyTeamDataManage()
    print(hockey_team_data)
    # Data to be serialized (could be any Python object)
    data = {
        "team": "Hockey Heroes",
        "players": ["Alice", "Bob", "Charlie"],
        "coach": "Coach Carter"
    }

    print(hockey_team_data.read_data())

