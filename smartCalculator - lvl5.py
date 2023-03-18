class InvalidExpressionError(Exception):
    def __str__(self):
        return 'Invalid expression'


class UnknownCommandError(Exception):
    def __str__(self):
        return 'Unknown command'

# expr = list(input().replace(' ', ''))
expr = ' '
next = None


def takeInput():
    global expr

    expr = list(input().replace(' ', ''))

def checkError():
    global expr
    global next
    global joint

    try:
        if len(expr) > 0:
            if expr[-1] in ['+', '-']:
                next = True
                raise InvalidExpressionError
            elif ''.join(expr) not in ['/exit', '/help'] and ''.join(expr)[0] == '/':
                next = True
                raise UnknownCommandError
            elif ''.join(expr).isalpha():

                next = True
                raise InvalidExpressionError
            else:
                if ''.join(expr)[0] != '/':
                    for char in expr:
                        if char in 'abcdefghijklmnopqrstuvqxyz':
                            next = True
                            raise InvalidExpressionError

    except InvalidExpressionError as error:
        print(error)
    except UnknownCommandError as error:
        print(error)


def simplifier():
    global expr

    nums = '1234567890'
    for x in range(100):
        for index, char in enumerate(expr):
            if index != (len(expr) - 1):
                if char == '-' and expr[index + 1] == '-':
                    del expr[index:(index + 2)]
                    expr.insert(index, '+')
                elif (char == '-' and expr[index + 1] == '+') or (char == '+' and expr[index + 1] == '-'):
                    del expr[index: (index + 2)]
                    expr.insert(index, '-')
                elif char == '+' and expr[index + 1] == '+':
                    del expr[index: (index + 2)]
                    expr.insert(index, '+')
                elif char in nums and expr[index + 1] in nums:
                    newNum = char + expr[index + 1]
                    del expr[index: (index + 2)]
                    expr.insert(index, newNum)


def addition(a, b):
    return str(a + b)


def subtraction(a, b):
    return str(a - b)


def solver():
    global expr

    if expr[0] == '-' and expr[1].isnumeric():
        newInt = expr[0] + expr[1]
        del expr[0: 2]
        expr.insert(0, newInt)
    elif expr[0] == '+':
        del expr[0]

    for x in range(50):
        for index, char in enumerate(expr):
            if index != (len(expr) - 1) and (char.isnumeric() or len(char) > 1):
                if expr[index + 1] == '+':
                    result = addition(int(char), int(expr[index + 2]))
                    # print(sum)
                    del expr[index: (index + 3)]
                    expr.insert(index, result)
                    break

                elif expr[index + 1] == '-':
                    result = subtraction(int(char), int(expr[index + 2]))
                    del expr[index: (index + 3)]
                    expr.insert(index, result)
                    break


while True:
    takeInput()
    checkError()
    if not next:
        if ''.join(expr) not in ['/exit', '/help'] and len(expr) > 0:
            simplifier()
            solver()
            print(''.join(expr))
        elif ''.join(expr) == '/help':
            print('This is calculator!')
        elif len(expr) == 0:
            continue
        else:
            print('Bye!')
            exit()
    next = None

# checkError()
