import curses
from finch import Finch
f = Finch()

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

direction = 0

key = ''
while key != ord('q'):
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    stdscr.refresh()
    if key == curses.KEY_UP: 
        direction = min(direction+1, 1)
        stdscr.addstr(2, 20, "Up")
        f.wheels(direction,direction)
    elif key == curses.KEY_DOWN: 
        direction = max(direction-1,-1)
        stdscr.addstr(3, 20, "Down")
        f.wheels(direction,direction)
