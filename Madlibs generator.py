x = """This is the text you are given to fill out:
      
Once upon a time there was a ___ who was friends with a ___. Both lived near the ___. One day, he challenged the ___ to a ___ race. Seeing how slow the ___ was going, the ___ thought he'll win this easily. So he decided to ___ for some time while the ___ kept on going. He saw ___ dream of eating ___. When the ___ woke up, he saw that the ___ was already at the finish line. Much to his ___, the ___ won the race while he was busy ___.
      
    Fill the blanks with words of your choice (not numbers). Have fun!
    """

print(x)

blanks = []

for i in range(16):
    blank = str(input(f"What would you like to write for blank {i + 1}?: "))
    blanks.append(blank)
    
#Checks if the lengths of all the values of blank in the list "blanks" is greater than 0
if all(len(blank) > 0 for blank in blanks):
    print(f"Once upon a time there was a {blanks[0]} who was friends with a {blanks[1]}. Both lived near the {blanks[2]}. One day, he challenged the {blanks[3]} to a {blanks[4]} race. Seeing how slow the {blanks[5]} was going, the {blanks[6]} thought he'll win this easily. So he decided to {blanks[7]} for some time while the {blanks[8]} kept on going. He saw {blanks[9]} dream of eating {blanks[10]}. When the {blanks[11]} woke up, he saw that the {blanks[12]} was already at the finish line. Much to his {blanks[13]}, the {blanks[14]} won the race while he was busy {blanks[15]}.")     
else:
    print("You did not fill in all of the blanks. Try again.")