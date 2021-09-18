import sys

try:
    # cut first element(name of the file)
    # there we pick our operation(1 input) from command line
    arithmetic_operations = sys.argv[1]
    # here we take all the numbers on which the operation will be performed
    expression = sys.argv[2:]
    # create a dict to make add, sub, multi and div keys to a sign
    arithmetic = {"add": "+",
                  "sub": "-",
                  "multi": "*",
                  "div": "/"}
    # We use join to make our expression a string with
    # spaces and then using the function eval
    print(eval(arithmetic[arithmetic_operations].join(sys.argv[2:])))
except ZeroDivisionError:
    print("Attempt to divide a number by zero")
except IndexError:
    print("Incorrect input! Index error, try again")
except NameError:
    print("Incorrect input! Name error, try again")
except KeyError:
    print("Incorrect input! The first argument should be: add, div, multi or sub")
except SyntaxError:
    print("Invalid syntax!")
except EOFError or KeyboardInterrupt:
    print("Error, incorrect input! Try again.")

