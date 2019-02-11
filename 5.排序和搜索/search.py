# -*- coding: utf-8 -*-

def binary_search(l, n):
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = (left + right) // 2
        if l[mid] == n:
            return mid
        else:
            if l[mid] < n:
                left = mid + 1
            else:
                right = mid - 1
    return None
    
class HashTable: # reimplement the dictionary
    def __init__(self):
        self.size = 11
        self.bins = [None] * self.size
        self.values = [None] * self.size
        
    def hash_func(self, key):
        return key % self.size
    
    def rehash(self, oldh):
        return (oldh + 1) % self.size
        
    def put(self, key, value):
        position = self.hash_func(key)
        if self.bins[position] == None:
            self.bins[position] = key
            self.values[position] = value
            return
        else:
            while self.bins[position] != None:
                if self.bins[position] == key:
                    self.values[position] = value
                    return
                else:
                    position = self.rehash(position)
            self.bins[position] = key
            self.values[position] = value
            return
        
    def get(self, key):
        position = self.hash_func(key)
        start = position
        if self.bins[position] == None:
            return None
        else:
            if self.bins[position] == key:
                return self.values[position]
            else:
                position = self.rehash(position)
                while self.bins[position] != None and position != start:
                    if self.bins[position] == key:
                        return self.values[position]
                    else:
                        position = self.rehash(position)
                return None
            
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, value):
        self.put(key, value)
    
if __name__ == '__main__':
    #print (binary_search([0, 1, 2, 8, 13, 17, 19, 32, 42], 0))
    H=HashTable()
    H[54]="cat"
    H[26]="dog"
    H[93]="lion"
    H[17]="tiger"
    H[77]="bird"
    H[31]="cow"
    H[44]="goat"
    H[55]="pig"
    H[20]="chicken"
    print (H.bins)
    print (H.values)
    print (H[20])
    H[20]='duck'
    print (H[20])