def start_game():
    global total_runs
    global wickets
    global current_player
    global playerA_runs
    global playerB_runs
    global playerA_name
    global playerB_name

    playerA_name = input("Enter Player A's name: ")
    playerB_name = input("Enter Player B's name: ")

    total_runs = 0
    wickets = 0
    current_player = playerA_name  # Start with Player A
    playerA_runs = 0
    playerB_runs = 0

def overs_in_match():
    over = 0
    while over < 5 and wickets < 4:
        ball_in_over(over)
        change_player()  # Change player after each over
        over += 1
    else:
        print(f'End of Match: {over} overs')
        print_final_score()

def ball_in_over(over):
    ball = 0
    while ball < 6 and wickets < 4:
        print(f'{total_runs}/{wickets} Over: {over}.{ball}')
        score_off_balls()
        ball += 1
    else:
        print(f'End of Over {over}')

def score_off_balls():
    global total_runs
    global wickets
    global current_player
    global playerA_runs
    global playerB_runs

    score = input(f'{current_player} Score: ')
    if score.isdigit():
        score = int(score)
        if score in (0, 1, 2, 3, 4, 6):
            runs = score
            total_runs += runs
            if current_player == playerA_name:
                playerA_runs += runs
            else:
                playerB_runs += runs
            if runs in (1, 3):
                change_player('')
        else:
            print('Invalid input.')
    elif score.lower() == 'w':
        wickets += 1
        if wickets == 4:
            print('Game Over')
        else:
            new_player_name = input("Enter New Player's name: ")
            if new_player_name:
                change_player(new_player_name)
            else:
                print("Invalid input.")
    else:
        print('Invalid input.')

def change_player(new_player_name=''):
    global current_player
    if new_player_name:
        current_player = new_player_name
    elif current_player == playerA_name:
        current_player = playerB_name
    else:
        current_player = playerA_name

def print_final_score():
    global playerA_runs
    global playerB_runs
    print(f"Final Score: {playerA_runs + playerB_runs} ({wickets} wickets)")
    print('Game Over')

start_game()
overs_in_match()
