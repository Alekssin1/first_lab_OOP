import sys
#cut first element(name of the file)
argument = sys.argv[1:]
#there we pick our operation(1 input) from command line
arithmetic_operations = argument[0]
#here we take all the numbers on which the operation will be performed
expression = argument[1:]
#create a dict to make add, sub, multi and div keys to a sign
arithmetic = {"add": "+",
              "sub": "-",
              "multi": "*",
              "div": "/"}
#We use join to make our expression a string with
# spaces and then using the function eval
print(eval(arithmetic[arithmetic_operations].join(argument[1:])))