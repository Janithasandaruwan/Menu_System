import json
import os
from team_data.data_manage import DataManage
from team_data.file_data_manage import TxtFileDataManage

class TemporaryTeamDataManage(DataManage):
    """Concrete implementation of the hockey team data manage temporary using DataManage abstract class"""

    # Define in the __init__ method
    def __init__(self, team_objects):
        # Current Team objects
        self.team_objects = team_objects
        # File path for store hockey team data
        self.__file_name = "team_data/hockey_team_data.txt"

    # Function for create a file with an empty list if it doesn't exist in the path
    def create_data_file(self):
        if not os.path.exists(self.__file_name):
            with open(self.__file_name, 'w') as file:
                # Initialize with an empty list
                json.dump([], file)

    def read_data(self):
        """Read data in the current team data object"""
        # Handling the errors when encountering the data retrieving
        try:
            # List for get all current data
            loaded_data = []
            # Loop through the team object and create team data dictionary using object getter methods
            for data in self.team_objects:
                data_dict = {
                    "Team ID" : data.team_id,
                    "Registered Date" : f"{data.date_created}",
                    "Team Name": f"{data.team_name}",
                    "Team Type": f"{data.team_type}",
                    "Total Players": f"{data.total_players}",
                    "Total Fee": f"{data.total_fee}",
                    "Fee Paid Status": f"{data.fee_paid}",
                    "Cancellation Date": f"{data.cancelled_date}",
                }
                # Append dict data to the loaded_data list
                loaded_data.append(data_dict)

            # Sort a list of dictionaries by the 'Team ID' key using lambda function
            sorted_data = sorted(loaded_data, key=lambda id_val:id_val["Team ID"])
            # Return all the loaded and sorted data
            return sorted_data
        except Exception as e:
            # Print error message and the warning
            print(f"Error occurred while reading data###########\nError : {e}")

    def update_data(self, team_id, update_data):
        """Update data in the team data objects"""
        # Handling the errors when encountering the data updating
        try:
            # Get the team object that need to update
            team_obj = next(obj for obj in self.team_objects if obj.team_id == team_id)
            # Update the team data using setter methods of the team object
            team_obj.team_name = update_data["Team Name"]
            team_obj.team_type = update_data["Team Type"]
            team_obj.total_players = update_data["Total Players"]
            team_obj.fee_paid = update_data["Fee Paid Status"]
            team_obj.cancelled_date = update_data["Cancellation Date"]
            print(f"Team ID: {team_id} Successfully Updated!********************")
        except Exception as e:
            # Print error message and the warning
            print(f"Error occurred while updating data###########\nError : {e}")

    def delete_data(self, team_id):
        """Delete data in the file"""
        # Handling the errors when encountering the data removing
        try:
            # Get the index of the team object that need to delete
            team_obj_index = next(idx for idx, obj in enumerate(self.team_objects) if obj.team_id == team_id)
            # Print the successful deleted message
            print(f"Team ID: {team_id} Successfully Deleted!********************")
            # Return the team object index
            return team_obj_index
        except Exception as e:
            # Print error message and the warning
            print(f"Error occurred while deleting data###########\nError : {e}")

    def get_next_team_ID(self):
        """Read all team IDs in the existing data and return team ID for next new team creation"""
        # Call the get_all_team_ID() function to get all the current data in the text file
        text_file_id_list = self.get_all_team_ID()
        # Check current data list in the text file and team object list is empty
        if len(text_file_id_list) == 0 and len(self.team_objects) == 0:
            # If the data list empty, the next Team ID should be 1
            return 1
        else:
            # Get all team IDs in team objects
            team_ID_objects = [obj.team_id for obj in self.team_objects]
            # Merge list of team IDs and get the last team ID
            merge_team_ID = text_file_id_list + team_ID_objects
            # Sort the list
            sorted_list = sorted(merge_team_ID)
            # Get the last team ID and sum with 1
            return sorted_list[-1] + 1

    def get_all_team_ID(self):
        """Read all team IDs in the existing data text file"""
        # Create a file_operation object for get all team ID in the text file
        self.file_operation = TxtFileDataManage([], False)
        # Call the get_all_team_ID() function to get all the current data in the text file
        current_data = self.file_operation.get_all_team_ID()
        return current_data

    def save_data(self, team_data):
        """Save data in the file"""
        pass

    def __str__(self):
        """String representation of the TemporaryTeamDataManage class"""
        return f"Hockey team data file path: {self.__file_name}"


if __name__ == "__main__":
    hockey_team_data = TemporaryTeamDataManage([])
    #print(hockey_team_data.update_data(1, {"Team Name": "Janitha", 'Team Type': "Mix", "Total PLayers": 40}))
    #print(hockey_team_data.get_next_team_ID())

