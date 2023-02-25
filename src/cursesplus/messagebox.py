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
                stdscr.addstr(by,bx," ")
        rectangle(stdscr,y//2-(len(message)//2)-1, x//2-(maxs//2)-1, y//2+(len(message)//2)+4, x//2+(maxs//2+1)+1)
        mi = -(len(message)/2)
        
        for msgl in message:
            mi += 1
            stdscr.addstr(int(y//2+mi),int(x//2-len(msgl)//2),msgl)
        stdscr.addstr(y//2+(len(message)//2)+3,x//2-(maxs//2),"[Yes]",[curses.color_pair(9) if selected else curses.color_pair(6)][0])
        stdscr.addstr(y//2+(len(message)//2)+3,x//2-(maxs//2)+10,"[No]",[curses.color_pair(6) if selected else curses.color_pair(9)][0])
        stdscr.refresh()
        ch = stdscr.getch()
        if ch == curses.KEY_RIGHT or ch == curses.KEY_LEFT:
            selected = not selected
        elif ch == 121 or ch == 110:
            return ch == 121
        elif ch == 10 or ch == 13 or ch == curses.KEY_ENTER:
            return selected
