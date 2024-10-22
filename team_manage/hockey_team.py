from datetime import datetime

class HockeyTeam:
    """Class for hockey team and its private instance"""

    # Define the __init__ method, the class constructor
    def __init__(self, team_id : int, team_name : str, team_type : str, total_players : int, total_fee : int, fee_paid : bool):
        self.__team_id = team_id # Team id
        self.__date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # The date that team registered
        self.__team_name = team_name # Team name
        self.__team_type = team_type # Team type
        self.__total_players = total_players # Total number of players
        self.__total_fee = total_fee # Total fee for participate in the event
        self.__fee_paid = fee_paid # Boolean for fee paid or not

    # Define the getter method for team ID
    @property
    def team_id(self):
        return self.__team_id

    # Define the getter method for team created date
    @property
    def date_created(self):
        return self.__date_created

    # Define getter and setter method for team name
    @property
    def team_name(self):
        return self.__team_name

    @team_name.setter
    def team_name(self, name):
        # Check whether team name is empty
        if not name.strip():
            raise ValueError("Team name cannot be empty!")
        return self.__team_name

    # Define getter and setter method for team type
    @property
    def team_type(self):
        return self.__team_type

    @team_type.setter
    def team_type(self, type):
        # Check whether team type is mix, girl, boy
        if type.lower() not in ['mix', 'boys', 'girls']:
            raise ValueError("Team type must be mix, girls or boys!")
        self.__team_type = type

    # Define getter and setter method for total players
    @property
    def total_players(self):
        return self.__total_players

    @total_players.setter
    def total_players(self, count):
        # Check whether total players count is positive integer
        if not isinstance(count, int) or count <= 0:
            raise ValueError("Number of players must be a positive integer!")
        self.__total_players = count

    # Define getter and setter method for total fee
    @property
    def total_fee(self):
        return self.__total_fee

    @total_fee.setter
    def total_fee(self, value):
        # Check whether fee is non-negative
        if value < 0:
            raise ValueError("Fee cannot be negative!")
        self.__total_fee = value

    # Define getter and setter method for fee status
    @property
    def fee_paid(self):
        return self.__fee_paid

    @fee_paid.setter
    def fee_paid(self, value):
        # Check whether fee status is boolean value
        if not isinstance(value, bool):
            raise ValueError("Fee paid status must be a boolean value!")
        self.__fee_paid = value

    def __str__(self):
        """The string representation of the class"""
        return (f"Team ID: {self.__team_id}\n"
                f"Date Created: {self.__date_created.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Team Name: {self.__team_name}\n"
                f"Team Type: {self.__team_type}\n"
                f"Total Players: {self.__total_players}\n"
                f"Total Fee: ${self.__total_fee}\n"
                f"Fee Paid Status: {self.__fee_paid}\n")



if __name__ == "__main__":
    team = HockeyTeam("test_id", "test_name", "test_type", 20, 200, "TRUE")
    team.team_type = "Boys"
    team.total_players = 10
    team.fee_paid = True
    print(team.date_created)









