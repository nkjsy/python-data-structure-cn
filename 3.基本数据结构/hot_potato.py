# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 11:17:36 2019

@author: Administrator
"""

class Que():
    def __init__(self):
        self.q = []
        
    def __init__(self, l):
        self.q = []
        for i in l:
            self.enque(i)
    
    def enque(self, item):
        self.q.insert(0, item)
        
    def deque(self):
        return self.q.pop()
    
    def size(self):
        return len(self.q)
    
    def isEmpty(self):
        return self.q == []
    
def hot(name, n):
    q = Que(name)
    while q.size() > 1:
        for c in range(n):
            q.enque(q.deque())
        q.deque()
    return q.deque()

if __name__ == '__main__':
    print(hot(["Bill","David","Susan","Jane","Kent","Brad"],7))