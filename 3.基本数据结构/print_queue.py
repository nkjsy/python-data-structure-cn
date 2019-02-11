# -*- coding: utf-8 -*-

# ppm: how many pages the printer can print in every minute
# period: total simulation time
# interval=180: on average, after how many seconds will a task come 
# max_pages=20: every task will include 1-20 pages

from hot_potato import Que
import random

class Printer():
    def __init__(self, ppm):
        self.ppm = ppm
        self.current_task = None
        self.task_time = 0
        
    def busy(self):
        return True if self.current_task != None else False
    
    def start_new(self, new_task):
        self.current_task = new_task
        self.task_time = new_task.get_pages() * 60 / self.ppm
        
    def countdown(self):
        if self.current_task != None:
            self.task_time -= 1
            if self.task_time <= 0:
                self.current_task = None
                self.task_time = 0
            

class Task():
    def __init__(self, start):
        self.pages = random.randrange(1,21)
        self.start = start
        
    def get_pages(self):
        return self.pages
    
    def wait_time(self, finish):
        return finish - self.start
    
def task_come():
    r = random.randrange(1, 181)
    if r == 180:
        return True
    else:
        return False
    
def simulation(period):
    wait_time_list = []
    printer = Printer(5)
    q = Que([])
    
    for t in range(period):
        if task_come():
            new_wait_task = Task(t)
            q.enque(new_wait_task)
        
        if (not printer.busy()) and (not q.isEmpty()):
            new_task = q.deque()
            printer.start_new(new_task)
            wait = new_task.wait_time(t)
            wait_time_list.append(wait)
            
        printer.countdown()
        
    return sum(wait_time_list) / len(wait_time_list)

if __name__ == '__main__':
    round = 100
    l = []
    for i in range(round):
        t = simulation(3600)
        #print ('average wait time per task:', t)
        l.append(t)
    print (f'average wait time after {round} rounds experiment:', sum(l)/round)