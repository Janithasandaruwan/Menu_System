from team_manage.hockey_team_manage import TeamOperations



if __name__ == "__main__":
    teamop = TeamOperations()
    teamop.create_team(1, "Test_name", "Boy", 10, 200, True)