'''rr=0
while (rr<100):
    if rr<10:
        print(f"Hasaranga 0{rr}")
    else:
        print(f"Hasaranga {rr}")
    rr+=1


input= input('Enter word:')
result = ""
nambare = 0
while nambare < len(input):
    result += input[nambare]
    nambare += 2
print(result)


num=10


while (num<10000):
    num += 1

    num2= str(num)
    if num2[::-1] == num2:
        print(num2)
    else:
        continue'''












# Initialize variables
over = 0
total_runs = 0
outs = 0
player_A_runs = 0
player_B_runs = 0
player_A_name = 'Wanindu'
player_B_name = 'Hasaranga'
current_batsman = player_A_name

# Loop for overs
while over < 10:
    ball = 1
    while ball <= 6:
        run = input(f'Over {over}.{ball} - player {current_batsman}=')

        if run.lower() == 'out':
            outs += 1
            new_batsman_name = input('Enter New Player Name: ')
            if outs == 2:
                print(f"Over {over + 1}: marks= {total_runs}, outs = {outs}")
                break
            if current_batsman == player_A_name:
                print(f"{player_A_name} scored {player_A_runs} marks")
                player_A_runs = 0
                player_A_name = new_batsman_name
                current_batsman = player_A_name
            else:
                print(f"{player_B_name} scored {player_B_runs} marks")
                player_B_runs = 0
                player_B_name = new_batsman_name
                current_batsman = player_A_name
        else:
            total_runs += int(run)
            if int(run) in [1, 3]:
                if current_batsman == player_A_name:
                    player_A_runs += int(run)
                    current_batsman = player_B_name
                else:
                    player_B_runs += int(run)
                    current_batsman = player_A_name
            else:
                if current_batsman == player_A_name:
                    player_A_runs += int(run)
                else:
                    player_B_runs += int(run)

        ball += 1

    if outs == 2:
        break

    over += 1
    print(f"Over {over}: marks= {total_runs}, outs = {outs}")

print("Game Over")


