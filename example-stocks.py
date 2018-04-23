import pandas as pd
import pandas.io.data as web
import datetime

""" import tdl
import amaj
import colors as col

''' initialize '''

# terminal
t = amaj.Terminal(64, 24)

# subreddit panel
list_panel = t.create_window(0, 0, 16, 24)
[list_panel.draw_char(15, i, None, None, col.BASE00) for i in range(list_panel.h)] # sep bar

# main panel
main_panel = t.create_window(16, 0, 48, 32)

if __name__ == '__main__':
    while amaj.is_window_open(): 
        amaj.blit_terminal(t)
 """

# We will look at stock prices over the past year, starting at January 1, 2016
start = datetime.datetime(2017, 1, 1)
end = datetime.date.today()

# Let's get Apple stock data; Apple's ticker symbol is AAPL
# First argument is the series we want, second is the source ("yahoo" for Yahoo! Finance), third is the start date, fourth is the end date
apple = web.DataReader("AAPL", "yahoo", start, end)

type(apple)
