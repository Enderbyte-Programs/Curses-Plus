import cursesplus
import curses
import random
    
if __name__ == "__main__":
    win = cursesplus.show_ui()
    
    cursesplus.classic.optionmenu(win.screen,["hello","goodbyte"])
    cursesplus.shutdown_ui()