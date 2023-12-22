# sys.argv 
import sys

arguments = sys.argv
arguments_amount = len(arguments)

if arguments_amount <= 1:
    print("You have not passed any arguments")
else:
    print(f"You have passed {arguments_amount-1} arguments: {arguments[1:]}")