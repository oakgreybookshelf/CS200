from array_stack import ArrayStack

def infix_to_postfix(infix_str):
    '''
    Return a string that contains the postfix representation of a
    given infix expression.

    Assumptions:
        * infix_str string contains
            * Input string is properly formatted
            * no spaces
            * signle digit operands
            * operators: + - * /
            * parentheses: ( )
        * return string contains
            * no spaces
            * Single digit operands (values)
            * Operators: + - * /
    '''
    postfix = ''
    S = ArrayStack()
    for c in infix_str:
        if c not in '+-*/()':
            postfix += c
        elif S.is_empty():
            S.push(c)
        elif c == '(':
            S.push(c)
        elif c == ')':
            while S.top() != '(':
                postfix += S.pop()
            assert S.pop() == '('
        elif S.top() == '(':
            S.push(c)
        elif precedence(c) > precedence(S.top()):
            S.push(c)
        else:
            while S and S.top() != '(' and precedence(c) <= precedence(S.top()):
                postfix += S.pop()
            S.push(c)
    while S:
        postfix += S.pop()
    return postfix


def precedence(c):
    '''
    Return an integer value that represents the precedence of an
    operator given as a single character string. The higher the
    integer value, the higher the operator's precedence. A higher
    precendence operator evaluates before a lower precenedence
    operator.
    '''
    if c in '+-':
        return 1
    elif c in '*/':
        return 2
