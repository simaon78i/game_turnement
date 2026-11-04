"""adding a team validation"""

def validate_team(teams,team_id,team_name):
        return validate_id(team_id) \
            and validate_name(team_name) \
            and validate_duplicate(teams,team_id,team_name)

def validate_id(team_id):
    if not(isinstance(team_id) == int and team_id>0):
        raise ValueError("team id should be an \
            integer greater then 0!")

def validate_name(team_name):
    if team_name=="":
        raise ValueError("team name cannot be empty!")

def validate_duplicate(teams,team_id,team_name):
    if not teams:
        return
    for team in teams:
        existing_id,existing_name =team.get("id"),team.get("name") 
        if existing_id == team_id:
            raise TypeError("team id already exist please try again")
        elif existing_name == team_name:
            raise TypeError("team name already exist please try again")

"""receive match details validation"""

def validate_match(matches,home_team_id,out_team_id,ht_goals,ot_goals):
    validate_goals(ht_goals,ot_goals)
    validate_teams(home_team_id,out_team_id)
    validate_matches_num(matches,home_team_id,out_team_id)


def validate_goals(ht_goals,ot_goals):
    if not(isinstance(ht_goals) is int and ht_goals>0
        and isinstance(ot_goals) is int and ot_goals >0):
        raise ValueError("teams goals must be an integer greater then zero!")


def validate_teams(home_team_id,out_team_id):
    team_counter = 0
    for team in teams:
        team_id = team.get("id")
        if team_id==home_team_id or team_id==out_team_id:
            team_counter+=1
    if team_counter <2:
        raise ValueError("one of the teams name dos'ent exist please try again")

def validate_matches_num(matches,home_team_id,out_team_id):
    if not matches:
        return
    for match in matches:
        home_team,away_team = match.get("home team id"),match.get("away team id")
        if home_team == home_team_id and away_team == out_team_id:
            raise ValueError("two groups cannot have multiple games!")

def validate_choice_rate_table(choice):
    if not(isinstance(choice) is int and 5>choice>0):
        raise ValueError("choice must be an integer between 1 to 4!")

    
        
        

    


        