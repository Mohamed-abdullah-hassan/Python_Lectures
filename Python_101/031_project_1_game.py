#Python Rock, Paper, Scissors
#from Video #31
import random

game = ["Rock", "Paper", "Scissors"]
print(game[1])
userScore = 0
compScore = 0
while True:
    user = input("Enter 1 for Rock, 2 For Paper, 3 for Scissors, 0 to quit:  ")
    if(user.isnumeric()):
        user = int(user)
        if user >3:
            print("Wrong Answer Please enter 1 or 2 or 3 or 0")
            continue    
    else:
        print("Wrong Answer Please enter 1 or 2 or 3 or 0")
        continue
    chose = random.choice(game)
    if user == 0:
        break
    print("\nYou  Selected (",game[user-1],"), and Computer Selected (",chose,") ")
    if game[user-1] == chose:
        print("It's a Tie")
    elif chose == 'Rock' and game[user-1] == "Paper":
        print("You Win")
        userScore = userScore +1
    elif chose == 'Paper' and game[user-1] == "Scissors":
        print("You Win")
        userScore = userScore +1
    elif chose == 'Scissors' and game[user-1] == "Rock":
        print("You Win")
        userScore = userScore +1
    else:
        print("Computer wins!!!\n \n")
        compScore = compScore +1
    print(f"Score:\n    User {userScore}\n    Computer {compScore}\n")
