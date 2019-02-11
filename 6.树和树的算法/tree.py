# -*- coding: utf-8 -*-

class BinaryTree:
    def __init__(self, obj):
        self.root = obj
        self.left = None
        self.right = None
        
    def insert_left(self, t):
        if self.left == None:
            self.left = BinaryTree(t)
        else:
            l = BinaryTree(t)
            l.left = self.left
            self.left = l
            
    def insert_right(self, t):
        if self.right == None:
            self.right = BinaryTree(t)
        else:
            r = BinaryTree(t)
            r.right = self.right
            self.right = r
            
    def get_root(self):
        return self.root
    
    def set_root(self, obj):
        self.root = obj
        
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
class BinaryHeap:
    def __init__(self):
        self.size = 0
        self.heap = [0]
    
    def up(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i//2]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2
            
    def insert(self, n):
        self.size += 1
        self.heap.append(n)
        self.up(self.size)
        
    def min_child(self, i):
        if i*2+1 > self.size:
            return i*2
        else:
            if self.heap[i*2] > self.heap[i*2+1]:
                return i*2+1
            else:
                return i*2
    
    def down(self, i):
        while i*2 <= self.size:
            mc = self.min_child(i)
            if self.heap[i] > self.heap[mc]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc
            
    def del_min(self):
        m = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.down(1)
        return m

    def build(self, l):
        self.heap = [0] + l[:]
        self.size = len(l)
        for i in range(len(l)//2, 0, -1):
            self.down(i)

class BinarySearchTree:
    def __init__(self):
        self.size = 0
        self.root = None
        
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()
    
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = Node(key, val)
        self.size += 1
        
    def _put(self, key, val, current):
        if key > current.key:
            if current.has_right():
                self._put(key, val, current.right)
            else:
                current.right = Node(key, val, parent=current)
        else:
            if current.has_left():
                self._put(key, val, current.left)
            else:
                current.left = Node(key, val, parent=current)
                
    def __setitem__(self, k, v):
        self.put(k, v)
        
    def get(self, key):
        r = self._get(key, self.root)
        if r:
            return r.val
        else:
            return None
        
    def _get(self, key, current):
        if current == None:
            return None
        elif key == current.key:
            return current
        elif key > current.key:
            return self._get(key, current.right)
        else:
            return self._get(key, current.left)
        
    def __getitem__(self, k):
        return self.get(k)
    
    def __contains__(self, k):
        if self.get(k):
            return True
        else:
            return False
        
    
class Node:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        
    def has_left(self):
        return self.left
    
    def has_right(self):
        return self.right
    
    def is_left(self):
        return self.parent and self.parent.left is self
    
    def is_right(self):
        return self.parent and self.parent.right is self
    
    def is_root(self):
        return not self.parent
    
    def is_leaf(self):
        return not (self.left or self.right)
    
    def has_any_children(self):
        return self.left or self.right
    
    def has_both_children(self):
        return self.left and self.right
    
    def replace_node(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self
            

if __name__ == '__main__':
    '''
    r = BinaryTree('a')
    print(r.get_root())
    print(r.get_left())
    r.insert_left('b')
    print(r.get_left())
    print(r.get_left().get_root())
    r.insert_right('c')
    print(r.get_right())
    print(r.get_right().get_root())
    r.get_right().set_root('hello')
    print(r.get_right().get_root())

    bh = BinaryHeap()
    bh.build([9,5,6,2,3])
    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())
    '''
    mytree = BinarySearchTree()
    mytree[3]="red"
    mytree[4]="blue"
    mytree[6]="yellow"
    mytree[2]="at"
    
    print(mytree[6])
    print(mytree[1])