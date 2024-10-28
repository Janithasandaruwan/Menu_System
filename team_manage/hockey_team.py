from datetime import datetime

class HockeyTeam:
    """Class for hockey team and its private instance"""

    # Define the __init__ method, the class constructor
    def __init__(self,
                 team_ID : int,
                 date_created : None,
                 team_name : str,
                 team_type : str = "Boys",
                 total_players : int = 0,
                 total_fee = None,
                 fee_paid : bool = False,
                 cancelled_date: str = None,
                 ):
        self.__team_id = team_ID # Team id
        # The date that team registered
        # Get the current date when the team object created newly
        # Get the existing date when the data restoring from the file
        self.__date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S") if date_created is None else date_created
        self.__team_name = team_name # Team name
        self.__team_type = team_type # Team type
        self.__total_players = total_players # Total number of players
        self.__fee_paid = fee_paid # Boolean for fee paid or not
        self.__cancelled_date = cancelled_date # Cancelled date of the team participation
        # Total fee calculated from the total number of players, and 100 SEK for one player
        self.__total_fee = 100 * int(total_players)  # Total fee for participate in the event

    # Define the getter method for team ID
    @property
    def team_id(self):
        return self.__team_id

    # Define the getter method for team created date
    @property
    def date_created(self):
        return self.__date_created

    # Define the getter method for total fee
    @property
    def total_fee(self):
        return self.__total_fee

    # Define getter and setter method for team name
    @property
    def team_name(self):
        return self.__team_name

    @team_name.setter
    def team_name(self, name):
        # Check whether team name is empty
        print(name)
        if not name.strip():
            raise ValueError("Team name cannot be empty!")
        self.__team_name = name

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
        # Change the total fee, when the number of player count change
        self.__total_fee = 100 * count

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

    # Define getter and setter method for cancellation date
    @property
    def cancelled_date(self):
        return self.__cancelled_date

    @cancelled_date.setter
    def cancelled_date(self, value):
        # Check whether cancellation date is string if it is not None
        if value is not None:
            if not isinstance(value, str):
                raise ValueError("Cancellation date must be string value!")
            else:
                self.__cancelled_date = value

    def __str__(self):
        """The string representation of the class"""
        return (f"Team ID: {self.__team_id}\n"
                f"Date Created: {self.__date_created}\n"
                f"Team Name: {self.__team_name}\n"
                f"Team Type: {self.__team_type}\n"
                f"Total Players: {self.__total_players}\n"
                f"Total Fee: {self.__total_fee} SEK\n"
                f"Fee Paid Status: {self.__fee_paid}\n"
                f"Cancellation Status: {self.__cancelled_date}\n")



if __name__ == "__main__":
    team = HockeyTeam("test_id", "test_name", "test_type", 20, False, "2024-12-10")
    print(team)
    #print(team.total_fee)









