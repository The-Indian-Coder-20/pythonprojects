import time
import random
import math

time.sleep(3)
print("Starting Dice Roll Game...")
time.sleep(1)
print(" ")
time.sleep(1)
print("Welcome to the Dice Roll Game! In this game, you will go against a friend and try to get the highest score from rolling dice. Have fun!")

player1score = 0
player2score = 0

x = input(str("What is Player one name?: "))
y = input(str("What is Player two name?: "))
while len(x) == 0:
    print("Please enter a name.")
    x = input(str("What is Player one name?: "))
while len(y) == 0:
    print("Please enter a name.")
    y = input(str("What is Player two name?: "))

die1 = random.randint(1,6)
die2 = random.randint(1,6)
die3 = random.randint(1,6)
die1GuessP1 = int(input("""What do you think is the number on the first dice 1? (player 1): """))
die1GuessP2 = int(input("""What do you think is the number on the first dice 1? (player 2): """))
if die1GuessP1 == die1 and die1GuessP2 == die1:
    player1score += 1
    player2score += 1
elif die1GuessP1 == die1 and die1GuessP2 != die1:
    player1score += 1
elif die1GuessP1 != die1 and die1GuessP2 == die1:
    player2score += 1
else:
    print("No one guessed the number on the first dice 1")