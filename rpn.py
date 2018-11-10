import operator
from termcolor import colored


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg):
    stack = list()
    base = 10
    for token in myarg.split():
        if token == 'bin':
            base = 2
        elif token == 'hex':
            base = 16
        elif token == 'c':
            stack.append(stack[-1])
        elif token == '!':
            count = stack.pop()
            result = 1
            while count > 0:
                result *= count
                count -= 1
            stack.append(result)
        else: 
            try:
                token = int(token, base)
                stack.append(token)
            except ValueError:
                function = operators[token]
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = function(arg1, arg2)
                stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    if base == 2:
        return bin(stack.pop())[2:]
    elif base == 16:
        return hex(stack.pop())[2:]
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        if result < 0:
            print("Result: ", colored(result, 'red'))
        elif result > 0:
            print("Result: ", colored(result, 'green'))
        else:
            print("Result: ", colored(result, 'yellow'))

if __name__ == '__main__':
    main()
