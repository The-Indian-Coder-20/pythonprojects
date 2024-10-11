import random

playAgain = "yes"

while playAgain.lower() == "yes" or playAgain.lower() == "y":
    num1, num2, num3, num4 = random.randint(1,5), random.randint(1,5), random.randint(1,5), random.randint(1,5)
    while num1 == num2 or num1 == num3 or num1 == num4 or num2 == num3 or num3 == num4 or num3 == num4:
        num1, num2, num3, num4 = random.randint(1,5), random.randint(1,5), random.randint(1,5), random.randint(1,5)
    numList = [num1, num2, num3, num4]
    emptyNumList = ["a", "b", "c", "d"]
    print("Please guess the numbers and place of the 4 digit number")
    num = int(input("What number would you like to guess?: "))
    place = input("What position would you like to put the number in?: ")
    while "a" in emptyNumList or "b" in emptyNumList or "c" in emptyNumList or "d" in emptyNumList:
        if num in numList:
            if str(place) in emptyNumList:
                if numList.index(num) == emptyNumList.index(place):
                    print("You got a position and number correct!")
                    emptyNumList[numList.index(num)] = num
                    print(emptyNumList)
                else:
                    print("You got the number correct, but not the position!")
                    place = input("What position would you like to put the number in?: ")
                    while emptyNumList.index(place) != numList.index(num):
                        place = input("What position would you like to put the number in?: ")
                    print("You got a position and number correct!")
                    emptyNumList[numList.index(num)] = num
                    print(emptyNumList)
        else:
            print("You didn't guess anything correct :(")
            num = int(input("What number would you like to guess?: "))
            place = input("What position would you like to put the number in?: ")
        if "a" in emptyNumList or "b" in emptyNumList or "c" in emptyNumList or "d" in emptyNumList:
            num = int(input("What number would you like to guess?: "))
            place = input("What position would you like to put the number in?: ")
        else:
            break
    print("Congratulations! You guessed all of the numbers!")
    playAgain = input("Would you like to play again?: ")
print("See you next time!")