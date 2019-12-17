def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def calculator():
    while True:
        inp = input("Enter the equation: ")
        x, op, y = inp.split(' ')
        if op == '+':
            result = add(int(x), int(y))
        elif op == '-':
            result = subtract(int(x), int(y))
        elif op == 'x':
            result = multiply(int(x), int(y))
        else:
            result = "I don't know what to do"
        print(inp, "=", result)


if __name__ == '__main__':
    calculator()
