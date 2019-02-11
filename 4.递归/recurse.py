# -*- coding: utf-8 -*-

def to_str(n, base):
    digits = '0123456789ABCDEF'
    if n < base:
        return digits[n]
    else:
        return to_str(n//base, base) + digits[n%base]
    
        
def move_disk(a, b):
    print (f'move one disk from {a} to {b}')
    
def move_tower(h, a, b, c):
    if h >= 1:
        move_tower(h-1, a, c, b)
        move_disk(a, b)
        move_tower(h-1, c, b, a)
  
coin_list = [1, 5, 10, 25]   
known = {}   
for c in coin_list:
    known[c] = 1
def min_coin(change):
    if change in known.keys():
        return known[change]
    mini = change
    for c in [c for c in coin_list if c < change]:
        rest = change - c
        n = min_coin(rest) + 1
        if n < mini:
            mini = n
    known[change] = mini
    return mini
    
    
if __name__ == '__main__':
    #print (to_str(10, 2))
    #move_tower(10, 'from_pole', 'to_pole', 'with_pole')
    print (min_coin(100))