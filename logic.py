import manager
import logging


def find_leading_team():
    logging.debug("leading team")
    list_to_display = manager.managing_rating_table_display(1)
    if not list_to_display:
        logging.info("empty teams list in find leading team")
        print("list is empty :(")
        return
    print("the leading team is :")
    return manager.show_teams(0,[list_to_display[0]])

def find_best_attack():
    logging.debug("best attack")
    if not manager.matches:
        logging.info("empty matches table")
        print("no games yet :(")
        return
    max_num = 0
    for team in manager.teams:
        if team.get("goals_for")>max_num:
            max_num = team.get("goals_for")
    print("teams with best attacks: ")
    for team in manager.teams:
        if team.get("goals_for")==max_num:
            manager.show_teams(0,[team])

def calc_success_rate():
    logging.debug("calculate success rate")
    for team in manager.teams:
        if team["played"] == 0:
            print(f"No Games for team {team["name"]}")
        else:
            print(f"the success rate for team {team["name"]} is: {(100*3*team["points"])/team["played"]}")

def find_no_wins_teams():
    logging.debug("no wining teams ")
    for team in manager.teams:
        if team["played"] > 0 and team["wins"] == 0:
            print(f"team with no wins {manager.show_teams(0,[team])}")

def tournament_summary():
    logging.debug("tournament summary")
    print(f"===tournament summary===")
    print(f"the number of teams: {len(manager.teams)}")
    print(f"the number of games: {len(manager.matches)}")
    goals_num = 0
    number_of_draws = 0
    for team in manager.teams:
        goals_num += team["goals_for"]
        number_of_draws +=team["draws"]
    print(f"total number of goals: {goals_num}")
    print(f"average goals per game: {goals_num/len(manager.matches) \
        if len(manager.matches)>0 else 0}")
    #draws needs to be divide by 2 since it counted both ways
    print(f"the number of draws is: {number_of_draws/2}")
    print(f"the leading team is: \n {find_leading_team()}")

def check_championship_potential():
    for team in manager.teams:
        number_of_matches = team["played"]
        number_of_goals = team["goals_for"]
        team_potential =number_of_goals + \
            (len(manager.teams)-1-number_of_matches)*3
        leading_team = find_leading_team()
        if not find_leading_team():
            return
        if leading_team["goals_for"]<team_potential:
            print(f"this team has the potential to win the tournament!!! \n{
                manager.show_teams(0,[team])}")
        






    

