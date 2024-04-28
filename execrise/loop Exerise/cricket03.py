def cricket_start() :
    total = 0
    over = 0
    out = 0
    player_A = "Wanindu"
    player_B = "hasaranga"
    player_A_runs = 0
    player_B_runs = 0
    batsman = player_A
    total_run = 0
    crickeover()



def runs(mark):
    global out, player_A, player_B, player_A_runs, player_B_runs, batsman, total_run

    if mark == "out":
        out += 1
        if out <= 3:
            if batsman == player_A:
                print(f'{player_A} runs = {player_A_runs}')
                new_player = input("Enter new player: ")
                player_A = new_player
                player_A_runs = 0
                batsman = player_A
            else:
                print(f'{player_B} runs = {player_B_runs}')
                new_player = input("Enter new player: ")
                player_B = new_player
                player_B_runs = 0
                batsman = player_B
        else:
            print("Innings Over")
    else:
        runs = int(mark)
        total_run += runs
        if batsman == player_A:
            player_A_runs += runs
            batsman = player_B
        else:
            player_B_runs += runs
            batsman = player_A

        print(f"Batsman: {batsman}")
        print(f"{player_A}: {player_A_runs}")
        print(f"{player_B}: {player_B_runs}")
        print(f"Total Runs: {total_run}")


def ball_in_match():
    global over
    ball = 1
    while ball <= 6:
        mark = input(f'Over {over + 1}.{ball} - {batsman} = ')
        runs(mark)
        ball += 1


def over_in_match():
    global over
    while over < 6:
        ball_in_match()
        over += 1
        if out >= 3:
            print("Innings Over")
            break


def crickeover():
    global over
    over = 0
    print("Starting Cricket Match...")
    over_in_match()
    print("End of Match")
