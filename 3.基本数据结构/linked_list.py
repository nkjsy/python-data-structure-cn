# -*- coding: utf-8 -*-

class Node:
    def __init__(self, item):
        self.value = item
        self.next = None
        
    def get_value(self):
        return self.value
    def set_value(self, item):
        self.value = item
    def get_next(self):
        return self.next
    def set_next(self, next_node):
        self.next = next_node
        
        
class UnorderedList:
    def __init__(self):
        self.head = None
        
    def add(self, node):
        node.set_next(self.head)
        self.head = node
        
    def is_empty(self):
        return self.head == None
    
    def size(self):
        count = 0
        current = self.head
        while current != None:
            current = current.get_next()
            count += 1
        return count
    
    def search(self, value):
        found = False
        current = self.head
        while current != None and not found:
            if current.get_value() == value:
                found = True
            else:
                current = current.get_next()
        return found
    
    def remove(self, value):
        found = False
        current = self.head
        previous = None
        while current != None and not found:
            if current.get_value() == value:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            

class OrderedList:
    def __init__(self):
        self.head = None
        
    def add(self, value):
        stop = False
        current = self.head
        previous = None
        while current != None and not stop:
            if current.get_value() > value:
                stop = True
            else:
                previous = current
                current = current.get_next()
        temp = Node(value)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
        
    def is_empty(self):
        return self.head == None
    
    def size(self):
        count = 0
        current = self.head
        while current != None:
            current = current.get_next()
            count += 1
        return count
    
    def search(self, value):
        found = False
        current = self.head
        while current != None and not found:
            if current.get_value() == value:
                found = True
            else:
                if current.get_value() > value:
                    return False
                else:
                    current = current.get_next()
        return found
    
    def remove(self, value):
        found = False
        current = self.head
        previous = None
        while current != None and not found:
            if current.get_value() == value:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())