operator = input("""What operator would you like to use? 
                 
    Choose one out of the four.
        + (addition)
        - (subtraction)
        * (multiplication)
        / (division) 
        
        """)
#Gives a alphabetical value instead of only symbols
if operator == "+":
    value = "addition"
elif operator == "-":
    value = "subtraction"
elif operator == "*":
    value = "multiplication"
else:
    value = "division"
#Prints alphabetical value as well as the symbol operator.
print(f"The chosen operator for this process is {value} ({operator})")
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
else:
    x = float(num1 / num2)
    y = round(x, 3)
    print(y)