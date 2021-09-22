import sys


def check_sign(sign):
    return sign not in "+-"


# check whether the user input is empty
def check_expression_empty(expression):
    if not expression:
        return [False, None]
    else:
        # create boolean for the loop
        true_mb_false = False
        expression = list(expression)
        indicator = 0
        return ebnf(expression, indicator, true_mb_false)


# create function which determines whether the input expression is the correct entry

def ebnf(argument, ind, boolean):
    # write the length of the expression to the variable expression_size

    # if the function has completely passed our list of
    # digits and signs and all satisfies return True and calculated expression
    # if no number or sign is found, return (False, None)
    # use boolean to check if there are + or - go one after another
    if ind == len(argument) - 1 and argument[ind].isdigit():
        return [True, eval("".join(argument))]
    elif ind == len(argument) - 1 and not check_sign(argument[ind]):
        return [False, None]
    else:

        if check_sign(argument[ind]) and not argument[ind].isdigit():
            return [False, None]
        if not check_sign(argument[ind]):
            if boolean:
                return [False, None]
            boolean = True
        else:
            boolean = False
        return ebnf(argument, ind + 1, boolean)

    # cut first element(name of the file) and join it in one expression


print(check_expression_empty("".join(sys.argv[1:])))
