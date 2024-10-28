import json
import os
from team_data.data_manage import DataManage

class TxtFileDataManage(DataManage):
    """Concrete implementation of the hockey team data manage using FileManage abstract class"""

    # Define in the __init__ method
    def __init__(self, team_objects):
        # File path for store hockey team data
        self.__file_name = "team_data/hockey_team_data.txt"
        # Current Team objects
        self.team_objects = team_objects

    # Function for create a file with an empty list if it doesn't exist in the path
    def create_data_file(self):
        if not os.path.exists(self.__file_name):
            with open(self.__file_name, 'w') as file:
                # Initialize with an empty list
                json.dump([], file)

    # Function for loop through the team objects list and create a team data list of dict
    def create_team_data_list(self):
        # List for get all current data
        loaded_data = []
        # Loop through the team object and create team data dictionary using object getter methods
        for data in self.team_objects:
            data_dict = {
                "Team ID": data.team_id,
                "Registered Date": f"{data.date_created}",
                "Team Name": f"{data.team_name}",
                "Team Type": f"{data.team_type}",
                "Total Players": f"{data.total_players}",
                "Total Fee": f"{data.total_fee}",
                "Fee Paid Status": f"{data.fee_paid}",
                "Cancellation Date": f"{data.cancelled_date}",
            }
            # Append dict data to the loaded_data list
            loaded_data.append(data_dict)
        # Return the data list
        return loaded_data

    def read_data(self):
        """Read data in the file"""
        # Reading data from the .txt file using JSON
        # Handling the errors when encountering the data retrieving
        try:
            # Call the create the file function if path doesn't exist the data txt file
            self.create_data_file()

            # Open the .txt file in read mode
            with open(self.__file_name, "r") as file:
                # Deserialize the JSON data
                loaded_data = json.load(file)
            # Print the successful read message
            #print("Data Successfully Retrieved!********************")
            # Sort a list of dictionaries by the 'Team ID' key using lambda function
            sorted_data = sorted(loaded_data, key=lambda id_val:id_val["Team ID"])
            # Return all the loaded and sorted data
            return sorted_data
        except Exception as e:
            # Print error message and the warning
            print(f"Error occurred while reading data###########\nError : {e}")

    def save_data(self, team_data):
        """Save data in the hockey_team_data.txt file"""
        # Saving data to a .txt file using JSON
        # Handling the errors when encountering the data saving
        try:
            # Call the create_team_data_list() to get the team data
            team_data = self.create_team_data_list()

            # Open the .txt file in read and write mode
            with open(self.__file_name, "r+") as file:
                # Read current data list as JSON
                current_data = json.load(file)
                # Append team data to the current data
                current_data = current_data + team_data
                # Go back to the beginning of the file
                file.seek(0)
                # Serialize and save data as JSON (with indentation for readability)
                json.dump(current_data, file, indent=4)
                # Remove any leftover data
                file.truncate()
            # Print the successful saved message
            print("Data Successfully Upload To Text File!!!!!")
        except Exception as e:
            # Print error message and the warning
            print(f"Error occurred while saving data###########\nError : {e}")

    def update_data(self, team_id, update_data):
        """Update data in the file"""
        pass

    def delete_data(self, team_id):
        """Delete data in the file"""
        pass

    def get_next_team_ID(self):
        """Read all team IDs in the existing data and return team ID for next new team creation"""
        # Call the read_data() function to get all the current data
        current_data = self.read_data()
        # Check current data list is not empty and get the last team ID
        if len(current_data) == 0:
            # If the data list empty, the next Team ID should be 1
            return 1
        else:
            # Get the last team ID and sum with 1
            return current_data[-1]["Team ID"] + 1

    def __str__(self):
        """String representation of the HockeyTeamDataManage class"""
        return f"Hockey team data file path: {self.__file_name}"


if __name__ == "__main__":
    hockey_team_data = TxtFileDataManage()
    #print(hockey_team_data.update_data(1, {"Team Name": "Janitha", 'Team Type': "Mix", "Total PLayers": 40}))
    #print(hockey_team_data.get_next_team_ID())

