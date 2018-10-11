#Implement a direct infix evaluator that combine the functionality of infix_to_postfix conversion
#and the postfix evaluation algorithm

import module_stack as st

def infix_eval(infix_expr):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    operator_stack = st.Stack()
    operand_stack = st.Stack()

    token_list = infix_expr.split()

    for token in token_list:
        
        if token in '0123456789':
            operand_stack.push(int(token))
        
        elif token == ')':
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            op = operator_stack.pop()
            result = do_math(op, operand1, operand2)
            operand_stack.push(result)

        elif token in '+-*/':
            operator_stack.push(token)

    while operand_stack.size() >= 2:
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        op = operator_stack.pop()
        result = do_math(op, operand1, operand2)
        operand_stack.push(result)
        
    
    return operand_stack.pop()       
      
        
def do_math(op,op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '-':
        return op1 - op2 
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2       


print(infix_eval('( 5 - 2 ) / ( 3 + 0 )'))    
