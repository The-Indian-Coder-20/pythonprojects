import time
print("Starting Capital Guessing Game...")
time.sleep(3)
print("You have three lifelines. If you lose all three lives, you lose. Good luck!")
time.sleep(3)

points = 0
lives = 3
countries = {"Japan": ["Tokyo"], "India": ["New Dehli", "new dehli", "dehli", "Dehli"], "France": ["Paris"], "Italy": ["Rome"], "United States of America": ["Washington D.C.", "washington d.c.", "washington D.C.", "D.C."]}

for country,capitals in countries.items():
    x = str(input(f"What is the capital of {country}?: "))
    if x in capitals:
        print("You are correct!")
        points += 1
    else:
        print("You are wrong!")
        lives -= 1
    if lives > 0 and countries:
        print("Game over, you won!")
        break
    elif lives == 0:
        print("You have lost all of your lives! You lost!")
        break
print(f"Your final score was {points}")