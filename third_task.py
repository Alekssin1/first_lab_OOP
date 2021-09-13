import sys
from ultrasplit import split_by_symbol

# cut first element(name of the file) and join it in one string
expression = "".join(i for i in sys.argv[1:])
# create boolean for the loop
boolean = False


# create function which determines whether the input string is the correct entry

def ebnf(argument, i, boolean):
    # write the length of the string to the variable expression_size

    expression_size = len(argument)
    # if the function has compeletely passed our list of
    # digits and signs and all satisfies return True and calculated expression
    # if no number or sign is found, return (False, None)
    # use boolean to check if there are + or - go one after another
    if i == expression_size - 1:
        return (True, eval("".join(expression)))
    else:
        if not (argument[i] == "+" or argument[i] == "-") != 1 and (argument[i].isdigit()):
            return (False, None)
        if (argument[i] == "+" or argument[i] == "-") == 1:
            if boolean:
                return (False, None)
            boolean = True
        else:
            boolean = False
        return ebnf(argument, i + 1, boolean)


expression = split_by_symbol(expression)
i = 0
print(ebnf(expression, i, boolean))
