# -*- coding: utf-8 -*-

from stack import Stack

def in_to_post(expr):
    tokens = expr.split()
    post = []
    s = Stack()
    
    prec = {}
    prec['('] = 1
    prec['+'] = 2
    prec['-'] = 2
    prec['*'] = 3
    prec['/'] = 3
    
    for token in tokens:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            post.append(token)
        elif token == '(':
            s.push(token)
        elif token == ')':
            top = s.pop()
            while top != '(':
                post.append(top)
                top = s.pop()
        elif token in '+-*/':
            while not s.is_empty() and prec[s.peek()] >= prec[token]:
                post.append(s.pop())
            s.push(token)
        else:
            raise RuntimeError('invalid expression!')
    
    while not s.is_empty():
        post.append(s.pop())
    return ' '.join(post)

def post_eval(expr):
    s = Stack()
    tokens = expr.split()
    for token in tokens:
        if token in '0123456789':
            s.push(int(token))
        else:
            b = s.pop()
            a = s.pop()
            s.push(calculate(token, a, b))
    return s.pop()

def calculate(token, a, b):
    if token == '+':
        return a + b
    elif token == '-':
        return a - b
    elif token == '*':
        return a * b
    else:
        return a / b
    
if __name__ == '__main__':
    print(in_to_post("( A + B ) * ( C + D )"))
    print(in_to_post("( A + B ) * C"))
    print(in_to_post("A + B * C"))
    print(in_to_post("A * B + C * D"))
    print(in_to_post("( A + B ) * C - ( D - E ) * ( F + G )"))
    print(post_eval('7 8 + 3 1 + /'))