# -*- coding: utf-8 -*-

class Stack:
    def __init__(self):
        self.s = []
        
    def is_empty(self):
        return self.s == []
    
    def push(self, item):
        self.s.append(item)
        
    def pop(self):
        return self.s.pop()
    
    def peek(self):
        return self.s[-1]
    
    def size(self):
        return len(self.s)
    
def par_pair(str):
    s = Stack()
    for char in str:
        if char in '([{':
            s.push(char)
        elif char in ')]}':
            if s.is_empty():
                return False
            p = s.pop()
            if not match(p, char):
                return False
    return s.is_empty()

def match(left, right):
    l = '([{'
    r = ')]}'
    return l.index(left) == r.index(right)

def base_converter(n, base):
    digits = '0123456789ABCDEF'
    s = Stack()
    while n > 0:
        remain = n % base
        s.push(remain)
        n = n // base
    out = ''
    while not s.is_empty():
        out = out + digits[s.pop()]
    return out
    
if __name__ == '__main__':
    '''
    print(par_pair('((()))'))
    print(par_pair('(()))'))
    print(par_pair('{{([][])}()}'))
    print(par_pair('[{()]'))
    print(par_pair('{{s(a[ddddddd]g[fff])ef}gawee()}geag'))
    '''
    print(base_converter(25,2))
    print(base_converter(15,16))