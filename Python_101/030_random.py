
import random
game = ["Rock", "Paper", "Scissors"]
num = 0
rock =0
paper = 0
sciss = 0
while num < 10:
    chose = random.choice(game)
    print(chose)
    num = num +1
num = 0
maxNum = 10000000
print(f"\nIterating random for {maxNum}, and calculating the percent of each selection")
while num < maxNum:
    chose = random.choice(game)
    if chose == "Rock":
        rock = rock+1
    elif chose == "Paper":
        paper = paper +1
    else:
        sciss = sciss +1
    num = num +1

print(f"\nCompleted Iterating random {num}")
print(f"Rock apeared: {rock} times, with percent of: {rock*100/maxNum}%")
print(f"Paper apeared: {paper} times, with percent of: {paper*100/maxNum}%")
print(f"Scissors apeared: {sciss} times, with percent of: {sciss*100/maxNum}%")

num = 0
rock =0
paper = 0
sciss = 0
pervChose = None

print(f"\nIterating random for {maxNum}, and counting repetetion")
while num < maxNum:
    chose = random.choice(game)
    if chose == "Rock":
        if pervChose == "Rock":
            rock = rock +1
        pervChose = "Rock"
    elif chose == "Paper":
        if pervChose == "Paper":
            paper = paper +1
        pervChose = "Paper"
    else:
        if pervChose == "Scissors":
            sciss = sciss +1
        pervChose = "Scissors"
        sciss = sciss +1
    num = num +1

print(f"\nCompleted Iterating random {num}, and counting repetetion")
print(f"Rock repeted: {rock} times")
print(f"Paper repeted: {paper} times")
print(f"Scissors repeted: {sciss} times")


num = 0
rock =0
paper = 0
sciss = 0
pervChose = None
maxRockRepeted = 0
maxPaperRepeted = 0
maxScissorRepeted = 0
maxCounter = 0
totalRepete = 0

print(f"\nIterating random for {maxNum}, and counting maximum repeted selection")
while num < maxNum:
    chose = random.choice(game)
    if pervChose == chose:
        maxCounter = maxCounter +1
        totalRepete = totalRepete +1
    else:
        if pervChose == "Rock":
            if maxCounter > maxRockRepeted:
                maxRockRepeted = maxCounter
        elif pervChose == "Paper":
            if maxCounter > maxPaperRepeted:
                maxPaperRepeted = maxCounter
        else:
            if maxCounter > maxScissorRepeted:
                maxScissorRepeted = maxCounter
        maxCounter =0
        pervChose = chose
    num = num +1

print(f"\nCompleted Iterating random {num}, and counting maximum repeted selection")
print(f"Total Repeted occurence: {totalRepete} Times")
print(f"Rock Maximum repeted equence: {maxRockRepeted} times")
print(f"Paper Maximum repeted equence: {maxPaperRepeted} times")
print(f"Scissors Maximum repeted equence: {maxScissorRepeted} times")