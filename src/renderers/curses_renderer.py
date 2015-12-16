import curses
import math
import time

class CursesRenderer(object):
    def __init__(self):
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)

    def __del__(self):
        curses.nocbreak()
        self.screen.keypad(True)
        curses.echo()
        curses.endwin()

    def render(self, game):
        self.screen.clear()

        row_length = 14
        row_height = 8
        screen_height, screen_width = self.screen.getmaxyx()

        row = 0
        col = 0

        if (row_height * math.ceil(len(game.boards) / 3.0)) > screen_height:
            self.screen.addstr(0,0, "Sorry, not enough space on the terminal")
            self.screen.refresh()
            time.sleep(3)
            # TODO: exit if too many boards
            # TODO: handle case where there are too many boards vertically
            return

        for board in game.boards:
            row_base = row * row_height + 1
            col_base = col * row_length + 1

            # Draw border
            self.screen.addch(row_base + 0, col_base + 0,curses.ACS_ULCORNER)
            self.screen.hline(row_base + 0, col_base + 1,curses.ACS_HLINE, 13-2)
            self.screen.addch(row_base + 0, col_base + 12,curses.ACS_URCORNER)
            self.screen.vline(row_base + 1, col_base + 0,curses.ACS_VLINE, 5)
            self.screen.addch(row_base + 6, col_base + 0,curses.ACS_LLCORNER)
            self.screen.hline(row_base + 6, col_base + 1,curses.ACS_HLINE, 13-2)
            self.screen.addch(row_base + 6, col_base + 12,curses.ACS_LRCORNER)
            self.screen.vline(row_base + 1, col_base + 12,curses.ACS_VLINE, 5)

            # Draw board lines
            self.screen.hline(row_base + 2, col_base + 1,curses.ACS_HLINE, 13-2)
            self.screen.hline(row_base + 4, col_base + 1,curses.ACS_HLINE, 13-2)
            self.screen.vline(row_base + 1, col_base + 4,curses.ACS_VLINE, 5)
            self.screen.vline(row_base + 1, col_base + 8,curses.ACS_VLINE, 5)

            if(col >= 2): # Maximum 3 boards per row
                col = 0
                row += 1
            else:
                col += 1
        self.screen.refresh()

        time.sleep(6)

        return self.cursor_pos()

    def render_error():
        pass


