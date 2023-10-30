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

## Patch 2.11.5

- Messagebox now has nicer titles

- coloured_option_menu is now more lax

## Version 2.11

- Add checkboxlist

- Choose one or more options from the list

- Add banned characters in cursesinput
.
- Fix blinking in textview

# Documentation

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