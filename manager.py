import logging
import validation as validate

logging.basicConfig(level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s")

teams = []
matches = []

def add_team(team_id,team_name):
    logging.info("===adding a team====")
    try:
        validate.validate_team(teams,team_id,team_name)
    except (ValueError,TypeError) as e:
        logging.warning(f"error: team wasn't added {e.message}")
        raise AddTeamError(e.message)
    new_team = {"id": team_id, "name": team_name, 
        "played": 0,"wins": 0, "draws": 0, 
        "losses": 0,"goals_for": 0, 
        "goals_against": 0, "points": 0}
    teams.append(new_team)
    logging.info("new team was added successfully :)")

def show_teams(choice = 0):
    if not teams:
        logging.info("team table empty")
        return "there ins't teams yet :("
    display = f""""""
    counter = 1
    for team in teams:
        display+= f"""team number:{counter}\n"""
        if not choice:
               display+=f""" team id:{team.get("id")}\n"""

        display+=f"""team name:{team.get("name")}\n
        stats
        played:{team.get("played")}\n
        wins:{team.get("wins")}\n
        draws{team.get("draws")}\n
        losses{team.get("losses")}\n
        goals for{team.get("goals_for")}\n
        goals against{team.get("goals_against")}\n
        points{team.get("points")}"""
    return display

def add_match(home_team_id,out_team_id,ht_goals,ot_goals):
    try:
        logging.info("adding a match")
        validate_game_score(matches,home_team_id,out_team_id,ht_goals,ot_goals)
    except ValueError as e:
        logging.error("match wasn't added")
        raise AddMatchError(f"error match wasn't added {e.message}")
    logging.info("updating every team stats")
    update_teams_goals_stats(home_team_id,out_team_id,ht_goals,ot_goals)
    match_to_add = {"home_team_id": home_team_id, 
        "away_team_id": out_team_id,
        "home_goals": ht_goals, 
        "away_goals": ot_goals}
    matches.append(match_to_add)
    logging.info("match added successfully :)")

def managing_teams_goals_stats(home_team_id,out_team_id,ht_goals,ot_goals):
    wining_team,losing_team = check_results(home_team_id,out_team_id,ht_goals,ot_goals)
    if wining_team =="draw":
        update_teams(teams,ht_goals,ot_goals,home_team_id,out_team_id,1)
    else:
        wt_goals =0
        lt_goals =0
        if wining_team ==home_team_id:
            wt_goals = ht_goals
            lt_goals = ot_goals
        else:
            wt_goals = ot_goals
            lt_goals = ht_goals
        update_teams(teams,wt_goals,lt_goals,wining_team,losing_team)
        logging.info("the results was added successfully :)")

def update_teams(teams,wt_goals,lt_goals,losing_team,wining_team,draw=0):
    goals_for=0
    goals_against=0
    for team in teams:
        if team.get("id") == wining_team:
            goals_for = wt_goals
            goals_against = lt_goals
        elif team.get("id")==losing_team:
            goals_for = lt_goals
            goals_against = lt_goals
        else:
            continue

        team["played"]+=1
        team["goals_for"]+=goals_for
        team["goals against"]+=goals_against
        if draw==0:
            team["points"]+=3
            team["wins"]+=1
        



def check_results(home_team_id,out_team_id,ht_goals,ot_goals):
    if ht_goals>ot_goals:
        return home_team_id,out_team_id
    elif ht_goals==ot_goals:
        return "draw",1
    return out_team_id,home_team_id

def managing_rating_table_display(choice):
    try:
        validate.validate_choice_rate_table(choice)
    except ValueError as e:
        logging.error("rate request didn't completed")
        raise RateTableError(f"error: {e.message}")
    list_to_display=[]
    if choice ==1:
        list_to_display = sorted(teams,key=lambda t:t["points"],reverse=True)
    elif choice==2:
        list_to_display = sort_by_difference(teams)
    elif choice==3:
        list_to_display = sorted(teams,key=lambda t:t["goals_for"],reverse=True)
    elif choice == 4:
        list_to_display = sorted(teams,key=lambda t:t["name"])
    show_teams(1)

def sort_by_difference():
    teams_cp = teams.copy()
    for team in teams:
        team["difference"] = team.get("goals_for")-team.get("goals_against")
    return sorted(teams_cp,key=lambda t:t["difference"],reverse=True)

    


    
    
