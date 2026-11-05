import logging
import validation as validate
from exceptions import AddTeamError,AddMatchError,InputError
# from mock_data import teams,matches

#CONSTANTS
INITIAL_DEFAULT_VAL=0

logging.basicConfig(level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s")

teams = []
matches = []

def add_team(user_input):
    user_id=""
    user_name=""
    logging.info("===adding a team====")
    try:
        team_id,team_name = validate.validate_team_user_input(user_input)
        validate.validate_team(teams,team_id,team_name)
        team_id = int(team_id)
    except (ValueError,TypeError) as e:
        logging.warning(f"error: team wasn't added {e}")
        raise AddTeamError(e)
    new_team = {"id": team_id, "name": team_name, 
        "played": INITIAL_DEFAULT_VAL,"wins": INITIAL_DEFAULT_VAL, "draws": INITIAL_DEFAULT_VAL, 
        "losses": INITIAL_DEFAULT_VAL,"goals_for": INITIAL_DEFAULT_VAL, 
        "goals_against": INITIAL_DEFAULT_VAL, "points": INITIAL_DEFAULT_VAL}
    teams.append(new_team)
    logging.info("new team was added successfully :)")


def show_teams(choice = 0,list_to_display=None):
    if not teams:
        logging.info("team table empty")
        print("there ins't teams yet :(")
    display = f""""""
    counter = 1
    teams_cp = teams.copy()
    #using a copy of teams in order not to run over the original list
    if list_to_display != None:
        teams_cp = list_to_display
    for team in teams_cp:
        display+= f"""team number:{counter}\n"""
        #choice is a default predicate for mission 5, we ordered not to 
        # show id in this case
        if not choice:
               display+=f""" team id:{team.get("id")}\n"""
        display+=f"""team name:{team.get("name")}\n

        ===stats===

        played: {team.get("played")}\n
        wins: {team.get("wins")}\n
        draws: {team.get("draws")}\n
        losses: {team.get("losses")}\n
        goals for: {team.get("goals_for")}\n
        goals against: {team.get("goals_against")}\n
        points: {team.get("points")}\n\n"""
        counter+=1
    print(display)

def add_match(user_input):
    home_team_id=INITIAL_DEFAULT_VAL
    out_team_id=INITIAL_DEFAULT_VAL
    ht_goals=INITIAL_DEFAULT_VAL
    ot_goals=INITIAL_DEFAULT_VAL
    try:
        logging.info("adding a match")
        home_team_id,out_team_id,ht_goals,ot_goals=validate.validating_match_input(user_input)
        home_team_id=int(home_team_id)
        out_team_id=int(out_team_id)
        ht_goals=int(ht_goals)
        ot_goals=int(ot_goals)
        validate.validate_match(teams,matches,home_team_id,out_team_id,ht_goals,ot_goals)
        logging.info("updating every team stats")
        managing_teams_goals_stats(home_team_id,out_team_id,ht_goals,ot_goals)
        match_to_add = {"home_team_id": home_team_id, 
            "away_team_id": out_team_id,
            "home_goals": ht_goals, 
            "away_goals": ot_goals}
        matches.append(match_to_add)
        logging.info("match added successfully :)")
    except ValueError as e:
        logging.error("match wasn't added")
        raise AddMatchError(f"error match wasn't added {e}")

def managing_teams_goals_stats(home_team_id,out_team_id,ht_goals,ot_goals):
    wining_team,losing_team = check_results(home_team_id,out_team_id,ht_goals,ot_goals)
    if wining_team =="draw":
        update_teams(teams,ht_goals,ot_goals,home_team_id,out_team_id,1)
    else:
        wt_goals =INITIAL_DEFAULT_VAL
        lt_goals =INITIAL_DEFAULT_VAL
        if wining_team ==home_team_id:
            wt_goals = ht_goals
            lt_goals = ot_goals
        else:
            wt_goals = ot_goals
            lt_goals = ht_goals
        update_teams(teams,wt_goals,lt_goals,losing_team,wining_team)
        logging.info("the results was added successfully :)")

def update_teams(teams,wt_goals,lt_goals,losing_team,wining_team,draw=0):
    goals_for=0
    goals_against=0
    for team in teams:
        if team.get("id") == wining_team:
            goals_for = wt_goals
            goals_against = lt_goals
            team["wins"]+=1
        elif team.get("id")==losing_team:
            goals_for = lt_goals
            goals_against = wt_goals
            team["losses"]+=1

        else:
            continue

        team["played"]+=1
        team["goals_for"]+=goals_for
        team["goals_against"]+=goals_against
        if draw==0:
            team["points"]+=3
        

def check_results(home_team_id,out_team_id,ht_goals,ot_goals):
    if ht_goals>ot_goals:
        return home_team_id,out_team_id
    elif ht_goals==ot_goals:
        return "draw",1
    return out_team_id,home_team_id

def managing_rating_table_display(leading_team = None):
    """
    note: im using sorting from the list significant order,
    i took this theory from the Radix Sort algorithm idea.
    """
    if not teams:
        return
    list_to_display = sorted(teams,key=lambda t:t["name"])
    list_to_display = sorted(list_to_display,key=lambda t:t["goals_for"],reverse=True)
    list_to_display = sort_by_difference(list_to_display)
    list_to_display = sorted(list_to_display,key=lambda t:t["points"],reverse=True)
    #default value in order not to print when using the leading_team function
    logging.info("list sorted by reversing the priorities demanded")
    if not leading_team:
        show_teams(1,list_to_display)
    return list_to_display

def sort_by_difference(list_to_display):
    for team in list_to_display:
        team["difference"] = team.get("goals_for")-team.get("goals_against")
    return sorted(list_to_display,key=lambda t:t["difference"],reverse=True)

def menu_handling(menu_choice):
    try:
        validate.validate_menu_handling(menu_choice)
        logging.info("menu is success")
    except ValueError as e:
        logging.error("wrong user input in menu")
        raise InputError(e)