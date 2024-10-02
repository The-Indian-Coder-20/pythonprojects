operator = input("""What operator would you like to use? 
                 
    Choose one out of the four.
        + (addition)
        - (subtraction)
        * (multiplication)
        / (division) 
        
        """)
value = ""
#Gives a alphabetical value instead of only symbols
while True:
    if operator == "+":
        value = "addition"
        print(f"The chosen operator for this process is {value} ({operator})")
        break
    elif operator == "-":
        value = "subtraction"
        print(f"The chosen operator for this process is {value} ({operator})")
        break
    elif operator == "*":
        value = "multiplication"
        print(f"The chosen operator for this process is {value} ({operator})")
        break
    elif operator == "/":
        value = "division"
        print(f"The chosen operator for this process is {value} ({operator})")
        break
    else:
        print(f"{operator} is now a valid operator.")
        exit()
#Prints alphabetical value as well as the symbol operator.
#Asks user for numbers to use.
num1 = float(input("What is the first number you would like to use?: "))
num2 = float(input("What is the second number you would like to use?: "))
#Prints the chosen numbers and the process that will be performed.
print(f"The chosen numbers are {num1} and {num2}.")
print("{} {} {}".format(num1, operator, num2))
#What to do for certain operators.
if operator == "+":
    x = float(num1 + num2)
    y = round(x, 3)
    print(y)
elif operator == "-":
    x = float(num1 - num2)
    y = round(x, 3)
    print(y)
elif operator == "*":
    x = float(num1 * num2)
    y = round(x, 3)
    print(y)
elif operator == "/":
    x = float(num1 / num2)
    y = round(x, 3)
    print(y)