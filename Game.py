import random
import time


print("Rock...".lower())
time.sleep(0.5)
print("Paper...".lower())
time.sleep(0.5)
print("Scissors...".lower())
time.sleep(0.5)
print("------------------")



player1_wins = 0
player2_wins = 0
winning_score = int(input("Enter your winnig score: "))

while player1_wins != winning_score and player2_wins != winning_score:
    
    randomNumber = random.randint(0, 2)

    if randomNumber == 0:
        computerMove = "rock" #سنگ
    elif randomNumber == 1:
        computerMove = "paper" #کاغذ
    elif randomNumber == 2:
        computerMove = "scissors" # قیچی

    # movements = ["rock" , "paper" , "scissors"]
    # computerMove = random.choice(movements)
    # #Tabloo Emtyazat


    print(f"player 1 : {player1_wins} and player 2 : {player2_wins}")
    player_1 = input("player_1 , Make your move : ").lower()
    player_2 = computerMove
    
    if player_1 == "q" or player_1 == "quit":
        break
    elif player_1 == player_2:
        print("thats a tie ...")
    elif player_1 == "rock":
        if player_2 == "scissors":
            print("player_1 wins!....")
            player1_wins += 1
        elif player_2 == "paper":
            print("player_2 wins!...")
            player2_wins += 1
    elif player_1 == "paper":
        if player_2 == "rock":
            print("player_1 wins!...")
            player1_wins += 1
        elif player_2 == "scissors":
            print("player_2 wins!...")
            player2_wins += 1
    elif player_1 == "scissors":
        if player_2 == "paper":
            print("player_1 wins!...")
            player1_wins += 1
        elif player_2 == "rock":
            print("player_2 wins!...")
            player2_wins += 1
    else:
        print("something went wrong ....")

print(f"Final Scores: player 1 : {player1_wins} | player 2 : {player2_wins}")
if player1_wins > player2_wins:
    print("player1 wins!...")
else:
    print("player2 wins!...")

