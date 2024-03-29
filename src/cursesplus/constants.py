"""This module contains constants"""
import curses
#DEFINE SOME CONSTANTS
BLACK = curses.COLOR_BLACK
WHITE = curses.COLOR_WHITE
RED = curses.COLOR_RED
YELLOW = curses.COLOR_YELLOW
GREEN = curses.COLOR_GREEN
CYAN = curses.COLOR_CYAN
BLUE = curses.COLOR_BLUE
MAGENTA = curses.COLOR_MAGENTA

#Now for some box drawing characters
b = """─━│┃┄┅┆┇┈┉┊┋┌┍┎┏┐┑┒┓
└┕┖┗┘┙┚┛├┝┞┟┠┡┢┣┤┥┦┧┨┩┪
┫┬┭┮┯┰┱┲┳┴┵┶┷┸┹┺┻┼┽┾┿╀╁
╂╃╄╅╆╇╈╉╊╋╌╍╎╏═║╒╓╔╕╖╗╘
╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬╭╮╯
╰╱╲╳╴╵╶╷╸╹╺╻╼╽╾╿""".replace("\n","").replace("\r","")
THIN_HORIZ_LINE = b[0]
THICK_HORIZ_LINE = b[1]
THIN_VERT_LINE = b[2]
THICK_VERT_LINE = b[3]
THIN_3_DASHED_LINE_HORIZ = b[4]
THICK_3_DASHED_LINE_HORIZ = b[5]
THIN_3_DASHED_LINE_VERT = b[6]
THICK_3_DASHED_LINE_VERT = b[7]
THIN_4_DASHED_LINE_HORIZ = b[8]
THICK_4_DASHED_LINE_HORIZ = b[9]
THIN_4_DASHED_LINE_VERT = b[10]
THICK_4_DASHED_LINE_VERT = b[11]
TL_CORNER_THIN = b[12]
TL_CORNER_THIN_VERT = b[13]
TL_CORNER_THIN_HORIZ = b[14]
TL_CORNER_THICK = b[15]
TR_CORNER_THIN = b[16]
TR_CORNER_THIN_VERT = b[17]
TR_CORNER_THIN_HORIZ = b[18]
TR_CORNER_THICK = b[19]
BL_CORNER_THIN = b[20]
BL_CORNER_THIN_VERT = b[21]
BL_CORNER_THIN_HORIZ = b[22]
BL_CORNER_THICK = b[23]
BR_CORNER_THIN = b[24]
BR_CORNER_THIN_VERT = b[25]
BR_CORNER_THIN_HORIZ = b[26]
BR_CORNER_THICK = b[27]
THIN_VERT_LINE_THIN_HORIZ_RIGHT = b[28]
THIN_VERT_LINE_THICK_HORIZ_RIGHT = b[29]
