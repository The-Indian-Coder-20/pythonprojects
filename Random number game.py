import time
import random

print("Random number game starting...")
time.sleep(3)
print("""Welcome to the random number game!
      
In this game you will try to guess a number that I, the computer will think of! This number will be between 1 and 100.
      
You will have a limited number of chances, so be careful!
      """)
time.sleep(3)

Number_life = 5
lives = print("You have {} lives.".format(Number_life))
num = random.randrange(0, 101)

while Number_life > 0:
    x = int(input("What number do you think it is?: "))
    print(x)
    if x > num:
        print("You guessed too high!")
        Number_life -= 1
    elif x < num:
        print("You guessed too low!")
        Number_life -= 1
    elif x == num:
        print("You got it correct!")
        print("You won the game!")
        break
    if Number_life == 0:
        print("You ran out of chances. You lose!")