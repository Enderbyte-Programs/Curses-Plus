from cursesplus import *
from cursesplus import filedialog

def __test__(stdscr):
    import random
    curses.curs_set(0)
    load_colours(False)
    #displayops(stdscr,[str(random.randint(1,1000)) for _ in range(1000)],"Hi every body")
    #rlist = [str(random.randint(1,999999)) for _ in range(random.randint(100,10000))]
    #p = ProgressBar(stdscr,len(rlist),1,True,True,"Example Progress Bar",True)
    #for i in rlist:
        #p.step(str(i),True)
        #p.appendlog(str(i),curses.color_pair(random.randint(1,12)))
    #p.done()
    #del p
    #displaymsg(stdscr,[filedialog.openfiledialog(stdscr,filter=[["*.py","Python File"],["*","All Files"]])])
    displaymsg(stdscr,str(cursesinput(stdscr,"HI").endswith(" ")))
    displaymsg(stdscr,filedialog.openfilesdialog(stdscr,filter=[["*.py","Python File"],["*","All Files"]]))

if __name__ == "__main__":
    #Testing things
    curses.wrapper(__test__)