import curses

def main(stdscr):
	while True:
		s = stdscr.getch()
		stdscr.addstr(curses.keyname(s))
curses.wrapper(main)
