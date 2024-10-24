import json
import os
from team_data.file_manage import FileManage

class HockeyTeamDataManage(FileManage):
    """Concrete implementation of the hockey team data manage using FileManage abstract class"""

    # Define in the __init__ method
    def __init__(self):
        # File path for store hockey team data
        self.__file_name = "team_data/hockey_team_data.txt"

    # Function for create a file with an empty list if it doesn't exist in the path
    def create_data_file(self):
        if not os.path.exists(self.__file_name):
            with open(self.__file_name, 'w') as file:
                # Initialize with an empty list
                json.dump([], file)

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
            print("Data Successfully Retrieved!********************")
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
            # Call the create the file function if path doesn't exist the data txt file
            self.create_data_file()

            # Open the .txt file in read and write mode
            with open(self.__file_name, "r+") as file:
                # Read current data list as JSON
                current_data = json.load(file)
                # Append team data to the current data
                current_data.append(team_data)
                # Go back to the beginning of the file
                file.seek(0)
                # Serialize and save data as JSON (with indentation for readability)
                json.dump(current_data, file, indent=4)
                # Remove any leftover data
                file.truncate()
            # Print the successful saved message
            print("Data Successfully Saved!********************")
        except Exception as e:
            # Print error message and the warning
            print(f"Error occurred while saving data###########\nError : {e}")

    def update_data(self, team_id, update_data):
        """Update data in the file"""
        # Handling the errors when encountering the data updating
        try:
            # Call the create the file function if path doesn't exist the data txt file
            self.create_data_file()

            # Open the .txt file in read and write mode
            with open(self.__file_name, "r+") as file:
                # Read current data list as JSON
                current_data = json.load(file)
                # Check whether Team ID is exist in current data list using any function
                if any(item["Team ID"] ==  team_id for item in current_data):
                    # Loop through the current data and update with updated data
                    for team_data in current_data:
                        # Find the item that need to be updated
                        if team_data['Team ID'] == team_id:
                            # Update the data with new data and break the loop
                            team_data.update(update_data)
                            break
                    # Go back to the beginning of the file
                    file.seek(0)
                    # Serialize and save data as JSON (with indentation for readability)
                    json.dump(current_data, file, indent=4)
                    # Remove any leftover data
                    file.truncate()
                    # Print the successful updated message
                    print(f"Team ID: {team_id} successfully updated!********************")
                else:
                    # If Team ID is not exist in the current data, show the warning messages
                    print(f"Team ID: {team_id} not found!######################")
        except Exception as e:
            # Print error message and the warning
            print(f"Error occurred while updating data###########\nError : {e}")

    def delete_data(self, team_id):
        """Delete data in the file"""
        # Handling the errors when encountering the data removing
        try:
            # Call the create the file function if path doesn't exist the data txt file
            self.create_data_file()

            # Open the .txt file in read and write mode
            with open(self.__file_name, "r+") as file:
                # Read current data list as JSON
                current_data = json.load(file)
                # Check whether Team ID is exist in current data list using any function
                if any(item["Team ID"] ==  team_id for item in current_data):
                    # Recreate the new data list without deleted item
                    new_data_list = [item for item in current_data if item['Team ID'] != team_id]
                    # Go back to the beginning of the file
                    file.seek(0)
                    # Serialize and save data as JSON (with indentation for readability)
                    json.dump(new_data_list, file, indent=4)
                    # Remove any leftover data
                    file.truncate()
                    # Print the successful saved message
                    print(f"Team ID: {team_id} successfully deleted!********************")
                else:
                    # If Team ID is not exist in the current data, show the warning messages
                    print(f"Team ID: {team_id} not found!######################")
        except Exception as e:
            # Print error message and the warning
            print(f"Error occurred while deleting data###########\nError : {e}")

    def __str__(self):
        """String representation of the HockeyTeamDataManage class"""
        return f"Hockey team data file path: {self.__file_name}"


if __name__ == "__main__":
    hockey_team_data = HockeyTeamDataManage()
    print(hockey_team_data.update_data(1, {"Team Name": "Janitha", 'Team Type (Girl/Boy/Mix)': "Mix", "Total PLayers": 40}))
    print(hockey_team_data.read_data())

