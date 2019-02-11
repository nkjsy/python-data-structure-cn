# -*- coding: utf-8 -*-

from stack import Stack
from tree import BinaryTree

def build_parser(math_exp):
    l = math_exp.split()
    s = Stack()
    current = BinaryTree('')
    s.push(current)
    for i in l:
        if i == '(':
            current.insert_left('')
            s.push(current)
            current = current.get_left()
        elif i.isdigit():
            current.set_root(int(i))
            current = s.pop()
        elif i in '+-*/':
            current.set_root(i)
            current.insert_right('')
            s.push(current)
            current = current.get_right()
        elif i == ')':
            current = s.pop()
        else:
            raise ValueError('invalid character in the math expression!')
    return current

def eval_parser(t):
    left = t.get_left()
    right = t.get_right()
    v = t.get_root()
    if left != None and right != None:
        if v == '+':
            return eval_parser(left) + eval_parser(right)
        elif v == '-':
            return eval_parser(left) - eval_parser(right)
        elif v == '*':
            return eval_parser(left) * eval_parser(right)
        else:
            return eval_parser(left) / eval_parser(right)
    else:
        return v
    
def print_exp(t): # inorder
    s = ''
    if t:
        if str(t.get_root()) in '+-*/':
            s += '('
            s += print_exp(t.get_left())
            s += str(t.get_root())
            s += print_exp(t.get_right())
            s += ')'
        else:
            s += str(t.get_root())
    return s
        
    
if __name__ == '__main__':
    pt = build_parser("( ( 10 - 5 ) * ( ( 3 + 2 ) / 5 ) )")
    print (eval_parser(pt))
    print (print_exp(pt))