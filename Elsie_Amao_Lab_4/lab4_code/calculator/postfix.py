from array_stack import ArrayStack


def evaluate_postfix(postfix_str):
    '''
    Return the result of evaluating a postfix
    expression given in a string: postfix_str.

    Assumptions:
        * Input string is properly formatted
        * No spaces
        * Single digit operands (values)
        * Operators: + - * /
    '''
    # Traverse postfix_str left-to-right, character-by-character, pushing
    # arguments onto an argument stack until you encounter an operator.
    # When you find an operator, pop its operands off the stack, perform
    # the operation, and push the result back on the stack (it may be
    # an operand for another operation). When you are done, the result
    # of the expression will be on the top of the stack.
    #
    # Tip: Converting a str to an int:  x = int('3')
    return 0
