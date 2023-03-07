from . import cp
import os
from curses.textpad import rectangle
import curses

def askyesno(stdscr,message: list = []) -> bool:
    selected = True
    x,y = os.get_terminal_size()
    ox = 0
    for o in message:
        ox += 1
        if "\n" in o:
            message.insert(ox,o.split("\n")[1])
    message = [m[0:x-5].split("\n")[0] for m in message[0:y-5]]#Limiting characters
    maxs = max([len(s) for s in message])
    while True:
        for by in range(y//2-(len(message)//2)-1,y//2+(len(message)//2)+4):
            for bx in range(x//2-(maxs//2)-1,x//2+(maxs//2+1)+1):
                stdscr.addstr(by,bx," ",curses.color_pair(12))
        rectangle(stdscr,y//2-(len(message)//2)-1, x//2-(maxs//2)-1, y//2+(len(message)//2)+4, x//2+(maxs//2+1)+1)
        stdscr.addstr(y//2+(len(message)//2)+4,x//2-(maxs//2),"Y: Yes | N: No")
        mi = -(len(message)/2)
        stdscr.addstr(y//2+(len(message)//2)+3,x//2-(maxs//2),"[Yes]",[curses.color_pair(9) if selected else curses.color_pair(6)][0])
        stdscr.addstr(y//2+(len(message)//2)+3,x//2-(maxs//2)+10,"[No]",[curses.color_pair(6) if selected else curses.color_pair(9)][0])   
        for msgl in message:
            mi += 1
            stdscr.addstr(int(y//2+mi),int(x//2-len(msgl)//2),msgl,curses.color_pair(12))
    
        stdscr.refresh()
        
        ch = stdscr.getch()
        if ch == curses.KEY_RIGHT or ch == curses.KEY_LEFT:
            selected = not selected
        elif ch == 121 or ch == 110:
            return ch == 121
        elif ch == 10 or ch == 13 or ch == curses.KEY_ENTER:
            return selected

def showinfo(stdscr,message: list = [],title:str="Info") -> None:
    selected = True
    x,y = os.get_terminal_size()
    ox = 0
    for o in message:
        ox += 1
        if "\n" in o:
            message.insert(ox,o.split("\n")[1])
    message = [m[0:x-5].split("\n")[0] for m in message[0:y-5]]#Limiting characters
    maxs = max([len(s) for s in message])
    while True:
        for by in range(y//2-(len(message)//2)-1,y//2+(len(message)//2)+4):
            for bx in range(x//2-(maxs//2)-1,x//2+(maxs//2+1)+1):
                stdscr.addstr(by,bx," ",curses.color_pair(10))
        rectangle(stdscr,y//2-(len(message)//2)-1, x//2-(maxs//2)-1, y//2+(len(message)//2)+4, x//2+(maxs//2+1)+1)
        stdscr.addstr(y//2-(len(message)//2)-1, x//2-(maxs//2)-1,title)
        mi = -(len(message)/2)
        stdscr.addstr(y//2+(len(message)//2)+3,x//2-(maxs//2),"[OK]",curses.color_pair(9)) 
        for msgl in message:
            mi += 1
            stdscr.addstr(int(y//2+mi),int(x//2-len(msgl)//2),msgl,curses.color_pair(10))
    
        stdscr.refresh()
        
        ch = stdscr.getch()
        if ch == 10 or ch == 13 or ch == curses.KEY_ENTER:
            return

def showwarning(stdscr,message: list = [],title:str="Warning") -> None:
    selected = True
    x,y = os.get_terminal_size()
    ox = 0
    for o in message:
        ox += 1
        if "\n" in o:
            message.insert(ox,o.split("\n")[1])
    message = [m[0:x-5].split("\n")[0] for m in message[0:y-5]]#Limiting characters
    maxs = max([len(s) for s in message])
    while True:
        for by in range(y//2-(len(message)//2)-1,y//2+(len(message)//2)+4):
            for bx in range(x//2-(maxs//2)-1,x//2+(maxs//2+1)+1):
                stdscr.addstr(by,bx," ",curses.color_pair(13))
        rectangle(stdscr,y//2-(len(message)//2)-1, x//2-(maxs//2)-1, y//2+(len(message)//2)+4, x//2+(maxs//2+1)+1)
        stdscr.addstr(y//2-(len(message)//2)-1, x//2-(maxs//2)-1,title)
        mi = -(len(message)/2)
        stdscr.addstr(y//2+(len(message)//2)+3,x//2-(maxs//2),"[OK]",curses.color_pair(9)) 
        for msgl in message:
            mi += 1
            stdscr.addstr(int(y//2+mi),int(x//2-len(msgl)//2),msgl,curses.color_pair(13))
    
        stdscr.refresh()
        
        ch = stdscr.getch()
        if ch == 10 or ch == 13 or ch == curses.KEY_ENTER:
            return

def showerror(stdscr,message: list = [],title:str="Warning") -> None:
    selected = True
    x,y = os.get_terminal_size()
    ox = 0
    for o in message:
        ox += 1
        if "\n" in o:
            message.insert(ox,o.split("\n")[1])
    message = [m[0:x-5].split("\n")[0] for m in message[0:y-5]]#Limiting characters
    maxs = max([len(s) for s in message])
    while True:
        for by in range(y//2-(len(message)//2)-1,y//2+(len(message)//2)+4):
            for bx in range(x//2-(maxs//2)-1,x//2+(maxs//2+1)+1):
                stdscr.addstr(by,bx," ",curses.color_pair(11))
        rectangle(stdscr,y//2-(len(message)//2)-1, x//2-(maxs//2)-1, y//2+(len(message)//2)+4, x//2+(maxs//2+1)+1)
        stdscr.addstr(y//2-(len(message)//2)-1, x//2-(maxs//2)-1,title)
        mi = -(len(message)/2)
        stdscr.addstr(y//2+(len(message)//2)+3,x//2-(maxs//2),"[OK]",curses.color_pair(9)) 
        for msgl in message:
            mi += 1
            stdscr.addstr(int(y//2+mi),int(x//2-len(msgl)//2),msgl,curses.color_pair(11))
    
        stdscr.refresh()
        
        ch = stdscr.getch()
        if ch == 10 or ch == 13 or ch == curses.KEY_ENTER:
            return