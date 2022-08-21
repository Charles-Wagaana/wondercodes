from ast import operator


value1 = int(input("Value1: "))
value2 = int(input("Value2: "))
operators = input("Operator: ")

if operators == "+":
    print(value1 + value2)
if operators == "-":
    print(value1 - value2)
if operators == "*":
    print(value1 * value2)
if operators == "/":
    print(value1/value2)

