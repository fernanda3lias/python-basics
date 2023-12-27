# argparse.ArgumentParser for more complex arguments
# Official Tutorial:
# https://docs.python.org/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='display Hello World on screen',
    # type=str, # Argument type
    metavar='STRING',
    # default='Hello World', # Default value
    required=False,
    # nargs='+', # More than a value
    action='append'# More than an argument

)
args = parser.parse_args()


if args.basic is None:
    print("You didn't pass b value")
    print(args.basic)

else:
    print(args.basic)