import sys
from ultrasplit import split_by_symbol

from ultrasplit import split_by_symbol


# check whether the user input is empty
def check_string_empty(string):
    if not string:
        print("You need to enter an expression")
    else:
        # We use join to make our expression a string with
        # spaces and then using the function eval
        try:
            print(eval(string))
        except ZeroDivisionError:
            print("Attempt to divide a number by zero")
        except NameError:
            print("Incorrect input! Name error, try again")
        except SyntaxError:
            print("Invalid syntax. Try again.")
        except EOFError or KeyboardInterrupt:
            print("Error, incorrect input! Try again.")


# cut first element(name of the file)
expression = "".join(sys.argv[1:])
check_string_empty(expression)
