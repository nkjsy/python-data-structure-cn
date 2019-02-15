# -*- coding: utf-8 -*-

from graph import Graph

class DFSGraph(Graph):
    def __init__(self):
        super.__init__()
        self.time = 0
        
    def dfs(self):
        for v in self:
            v.set_color('white')
            v.set_pred(-1)
        for v in self:
            if v.get_color() == 'white':
                self.dfs_visit(v)
            
    def dfs_visit(self, start):
        start.set_color('gray')
        self.time += 1
        start.set_found(self.time)
        for v in start.get_connect():
            if v.get_color() == 'white':
                v.set_pred(start)
                dfs_visit(v)
        start.set_color('black')
        self.time += 1
        start.set_finish(self.time)
    
if __name__ == '__main__':
