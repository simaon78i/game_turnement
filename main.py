import manager
from exceptions import AddTeamError,AddMatchError,InputError
from textwrap import dedent
import logic

MENU_MESSAGE = dedent(
        """
        ========== TOURNAMENT MANAGER ==========
        1. Add team
        2. Show all teams
        3. Add match result
        4. Show standings
        5. Show leading team
        6. Show best attacking team
        7. Show team success rate
        8. Show teams without wins
        9. Show tournament summary
        10. Check championship potential
        0. Exit
        Choose an option:
        """)

def menu_handling(menu_choice):
    try:
        manager.menu_handling(menu_choice)
    except InputError as e:
        print(e)
    int_menu_choice =11 if not menu_choice.isdigit() else int(menu_choice)
    while int_menu_choice !=0:
        if int_menu_choice==1:
            receive_team()
        elif int_menu_choice==2:
            manager.show_teams()
        elif int_menu_choice==3:
            receive_match()
        elif int_menu_choice==4:
            manager.managing_rating_table_display()
        elif int_menu_choice==5:
            logic.find_leading_team()
        elif int_menu_choice==6:
            logic.find_best_attack()
        elif int_menu_choice==7:
            logic.calc_success_rate()
        elif int_menu_choice==8:
            logic.find_no_wins_teams()
        elif int_menu_choice==9:
            logic.tournament_summary()
        elif int_menu_choice ==10:
            logic.check_championship_potential()
        menu_choice = input(MENU_MESSAGE)
        try:
            manager.menu_handling(menu_choice)
        except InputError as e:
            print(e)
            continue
        int_menu_choice = int(menu_choice)


def receive_team():
    loop_flag = False
    user_input = 1
    while not loop_flag and user_input!="0":
        user_input = input("please enter team id,team name only separated by , without spaces: 0 back to menu ")
        try:
            manager.add_team(user_input)
            loop_flag=True
        except AddTeamError as e:
            print(e)


def receive_match():
    loop_flag =False
    user_input = 1
    while not loop_flag and user_input!="0":
        user_input = input("please insert the match details: home team,away_team,home goals,away goals: 0 back to menu ")
        try:
            manager.add_match(user_input)
            loop_flag = True
        except AddMatchError as e:
            print(e)

def main():
    menu_choice = input(MENU_MESSAGE)
    menu_handling(menu_choice)


if __name__=="__main__":
    main()