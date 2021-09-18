import sys


def check_sign(char):
    if (char == "+" or char == "-" or char == "*" or char == "/") != 1:
        return True
    else:
        False


# check whether the user input is empty
def check_string_empty(string):
    if not string:
        return [False, None]
    else:
        # create boolean for the loop
        true_mb_false = False
        string = list(string)
        indicator = 0
        return ebnf(string, indicator, true_mb_false)


# create function which determines whether the input string is the correct entry

def ebnf(argument, ind, boolean):
    # write the length of the string to the variable expression_size

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


# cut first element(name of the file) and join it in one string
print(check_string_empty("".join(sys.argv[1:])))


