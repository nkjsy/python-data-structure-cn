# -*- coding: utf-8 -*-

from graph import Graph, Vertex
    
def knight_graph(bdsize):
    g = Graph()
    for row in range(bdsize):
        for col in range(bdsize):
            from_id = coord_to_id(row, col, bdsize)
            to_ids = move_list(row, col, bdsize)
            for to_id in to_ids:
                g.add_edge(from_id, to_id)
    return g

def coord_to_id(row, col, bdsize):
    return row * bdsize + col

def move_list(row, col, bdsize):
    all_moves = [(1,2), (2,1), (1,-2), (-2,1), (-1,2), (2,-1), (-1,-2), (-2,-1)]
    to_list = []
    for m in all_moves:
        to_row = row + m[0]
        to_col = col + m[1]
        if to_row>=0 and to_row<bdsize and to_col>=0 and to_col<bdsize:
            to_id = coord_to_id(to_row, to_col, bdsize)
            to_list.append(to_id)
    return to_list

# DFS
def knight_tour(depth, path, current, limit):
    current.set_color('gray')
    path.append(current)
    if depth<limit:
        #to_list = current.get_connect()
        to_list = order_by_next(current)
        done = False
        for t in to_list:
            if t.get_color() == 'white':
                done = knight_tour(depth+1, path, t, limit)
                if done:
                    break
        if not done: # backtrack
            path.pop()
            current.set_color('white')
    else:
        done = True
    return done

# order the to_list to speed up dfs
def order_by_next(n):
    l = []
    to_list = n.get_connect()
    for t in to_list:
        if t.get_color() == 'white':
            c = 0
            for tt in t.get_connect():
                if tt.get_color() == 'white':
                    c += 1
            l.append((c, t))
    l.sort(key=lambda x: x[0])
    return [x[1] for x in l]
    
if __name__ == '__main__':
    g = knight_graph(40)
    start = g.get_vertex(0)
    path = []
    done = knight_tour(0, path, start, 1599)
    print (done)
    for v in path:
        print (v.get_id())