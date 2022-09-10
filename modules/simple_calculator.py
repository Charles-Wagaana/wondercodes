import argparse


parser = argparse.ArgumentParser(description="This is a simple calculator")

parser.add_argument(
    'value1', type=int, 
    help='Enter first value.'
)
parser.add_argument(
    'value2', type=int,
    help='Enter second value.'
)
parser.add_argument(
    'Operator', type=str,
    help='Choose an operator',
    choices=['add', 'subtract', 'multiply', 'divide']
)

args = parser.parse_args()


if args.Operator == 'add':
    print(args.value1 + args.value2)

if args.Operator == 'subtract':
    print(args.value1 - args.value2)

if args.Operator == 'multiply':
    print(args.value1 * args.value2)

if args.Operator == 'divide':
    print(args.value1 // args.value2)

