import time
import random
import math

time.sleep(3)
print("Starting Dice Roll Game...")
time.sleep(1)
print(" ")
time.sleep(1)
print("Welcome to the Dice Roll Game! In this game, you will go against a friend and try to get the highest score from rolling dice. Have fun!")

def check_name(x, y):
    x = input(str("What is Player one name?: "))
    y = input(str("What is Player two name?: "))
    while len(x) == 0:
        print("Please enter a name.")
        return x
    while len(y) == 0:
        print("Please enter a name.")
        return y
    
check_name()