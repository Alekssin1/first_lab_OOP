import sys

# cut first element(name of the file)
expression = "".join(sys.argv[1:])

# We use join to make our expression a string with
# spaces and then using the function eval
# check whether the user input is empty
if expression:
    try:
        print(eval(expression))
    except ZeroDivisionError:
        print("Attempt to divide a number by zero")
    except NameError:
        print("Incorrect input! Name error, try again")
    except SyntaxError:
        print("Invalid syntax. Try again.")
    except EOFError or KeyboardInterrupt:
        print("Error, incorrect input! Try again.")
else:
    print("You need to enter an expression")
