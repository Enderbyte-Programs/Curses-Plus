# Curses Plus
Extension library to curses

## How To Install
Use ```pip3 install cursesplus```
on Linux or ```py -m pip install cursesplus```
on Windows

### SPECIAL INSTRUCTIONS FOR WINDOWS

For Windows you need to also install ```windows-curses``` or related program
to provide the basic curses functionality

# What's New?

## 3.16.1

- Remove the last bit of *american* spelling.

- Add fix to an uncontrollable crash on Windows

- Add home and end to coloured option menu

## NOTICE! 3.x - Incompatible API changes

As you may have noticed, the major version number has now jumped to 3. You may be wondering why it is 3.15 instead of 3.0. Well, an alpha I was working on got to 3.14, so I bumped it to 3.15 to prevent versioning issues.

**The following changes likely require changes in your code**

- Move colours to a new module called constants. Because this is auto-imported, this should not pose an issue

- Move filline, showcursor, and hidecursor to a new module called utils.

- Fix spelling issue, utils.filline is now utils.fill_line

- Change displayops to optionmenu. Please refactor all calls from displayops() to optionmenu(): No other changes are required

- Remove legacy function `showerror`. Use messagebox.showerror as a replacement

- Remove legacy function `askyesno_old`. Use messagebox.askyesno as a replacement

- Combine `displaymsg` and `displaymsgnodelay` into one function

- Existing `displaymsgnodelay` calls can be changed to `displaymsg(stdscr,[messages],False)`, so change the flag wait_for_keypress to false

- Remove redundant american function `set_color`. You can either use the (correct) spelling `set_colour` or you can not use this library.


# Documentation

## transitions.py

transitions contains many transitions to add animations to your program

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

## utils.py

Utils.py Contain a series of non-ui utility functions. By non-ui I mean that it does not show a screen and it is non-interactive. It is meant to enhance the creation of custom menus.

### fill_line(stdscr,line,colour)

This function fills row `line` with the colour `colour`.

- `stdscr` is a curses window object

- `line` is an int. It is the row number you wish to fill in

- `colour` is a curses colour. Use `cursesplus.set_colour()` for this

### hidecursor()

This function hides the console cursor

### showcursor()

This function shows the console cursor

## constants.py

constants.py contains a series of constants such as colours and special lines.