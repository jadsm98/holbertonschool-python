#!/usr/bin/python3
from sys import exit, argv
from calculator_1 import add, sub, mul, div


def main():
    pass
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print('1')
    elif argv[2] != '+' and argv[2] != '-' and argv[2] != '*' and argv[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        print('1')
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == '+':
        print('{} + {} = {}'.format(a, b, add(a, b)))
        print('0')
    elif argv[2] == '-':
        print('{} - {} = {}'.format(a, b, sub(a, b)))
        print('0')
    elif argv[2] == '*':
        print('{} * {} = {}'.format(a, b, mul(a, b)))
        print('0')
    elif argv[2] == '/':
        print('{} / {} = {}'.format(a, b, div(a, b)))
        print('0')
    main()
