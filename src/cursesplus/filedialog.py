from .cp import *
import glob

def parse_size(data: int) -> str:
    result = "???"
    if data < 0:
        neg = True
        data = -data
    else:
        neg = False
    if data < 2000:
        result = f"{data} bytes"
    elif data > 2000000000:
        result = f"{round(data/1000000000,2)} GB"
    elif data > 2000000:
        result = f"{round(data/1000000,2)} MB"
    elif data > 2000:
        result = f"{round(data/1000,2)} KB"
    if neg:
        result = "-"+result
    return result

class Fileobj:
    def __init__(self,path: str) -> None:
        if not os.path.isfile(path) and not os.path.isdir(path):
            raise FileNotFoundError(f"No file found {path}")
        self.path = path
        if os.path.isfile(path):
            self.isdir = False
        elif os.path.isdir(path):
            self.isdir = True
        self.size = os.path.getsize(path)
        self.datestamp = os.path.getctime(path)
        self.date = str(datetime.fromtimestamp(self.datestamp))[0:-7]
        self.sizestr = parse_size(self.size)
        self.strippedpath = path.replace("\\","/").split("/")[-1]  

def openfiledialog(stdscr,title: str = "Please choose a file",filter: str = [["*","All Files"]],directory: str = os.getcwd()) -> str:
    xoffset: int = 0
    yoffset: int = 0
    activefilter: int = 0
    selected: int = 0
    while True:
        masterlist: list = list[Fileobj]
        mx,my = os.get_terminal_size()
        MAXNL = mx - 33
        stdscr.clear()
        rectangle(stdscr,2,0,my-2,mx-1)
        filline(stdscr,0,10)
        filline(stdscr,1,12)
        filline(stdscr,my-2,9)
        filline(stdscr,my-1,11)
        topline = "Name"+" "*(MAXNL-4)+"|"+"Size     "+"|Date Modified"
        topline = topline+(mx-2-len(topline))*" "
        directories = [directory+"/"+l for l in os.listdir(directory) if os.path.isdir(directory+"/"+l)]
        if filter[activefilter][0] == "*":
            files = [directory+"/"+l for l in os.listdir(directory) if os.path.isfile(directory+"/"+l)]
        else:
            files = glob.glob(directory+"/"+filter[activefilter][0])
        directories.sort()
        files.sort()
        #displaymsg(stdscr,directories+files)
        masterlist = [Fileobj(f) for f in (directories+files)[yoffset:yoffset+my]]
        stdscr.addstr(0,0,title+"|H for Help|Press Shift-Left Arrow to move up directory"[0:mx],curses.color_pair(10))
        stdscr.addstr(1,0,directory[xoffset:xoffset+mx],curses.color_pair(12))
        stdscr.addstr(my-2,0,f"{filter[activefilter][1]} ({filter[activefilter][0]}) [{len(masterlist)} objects found]"[0:mx],curses.color_pair(9))
        stdscr.addstr(2,1,topline[0:mx-1])
        
        try:
            stdscr.addstr(my-1,0,masterlist[selected].path[xoffset:xoffset+mx],curses.color_pair(11))
        except:
            pass
        ind = yoffset#Track position in list
        indx = 0#track position in iter
        for fileobjects in masterlist[yoffset:yoffset+my-5]:
            wstr = fileobjects.strippedpath[xoffset:xoffset+MAXNL]
            wstr += " "*(MAXNL-len(wstr)+1)
            wstr += fileobjects.sizestr
            wstr += " "*(10-len(fileobjects.sizestr))
            wstr += fileobjects.date
            if selected == ind:
                stdscr.addstr(3+indx,1,wstr,curses.color_pair(5))
            elif fileobjects.isdir:
                stdscr.addstr(3+indx,1,wstr,curses.color_pair(2))
            else:
                stdscr.addstr(3+indx,1,wstr)
            ind += 1
            indx += 1#Inc both

        
        stdscr.refresh()
        ch = stdscr.getch()

        if ch == curses.KEY_LEFT and xoffset > 0:
            xoffset -= 1
        elif ch == curses.KEY_RIGHT:
            xoffset += 1
        elif ch == curses.KEY_UP and selected > 0:
            selected -= 1
            if selected < yoffset:
                yoffset -= 1
        elif ch == curses.KEY_DOWN and selected < len(masterlist)-1:
            if selected - yoffset > my - 7:
                yoffset += 1
            selected += 1
        elif ch == 102:
            activefilter = displayops(stdscr,[f"{f[1]} ({f[0]})" for f in filter],"Please choose a filter")
            selected = 0
            yoffset = 0
        elif ch == curses.KEY_ENTER or ch == 10 or ch == 13:
            if masterlist[selected].isdir:
                directory = masterlist[selected].path
                selected = 0
                yoffset = 0
            else:
                return masterlist[selected].path
        elif ch == curses.KEY_SLEFT:
            directory = "/".join(directory.split("/")[0:-1])
            selected = 0
            yoffset = 0
            if directory == "":
                directory = "/"
        elif ch == 104:
            displaymsg(stdscr,["List of Keybinds","Down Arrow: Scroll down","Up Arrow: Scroll up","Left Arrow: Scroll left","Right Arrow: Scroll right","Shift-left arrow: Move up to parent Directory","Enter: Open/select","F: Change filter"])

        masterlist.clear()

def openfilesdialog(stdscr,title: str = "Please choose a file",filter: str = [["*","All Files"]],directory: str = os.getcwd()) -> list:
    xoffset: int = 0
    yoffset: int = 0
    activefilter: int = 0
    selected: int = 0
    chosen: list[str] = []
    chosen.append(" ")
    chosen.clear()
    while True:
        masterlist: list = list[Fileobj]
        mx,my = os.get_terminal_size()
        MAXNL = mx - 33
        stdscr.clear()
        rectangle(stdscr,2,0,my-2,mx-1)
        filline(stdscr,0,10)
        filline(stdscr,1,12)
        filline(stdscr,my-2,9)
        filline(stdscr,my-1,11)
        topline = "Name"+" "*(MAXNL-4)+"|"+"Size     "+"|Date Modified"
        topline = topline+(mx-2-len(topline))*" "
        directories = [directory+"/"+l for l in os.listdir(directory) if os.path.isdir(directory+"/"+l)]
        if filter[activefilter][0] == "*":
            files = [directory+"/"+l for l in os.listdir(directory) if os.path.isfile(directory+"/"+l)]
        else:
            files = glob.glob(directory+"/"+filter[activefilter][0])
        directories.sort()
        files.sort()
        #displaymsg(stdscr,directories+files)
        masterlist = [Fileobj(f) for f in (directories+files)[yoffset:yoffset+my]]
        stdscr.addstr(0,0,title+"|H for Help|Press Shift-Left Arrow to move up directory"[0:mx],curses.color_pair(10))
        stdscr.addstr(1,0,directory[xoffset:xoffset+mx],curses.color_pair(12))
        stdscr.addstr(my-2,0,f"{filter[activefilter][1]} ({filter[activefilter][0]}) [{len(masterlist)} objects found]"[0:mx],curses.color_pair(9))
        stdscr.addstr(2,1,topline[0:mx-1])
        
        try:
            stdscr.addstr(my-1,0,str(chosen)[xoffset:xoffset+mx],curses.color_pair(11))
        except:
            pass
        ind = yoffset#Track position in list
        indx = 0#track position in iter
        for fileobjects in masterlist[yoffset:yoffset+my-5]:
            wstr = fileobjects.strippedpath[xoffset:xoffset+MAXNL]
            wstr += " "*(MAXNL-len(wstr)+1)
            wstr += fileobjects.sizestr
            wstr += " "*(10-len(fileobjects.sizestr))
            wstr += fileobjects.date
            if selected == ind:
                stdscr.addstr(3+indx,1,wstr,curses.color_pair(5))
            elif fileobjects.isdir:
                stdscr.addstr(3+indx,1,wstr,curses.color_pair(2))
            elif fileobjects.path in chosen:
                stdscr.addstr(3+indx,1,wstr,curses.color_pair(4))
            else:
                stdscr.addstr(3+indx,1,wstr)
            ind += 1
            indx += 1#Inc both

        
        stdscr.refresh()
        ch = stdscr.getch()

        if ch == curses.KEY_LEFT and xoffset > 0:
            xoffset -= 1
        elif ch == curses.KEY_RIGHT:
            xoffset += 1
        elif ch == curses.KEY_UP and selected > 0:
            selected -= 1
            if selected < yoffset:
                yoffset -= 1
        elif ch == curses.KEY_DOWN and selected < len(masterlist)-1:
            if selected - yoffset > my - 7:
                yoffset += 1
            selected += 1
        elif ch == 102:
            activefilter = displayops(stdscr,[f"{f[1]} ({f[0]})" for f in filter],"Please choose a filter")
            selected = 0
            yoffset = 0
        elif ch == curses.KEY_ENTER or ch == 10 or ch == 13:
            if masterlist[selected].isdir:
                directory = masterlist[selected].path
                selected = 0
                yoffset = 0
            else:
                chosen.clear()
                chosen.append(masterlist[selected].path)
        elif ch == 115:
            #s for add to selection
            if not masterlist[selected].isdir:
                if masterlist[selected].path in chosen:
                    chosen.remove(masterlist[selected].path)
                else:
                    chosen.append(masterlist[selected].path)
        elif ch == curses.KEY_SLEFT:
            directory = "/".join(directory.split("/")[0:-1])
            selected = 0
            yoffset = 0
            if directory == "":
                directory = "/"
        elif ch == 100 or curses.keyname(ch).decode() == "^X":
            return [c for c in chosen if os.path.isfile(c) and c.replace(" ","") != ""]#Only return files that still exist
        elif ch == 99:
            chosen.clear()
        elif ch == 104:
            displaymsg(stdscr,["List of Keybinds","Down Arrow: Scroll down","Up Arrow: Scroll up","Left Arrow: Scroll left","Right Arrow: Scroll right","Shift-left arrow: Move up to parent Directory","Enter: Open/select","F: Change filter","S: Append / Remove from selection","D/Ctrl-X: Done","C: Clear selection"])

        masterlist.clear()