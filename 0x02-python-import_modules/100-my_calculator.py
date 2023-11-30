#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    operators = {'+': add, '-': sub, '*': mul, '/': div}
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    elif argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]
        function = operators[operator]
        print("{} {} {} = {}".format(a, operator, b, function(a, b)))
