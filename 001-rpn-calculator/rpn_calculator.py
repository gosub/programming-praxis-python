# RPN Calculator
# Evaluate numeric expressions at the command line
# Programming Praxis Exercise 1
# http://programmingpraxis.com/2009/02/19/rpn-calculator/


operators = { '+': lambda x,y: x+y,
              '-': lambda x,y: x-y,
              '*': lambda x,y: x*y,
              '/': lambda x,y: x/y }


def rpn_calc_eval(expression, stack):
    tokens = expression.strip(" \n\r\t").split(" ")
    for t in tokens:
        if t in operators:
            x = stack.pop()
            y = stack.pop()
            result = operators[t](y,x)
            stack.append(result)
        else:
            try:
                x = int(t)
                stack.append(x)
            except ValueError:
                try:
                    x = float(t)
                    stack.append(x)
                except ValueError:
                    pass
    return stack


def rpn_calc_repl():
    stack = []
    while True:
        expression = raw_input("rpn> ")
        if expression == 'q':
            break
        elif expression == 'c':
            stack = []
        elif expression == 'p':
            print stack
        else:
            stack = rpn_calc_eval(expression, stack)
            print stack[-1]


if __name__ == '__main__':
    print "RPN Calculator"
    print "special commands: [p]rint the stack, [c]lear the stack, [q]uit"
    print
    rpn_calc_repl()
