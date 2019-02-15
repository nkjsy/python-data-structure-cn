# -*- coding: utf-8 -*-

import sys
sys.path.append(r"H:\python-data-structure-cn\3.基本数据结构")
from hot_potato import Que

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connect_to = {}
        self.color = 'white'
        self.distance = 0
        self.pred = None
        self.found = 0
        self.finish = 0
        
    def get_id(self):
        return self.id
        
    def get_weight(self, to):
        return self.connect_to.get(to, None)
    
    def get_connect(self):
        return self.connect_to.keys()
    
    def add_connect(self, to, weight = 0):
        self.connect_to[to] = weight
        
    def __str__(self):
        return str(self.id) + 'connected to:' + str([x.id for x in self.get_connect()])
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
        
    def get_distance(self):
        return self.distance
    
    def set_distance(self, distance):
        self.distance = distance
        
    def get_pred(self):
        return self.pred
    
    def set_pred(self, pred):
        self.pred = pred
        
    def get_found(self):
        return self.found
    
    def set_found(self, found):
        self.found = found
        
    def get_finish(self):
        return self.finish
    
    def set_finish(self, finish):
        self.finish = finish
    
    
class Graph:
    def __init__(self):
        self.vertex_list = {}
        self.num_vertex = 0
        
    def get_vertex(self, key):
        return self.vertex_list.get(key)
    
    def get_vertexs(self):
        return self.vertex_list.keys()
    
    def __contains__(self, key):
        return key in self.vertex_list.keys()
        
    def add_vertex(self, key):
        self.num_vertex += 1
        v = Vertex(key)
        self.vertex_list[key] = v
        return v
        
    def add_edge(self, f, t, weight=0):
        fv = self.get_vertex(f)
        if not fv:
            fv = self.add_vertex(f)
        tv = self.get_vertex(t)
        if not tv:
            tv = self.add_vertex(t)
        fv.add_connect(tv, weight)
        
    def __iter__(self):
        return iter(self.vertex_list.values())
    
def build_graph(word_file):
    g = Graph()
    buckets = {}
    fr = open(word_file, 'r')
    # put all words into buckets
    for word in fr.readlines():
        word = word[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in buckets:
                buckets[bucket].append(word)
            else:
                buckets[bucket] = [word]
    fr.close()
    # all words in the same bucket have edges
    for bucket in buckets:
        words = buckets[bucket]
        for w1 in words:
            for w2 in words:
                if w1 != w2:
                    g.add_edge(w1, w2)
    return g

def bfs(start):
    start.set_color('gray')
    q = Que([])
    q.enque(start)
    while not q.isEmpty():
        current = q.deque()
        for v in current.get_connect():
            if v.get_color() == 'white':
                v.set_color('gray')
                v.set_distance(current.get_distance()+1)
                v.set_pred(current)
                q.enque(v)
        current.set_color('black')
            
def traverse(y):
    while y:
        print (y.get_id())
        y = y.get_pred()
    
if __name__ == '__main__':
    '''
    g = Graph()
    for i in range(6):
        g.add_vertex(i)
    g.add_edge(0,1,5)
    g.add_edge(0,5,2)
    g.add_edge(1,2,4)
    g.add_edge(2,3,9)
    g.add_edge(3,4,7)
    g.add_edge(3,5,3)
    g.add_edge(4,0,1)
    g.add_edge(5,4,8)
    g.add_edge(5,2,1)
    for v in g:
        for w in v.get_connect():
            print("( %s , %s )" % (v.get_id(), w.get_id()))
    '''

    g = build_graph('./fourletterwords.txt')
    start = g.get_vertex('FOOL')
    to = g.get_vertex('SAGE')
    bfs(start)
    traverse(to)