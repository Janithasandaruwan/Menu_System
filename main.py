from team_manage.hockey_team_manage import TeamOperations



if __name__ == "__main__":
    team_opeartion = TeamOperations()
    #team_opeartion.create_team("Test_name4", "Mix", 13, True)
    #print(team_opeartion.get_a_team_by_id(1))
    #team_opeartion.delete_team(3)
    #team_opeartion.update_team(1, "Sandaruwan", "Girl", 40, True)
    #print(team_opeartion.get_all_teams())
    print(team_opeartion.get_a_team_by_gender("boys"))