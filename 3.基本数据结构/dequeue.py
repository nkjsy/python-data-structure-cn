# -*- coding: utf-8 -*-

class Dequeue():
    def __init__(self):
        self.q = []
    
    def add_rear(self, item):
        self.q.insert(0, item)
        
    def add_front(self, item):
        self.q.append(item)
        
    def remove_rear(self):
        return self.q.pop(0)
        
    def remove_front(self):
        return self.q.pop()
    
    def size(self):
        return len(self.q)
    
    def isEmpty(self):
        return self.q == []
    
def is_pal(s):
    q = Dequeue()
    for char in s:
        q.add_front(char)
    
    while q.size() > 1:
        front = q.remove_front()
        rear = q.remove_rear()
        if front != rear:
            return False
        
    return True

if __name__ == '__main__':
    print(is_pal("lsdkjfskf"))
    print(is_pal("radar"))