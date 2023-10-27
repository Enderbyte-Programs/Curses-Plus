# Curses Plus
Extension library to curses

## How To Install
Use ```pip3 install cursesplus```
on Linux or ```py -m pip install cursesplus```
on Windows

### SPECIAL INSTRUCTIONS FOR WINDOWS

For Windows you need to also install ```windows-curses``` or related program
to provide the basic curses functionality

## What's New?

### THE SWITCH TO 3.0

cursesplus is getting a widgets based system. The old utilities have been moved to a classic class. filedialogues and message boxes remain. The program will likely be hard to use until everything is finalized.

**DANGER: THIS IS A TRULY BACKWARDS INCOMPATIBLE UPDATE. LOTS OF CODE WILL NEED TO BE REFACTORED!**

- Add TUI base module

- Add widgets module

- Move colours to constants module

- cursesplus.cp is now imported under cursesplus.classic

- There is now a default ctrl_C detector. 

### 3.2

- Add rectangle drawing for windows

- Remove ctrl c handler

- Move colours set to utils. For backwards compatibility, it is automatically imported to root level

- Utils.coord is now imported on root level

# Documentation

## Two Ways to Use

### 1. New Way

The new way is currently under construction, so expect some bugs. The New Way does not need any fooling around with bare curses. The new way is an abstration of curses, almost a "replacement" if you will. To start, do something like this. Only one function is required:

```
import cursesplus

win = cursesplus.show_ui()

#See below for how to use classic utilities in a 3.x environment
```

### 2. The Old Way

If you have been using cursesplus since before 3.0, you know what to do. You need to manually call initscr or wrapper and pass the stdscr to each function individually. For example
```
import cursesplus
import curses

def main(stdscr):
    cursesplus.classic.displaymsg(stdscr,["This is a message"])

curses.wrapper(main)
```

### 1A. Using classic utilities in a new set-up

To use Old-Style utility functions in a new way, see this code. This does the same as the example in part 2
```
import cursesplus

win = cursesplus.show_ui()
cursesplus.classic.displaymsg(win.screen,["This is a message"])

cursesplus.shutdown_ui() #Good practice to close down after
```

## transitions.py

transitions contains many transitions to add animations to your program

### _old(stdscr,func_to_call=None,args=(),type=0)

This is the old transitions function found in cursesplus prior to like 2.8 or something. It has since been replaced by horizontal_bars() and random_blocks()

- `stdscr` is a curses window object

- `func_to_call` is a function. If it is set to none, no function is called

- `args` is a tuple. The tuple will be passed to the function as arguments

- `type` is an int. It may be 0 or 1. If it is 0, there are horizontal bars. If it is 1, it is random blocks

### __exec(func,args)

**NOTE: THIS IS AN INTERNAL FUNCTION, IT IS NOT MEANT TO BE USED BY THE COMMON USER**

This executes `func(args)`

### horizontal_bars(stdscr,func_to_call=None,args=(),speed=1)

This is a replacement function to old's type zero. It fills the screen from the top down with horizontal white bars. It then replaces them with black bars in the same configuration.

- `stdscr` is a curses window object

- `func_to_call` is a function. If it is set to none, no function is called

- `args` is a tuple. The tuple will be passed to the function as arguments

- `speed` is an int. A higher value increases the animation speed. A lower value (0 - 1) makes it slower. If you set speed to 0, the program will crash.

### random_blocks(stdscr,func_to_call=None,args=(),speed=1)

This is a replacement for old's type one transition. It fills random characters of the screen with blocks until the whole screen is covered, then it removes it in the same fashion.

- `stdscr` is a curses window object

- `func_to_call` is a function. If it is set to none, no function is called

- `args` is a tuple. The tuple will be passed to the function as arguments

- `speed` is an int. A higher value increases the animation speed. A lower value (0 - 1) makes it slower. If you set speed to 0, the program will crash.

### vertical_bars(stdscr,func_to_call=None,args=(),speed=1)

This is an all new transition. It functions like horizontal bars except they are vertical and go left to right.

- `stdscr` is a curses window object

- `func_to_call` is a function. If it is set to none, no function is called

- `args` is a tuple. The tuple will be passed to the function as arguments

- `speed` is an int. A higher value increases the animation speed. A lower value (0 - 1) makes it slower. If you set speed to 0, the program will crash.