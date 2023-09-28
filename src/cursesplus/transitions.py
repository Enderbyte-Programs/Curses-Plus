import os
import random
from time import sleep

def _old(stdscr,func_to_call=None,args=(),type=0):
    """
    Generate a fancy transition with curses. Type 0 is a wipe transition with lines. Type 1 is a more powerful random block pixel transition.
    Calls func_to_call(args) after transition is finishd
    """
    block = "█"
    mx,my = os.get_terminal_size()
    if type == 0:
        
        for y in range(my-1):
            stdscr.addstr(y,0,block*(mx-1))
            stdscr.refresh()
            sleep(0.01)
        for y in range(my-1):
            stdscr.addstr(y,0," "*(mx-1))
            stdscr.refresh()
            sleep(0.01)
    elif type == 1:
        _grid = [(x,y) for y in range(my-1) for x in range(mx-1)]
        while _grid:
            for i in range(round(((my*mx)/(24*80))*20)):# Fixing slow transitions on HD screens
                try:
                    pk = random.choice(_grid)
                    _grid.pop(_grid.index(pk))
                    stdscr.addstr(pk[1],pk[0],block)
                    stdscr.refresh()
                except:
                    break
            sleep(0.01)
        _grid = [(x,y) for y in range(my-1) for x in range(mx-1)]
        while _grid:
            for i in range(round(((my*mx)/(24*80))*20)):
                try:
                    pk = random.choice(_grid)
                    _grid.pop(_grid.index(pk))
                    stdscr.addstr(pk[1],pk[0]," ")
                    stdscr.refresh()
                except:
                    break
            sleep(0.01)
    if func_to_call is not None:
        func_to_call(*args)

### NEW CODE START HERE

block = "█"

def __exec(func,args):
    func(*args)

def horizontal_bars(stdscr,func_to_call=None,args=(),speed=1):
    mx,my = os.get_terminal_size()
    for y in range(my-1):
        stdscr.addstr(y,0,block*(mx-1))
        stdscr.refresh()
        sleep(0.01/speed)
    for y in range(my-1):
        stdscr.addstr(y,0," "*(mx-1))
        stdscr.refresh()
        sleep(0.01/speed)
    if func_to_call is not None:
        __exec(func_to_call,args)

def random_blocks(stdscr,func_to_call=None,args=(),speed=1):
    mx,my = os.get_terminal_size()
    
    _grid = [(x,y) for y in range(my-1) for x in range(mx-1)]
    while _grid:
        for i in range(round(((my*mx)/(24*80))*20)):# Fixing slow transitions on HD screens
            try:
                pk = random.choice(_grid)
                _grid.pop(_grid.index(pk))
                stdscr.addstr(pk[1],pk[0],block)
                stdscr.refresh()
            except:
                break
        sleep(0.01)
    _grid = [(x,y) for y in range(my-1) for x in range(mx-1)]
    while _grid:
        for i in range(round(((my*mx)/(24*80))*20)):
            try:
                pk = random.choice(_grid)
                _grid.pop(_grid.index(pk))
                stdscr.addstr(pk[1],pk[0]," ")
                stdscr.refresh()
            except:
                break
        sleep(0.01)
    if func_to_call is not None:
        __exec(func_to_call,args)

def vertical_bars(stdscr,func_to_call=None,args=(),speed=1):
    mx,my = os.get_terminal_size()
    for y in range(mx-1):
        for x in range(my-1):
            stdscr.addstr(x,y,block)
        stdscr.refresh()
        sleep(0.01/speed)
    for y in range(mx-1):
        for x in range(my-1):
            stdscr.addstr(x,y," ")
        stdscr.refresh()
        sleep(0.01/speed)
    if func_to_call is not None:
        __exec(func_to_call,args)