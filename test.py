import json
import os

def append_team_data(filename, new_team_data):
    # Create the file with an empty list if it doesn't exist
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            json.dump([], file)  # Initialize with an empty list

    # Read, update, and write data in one block
    with open(filename, 'r+') as file:
        team_data = json.load(file)  # Load existing data (which is a list)
        team_data.append(new_team_data)  # Append the new dictionary
        file.seek(0)  # Go back to the start of the file
        json.dump(team_data, file, indent=4)  # Write the updated list
        file.truncate()  # Remove any extra data if the new data is shorter

# Example usage
filename = 'team_data.txt'

# First append
new_team1 = {
    'team_name': 'Ice Breakers',
    'coach': 'John Doe',
    'players': ['Alice', 'Bob', 'Charlie'],
    'home_rink': 'Rink A'
}
append_team_data(filename, new_team1)

# Second append
new_team2 = {
    'team_name': 'Frozen Warriors',
    'coach': 'Jane Smith',
    'players': ['David', 'Eve', 'Frank'],
    'home_rink': 'Rink B'
}
append_team_data(filename, new_team2)

# Third append (optional)
new_team3 = {
    'team_name': 'Glacial Giants',
    'coach': 'Mike Brown',
    'players': ['George', 'Harry', 'Isabelle'],
    'home_rink': 'Rink C'
}
append_team_data(filename, new_team3)

