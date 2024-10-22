from team_manage.hockey_team_manage import TeamOperations



if __name__ == "__main__":
    team_opeartion = TeamOperations()
    #team_opeartion.create_team(1, "Test_name", "Boy", 10, 200, True)
    #print(team_opeartion.get_a_team_by_id(1))
    print(team_opeartion.get_all_teams())
    #print(team_opeartion.get_a_team_by_gender("girl"))