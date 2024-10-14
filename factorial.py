
for i in range(1,11):
    print(i)
for i in range(3, 24, 3):
    print(i)
for x in "Shrish Prasad Panda":
    print(x)
for x in range(1, 21):
    if x % 2 == 0:
        print(x)

number = int(input("What number would you like to find the factorial of? (Maximum integer number must be less than 1559): "))
factorial = 1
for i in range(1, number + 1):
    if number == 0:
        print("Factorial of 0 is 1")
    elif number > 0:
        factorial *= i
    else:
        print("This number's factorial is not defined.")
print("The factorial of", number, "is", factorial)