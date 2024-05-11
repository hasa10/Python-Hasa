class CricketMarch():
    def start_game(self):
        #global total_runs,wickets,current_player
        #global playerA_runs
        #global playerB_runs
        #global playerA_name
        #global playerB_name

        playerA_name = input("Enter Player A's name: ")
        playerB_name = input("Enter Player B's name: ")
        print(self)

        self.total_runs = 0
        self.wickets = 0
        self.current_player = playerA_name  # Start with Player A
        self.playerA_runs = 0
        self.playerB_runs = 0
        

    def overs_in_match(self):
        over = 0
        while over < 5 and self.wickets < 4:
            self.ball_in_over(over)
            self.change_player(self)  # Change player after each over
            over += 1
        else:
            print(f'End of Match: {over} overs')
            self.print_final_score(self)

    def ball_in_over(self,over):
        ball = 0
        while ball < 6 and self.wickets < 4:
            print(f'{self.total_runs}/{self.wickets} Over: {over}.{ball}')
            self.score_off_balls()
            ball += 1
        else:
            print(f'End of Over {over}')

    def score_off_balls(self):
        self.total_runs
        self.wickets
        #global current_player
        #global playerA_runs
        #global playerB_runs

        score = input(f'{self.current_player} Score: ')
        if score.isdigit():
            score = int(score)
            if score in (0, 1, 2, 3, 4, 6):
                runs = score
                self.total_runs += runs
                if self.current_player == self.playerA_name:
                    playerA_runs += runs
                else:
                    playerB_runs += runs
                if runs in (1, 3):
                    self.change_player('')
            else:
                print('Invalid input.')
        elif score.lower() == 'w':
            wickets += 1
            if wickets == 4:
                print('Game Over')
            else:
                new_player_name = input("Enter New Player's name: ")
                if new_player_name:
                    self.change_player(new_player_name)
                else:
                    print("Invalid input.")
        else:
            print('Invalid input.')

    def change_player(self,new_player_name=''):
        #global current_player
        if new_player_name:
            self.current_player = new_player_name
        elif self.current_player == self.playerA_name:
            self.current_player = self.playerB_name
        else:
            self.current_player = self.playerA_name

    def print_final_score(self):
        #global playerA_runs
        #global playerB_runs
        print(f"Final Score: {self.playerA_runs + self.playerB_runs} ({self.wickets} wickets)")
        print('Game Over')



def main():
    firstBat = CricketMarch()
    secondBat = CricketMarch()
    firstBat.start_game()
    firstBat.overs_in_match()
    secondBat.start_game()
    secondBat.overs_in_match()
    print('dwe343',firstBat)
    print('eyyu44',secondBat)

if __name__ == "__main__":
    main()
    



