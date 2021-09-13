import sys
#cut first element(name of the file)
expression = sys.argv[1:]
#We use join to make our expression a string with
# spaces and then using the function eval
print(eval(" ".join(expression)))