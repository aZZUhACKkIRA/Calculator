import utils as u

try:
    print("This program was made by Mohammed Azhaan Pasha")

    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number "))
    print("""
    Choose any operator from below.
    1 -- to add
    2 -- to subtract
    3 -- to multiply
    4 -- to divide
    5 -- to power
    0 -- to quit the program
    """)
    arithmetic = int(input())

    i = 5

    if arithmetic == 1:
        print(u.add(number1, number2))

    elif arithmetic == 2:
        print(u.minus(number1, number2))

    elif arithmetic == 3:
        print(u.multiply(number1, number2))

    elif arithmetic == 4:
        print(u.divide(number1, number2))

    elif arithmetic == 5:
        print(u.power(number1, number2))

    elif arithmetic == 0:
        exit()

    else:
        print("Sorry you entered an invalid input"
              "Run the program again")
    print("")
except ValueError:
    print('')
    print("Invalid Input")

print("Press 'Shift + F10' to run again")
print("This program was made by Mohammed Azhaan Pasha.")
