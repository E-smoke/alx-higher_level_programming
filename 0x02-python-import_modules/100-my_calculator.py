#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] == "+":
        r = calculator_1.add(int(sys.argv[1]), int(sys.argv[3]))
        print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], r))
    elif sys.argv[2] == "-":
        r = calculator_1.sub(int(sys.argv[1]), int(sys.argv[3]))
        print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], r))
    elif sys.argv[2] == "*":
        r = calculator_1.mul(int(sys.argv[1]), int(sys.argv[3]))
        print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], r))
    elif sys.argv[2] == "/":
        r = calculator_1.div(int(sys.argv[1]), int(sys.argv[3]))
        print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], r))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
