

def start_game():
    global total_runs
    global wickets
    total_runs = 0
    wickets = 0

def overs_in_match():
    over = 0
    while over < 5:
        ball_in_over(over)  # positional argument
        over += 1
    else:
        print(f'End of Match: {over} overs')

def ball_in_over(over):
    ball = 0
    while ball < 6:
        print(f'{total_runs}/{wickets} Over: {over}.{ball}')
        score_off_balls()
        ball += 1

def score_off_balls():
    global total_runs
    global wickets
    score = input(' Score: ')
    if score.isdigit():
        score = int(score)
        if score in (0, 1, 2, 3, 4, 6):
            runs = score
            total_runs += runs
    elif score.lower() == 'w':  # Corrected the condition here
        wickets += 1
    else:
        print('not digit')

def print_score():
    pass

start_game()
overs_in_match()
