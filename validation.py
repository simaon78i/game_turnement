"""adding a team validation"""

def validate_team_user_input(user_input):
    try:
        user_id,user_name = user_input.split(",")
    except TypeError:
        raise ValueError("team id and name in the wrong format!!")
    return user_id,user_name


def validate_team(teams,team_id,team_name):
        return validate_id(team_id) \
            and validate_name(team_name) \
            and validate_duplicate(teams,team_id,team_name)


def validate_id(team_id):
    int_team_id = None
    raise_flag = False
    try:
        int_team_id = int(team_id)
    except ValueError:
        raise_flag = True
    if (not raise_flag) and not int_team_id>0:
        raise_flag = True
    if raise_flag:
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

def validate_match(teams,matches,home_team_id,out_team_id,ht_goals,ot_goals):
    validate_goals(ht_goals,ot_goals)
    validate_teams(teams,home_team_id,out_team_id)
    validate_matches_num(matches,home_team_id,out_team_id)


def validate_goals(ht_goals,ot_goals):
    int_ht = None
    int_ot = None
    raise_flag = False
    try:
        int_ht = int(ht_goals)
        int_ot = int(ot_goals)
    except ValueError:
        raise_flag = True
    if (not raise_flag) and int_ht<0 and int_ot <0:
        raise_flag = True
    if raise_flag:
        raise ValueError("teams goals must be an integer greater then zero!")


def validate_teams(teams,home_team_id,out_team_id):
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
        if home_team == home_team_id and away_team == out_team_id or \
            home_team ==out_team_id  and away_team == home_team_id:
            raise ValueError("two groups cannot have multiple games!")


def validate_choice_rate_table(choice):
    int_choice = None
    raise_flag = False
    try:
        int_choice = int(choice)
    except ValueError:
        raise_flag = True
    if (not raise_flag) and 5>int_choice>0:
        raise_flag = True
    if raise_flag:
        raise ValueError("choice must be an integer between 1 to 4!")


def validate_menu_handling(menu_choice):
    int_choice = None
    raise_flag = False
    try:
        int_choice = int(menu_choice)
    except ValueError:
        raise_flag = True
    if (not raise_flag) and (int_choice>10 or int_choice<0):
        raise_flag = True
    if raise_flag:
        raise ValueError("wrong input please choose an integer from 0 to 10!")


def validating_match_input(user_input):
    try:
        home_team,out_team,ht_goals,ot_goals = user_input.split(",")
        return home_team,out_team,ht_goals,ot_goals
    except TypeError as e:
        raise ValueError("teams id and goals are in wrong format!!")