import cursesplus
import curses
import random
    
if __name__ == "__main__":
    win = cursesplus.show_ui()
    cursesplus.classic.displayops(win.screen,["Hlel","Goodbye"])
    cursesplus.shutdown_ui()