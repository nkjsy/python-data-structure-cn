# -*- coding: utf-8 -*-

# 1 bubble sort
def bubble_sort(l):
    for n in range(len(l)-1):
        for m in range(len(l)-1-n):
            if l[m] > l[m+1]:
                l[m], l[m+1] = l[m+1], l[m]
    return l

# 2 selection sort
def selection_sort(l):
    for n in range(len(l)-1, 0, -1):
        pos = 0
        for m in range(1, n+1):
            if l[m] > l[pos]:
                pos = m
        l[n], l[pos] = l[pos], l[n]
    return l
    
# 3 insertion sort
def insertion_sort(l):
    for n in range(1, len(l)):
        current = l[n]
        pos = n
        while pos > 0 and l[pos-1] > current:
            l[pos] = l[pos-1]
            pos -= 1
        l[pos] = current
    return l

# 4 shell sort
def gap_insertion_sort(l, start, gap):
    for n in range(start, len(l), gap):
        current = l[n]
        pos = n
        while pos >= start+gap and l[pos-gap] > current:
            l[pos] = l[pos-gap]
            pos -= gap
        l[pos] = current
        
def shell_sort(l):
    count = len(l) // 2
    while count >= 1:
        for i in range(count):
            gap_insertion_sort(l, i, count)
        print (f'After sorting with gap {count}:', l)
        count = count // 2

# 5 merge sort
def merge_sort(l):
    print ('Spliting list', l)
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                l[k] = right[j]
                k += 1
                j += 1
            else:
                l[k] = left[i]
                k += 1
                i += 1
        while i < len(left):
            l[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            l[k] = right[j]
            k += 1
            j += 1
    print ('Merged list', l)
    
# 6 quick sort
def quick_sort(l):
    quick_sort_help(l, 0, len(l)-1)
    
def quick_sort_help(l, first, last):
    if first < last:
        pivot = partition(l, first, last)
        quick_sort_help(l, first, pivot-1)
        quick_sort_help(l, pivot+1, last)
        
def partition(l, first, last):
    mid = l[first]
    left = first + 1
    right = last
    while True:
        while l[left] <= mid and left <= right:
            left += 1
        while l[right] >= mid and left <= right:
            right -= 1
        if left > right:
            l[first], l[right] = l[right], l[first]
            return right
        else:
            l[left], l[right] = l[right], l[left]

if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    print (f'Original list is: {alist}')
    quick_sort(alist)
    print (f'Sorted list is: {alist}')