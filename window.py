import tdl
import colors as col
import itertools
import widgets

class Window():

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.widget_list = []

        # create console
        self.con = tdl.Console(w, h)

        # draw frame
        for i, j in itertools.product(range(self.w), range(self.h)):
            self.con.draw_char(i, j, None, None, col.BASE01)

    def draw_char(self, x, y, char, fg, bg):
        self.con.draw_char(x, y, char, fg, bg)

    def draw_str(self, x, y, text, fg, bg):
        self.con.draw_str(x, y, text, fg, bg)

    def blit(self, root):
        # blit to root
        root.blit(self.con, self.x, self.y, self.w, self.h, 0, 0)