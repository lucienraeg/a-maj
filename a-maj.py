import tdl
import itertools

import window
import colors as col

class Terminal():

    def __init__(self, width, height, title='', font='terminal8x12'):
        self.width = width
        self.height = height
        self.title = title
        self.windows = []
        self.font = font

        tdl.set_font('fonts/{}.png'.format(font), greyscale=True, altLayout=False)
        self.root = tdl.init(width, height, title=title, fullscreen=False)

    def handle_keys(self):
        user_input = tdl.event.key_wait()

    def create_window(self, x, y, w, h):
        new_window = window.Window(x, y, w, h)
        self.windows.append(new_window)

        return new_window

    def blit_windows(self):
        for win in self.windows:
            # blit window
            win.blit(self.root)



# initialize
t = Terminal(32, 16)

w1 = t.create_window(0, 0, 16, 16)
w1.draw_char(1, 4, 15, col.RED, col.BASE07)
w1.draw_char(10, 2, None, None, col.CYAN)
w1.draw_char(2, 8, 1, col.MAGENTA, None)

# main loop
while not tdl.event.is_window_closed():
    t.blit_windows()

    tdl.flush()
