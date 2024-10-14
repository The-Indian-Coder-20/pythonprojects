import random

maxCount = 10
score1, score2 = 0, 0
i = 1
die1, die2 = 0, 0
while i <= maxCount:
    die1, die2 = random.randint(1,6), random.randint(1,6)

    score1 += die1
    score2 += die2
    
    if die1 == 6 and die2 == 6:
        die1, die2 = random.randint(1,6), random.randint(1,6)
        score1 += die1
        score2 += die2
    elif die2 == 6:
        die2 = random.randint(1,6)
        score2 += die2
    elif die1 == 6:
        die1 = random.randint(1,6)
        score1 += die1
    i += 1
if score1 > score2:
    print(f"Player one won with a total score of {score1}!")
elif score1 == score2:
    print(f"Both players got the same score of {score1}!")
else:
    print(f"Player two won with a total score of {score2}!")