import tdl
import colors as col
import itertools

class Window():

    def __init__(self, x, y, w, h, title=''):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.title = title

        # create console
        self.con = tdl.Console(w, h)

        # draw bg
        for i, j in itertools.product(range(self.w), range(self.h)):
            self.con.draw_char(i, j, None, None, col.BASE00)

    def draw_char(self, x, y, char, bg, fg):
        self.con.draw_char(x, y, char, bg, fg)

    def draw_str(self, x, y, text, bg, fg):
        self.con.draw_str(x, y, text, bg, fg)

    def blit(self, root):
        # draw title
        self.draw_str(1, 0, 'Hello', col.BASE07, None)
        # TODO: borders

        # blit to root
        root.blit(self.con, self.x, self.y, self.w, self.h, 0, 0)
