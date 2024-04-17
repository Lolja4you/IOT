import matplotlib.pyplot as plt
import tkinter as tk

import json
import pandas as pd


class LogText(tk.Text):
    def __init__(self, master, height, width):
        super().__init__(master, height=height, width=width)
        self.tag_configure("green", foreground="green")
        self.tag_configure("red", foreground="red")
        self.tag_configure("yellow", foreground="yellow")
        self.tag_configure("orange", foreground="orange")
        self.tag_configure("dBlue", foreground="#000033")
        self.tag_configure("blue", foreground="#0000ff")



class PlotHelper:
    def __init__(self, data_storage, type_plot, canvas, fig):
        self.colors = ['#FF0000', '#0000FF', '#006400', '#F4A460', '#00FF7F', '#FF00FF']
        self.press = None
        self.candle = type_plot
        
        self.data_storage = data_storage
        # self.log_text = log_text
        self.canvas = canvas
        self.fig = fig

        self.ax = None 


    def update_plot(self):
        self.fig.clear()
        
        data_dict = json.loads(self.data_storage)

        # Extract the 'DATA' key from the dictionary
        data = data_dict['DATA']

        # Convert the list of dictionaries into a pandas DataFrame
        df = pd.DataFrame(data)

        # Convert the 'DATE' column to a datetime format and set it as the index
        df['DATE'] = pd.to_datetime(df['DATE'], format='%y%m%d')
        df.set_index('DATE', inplace=True)


        if self.candle == 'Свечной':
            plt.xlabel('Date')
            plt.ylabel('Price (Rub)')
            plt.grid(which='major')
            plt.grid(which='minor', linestyle=':')
            up = df[df.CLOSE >= df.OPEN]

            # Create a new DataFrame called "DOWN" that stores the stock_prices
            # when the closing stock price is lesser than the opening stock price
            DOWN = df[df.CLOSE < df.OPEN]

            # When the stock prices have decreased, then it
            # will be represented by red color candlestick
            col1 = 'red'

            # When the stock prices have increased, then it
            # will be represented by green color candlestick
            col2 = 'green'

            # Set the width of candlestick elements
            width = 5
            width2 = 0.1

            # Plot the up prices of the stock
            plt.bar(up.index, up.CLOSE-up.OPEN, width, bottom=up.OPEN, color=col2)
            plt.bar(up.index, up.HIGH-up.CLOSE, width2, bottom=up.CLOSE, color=col2)
            plt.bar(up.index, up.LOW-up.OPEN, width2, bottom=up.OPEN, color=col2)

            # Plot the DOWN prices of the stock
            plt.bar(DOWN.index, DOWN.CLOSE-DOWN.OPEN, width, bottom=DOWN.OPEN, color=col1)
            plt.bar(DOWN.index, DOWN.HIGH-DOWN.OPEN, width2, bottom=DOWN.OPEN, color=col1)
            plt.bar(DOWN.index, DOWN.LOW-DOWN.CLOSE, width2, bottom=DOWN.CLOSE, color=col1)

            plt.xticks(rotation=45, ha='right')

            # Display the candlestick chart of stock data for a week


        else:
            self.ax = self.fig.add_subplot(111)
            self.ax.plot((df.LOW+df.HIGH)/2,  marker='o')
            
            plt.xticks(rotation=45, ha='right')
            plt.xlabel('Date')
            plt.ylabel('Price (Rub)')

            plt.grid(which='major')
            plt.grid(which='minor', linestyle=':')

        self.canvas.draw()

    def on_scroll(self, event):
        xdata = event.xdata
        ydata = event.ydata

        if event.button == 'DOWN':
            self.ax.set_xlim(xdata - (xdata - self.ax.get_xlim()[0]) * 1.1, xdata + (self.ax.get_xlim()[1] - xdata) * 1.1)
            self.ax.set_ylim(ydata - (ydata - self.ax.get_ylim()[0]) * 1.1, ydata + (self.ax.get_ylim()[1] - ydata) * 1.1)
        elif event.button == 'up':
            self.ax.set_xlim(xdata - (xdata - self.ax.get_xlim()[0]) * 0.9, xdata + (self.ax.get_xlim()[1] - xdata) * 0.9)
            self.ax.set_ylim(ydata - (ydata - self.ax.get_ylim()[0]) * 0.9, ydata + (self.ax.get_ylim()[1] - ydata) * 0.9)

        self.canvas.draw()

    def on_press(self, event, *args, **kwargs):
        if event.button == 2:  # Средняя кнопка мыши
            self.x0 = event.xdata
            self.y0 = event.ydata
            self.press = True

    def on_release(self, *args, **kwargs):
        self.press = False

    def on_motion(self, event):
        if self.press and event.button == 2:  # Средняя кнопка мыши
            if not self.split:
                dx = event.xdata - self.x0
                dy = event.ydata - self.y0
                xlim = self.ax.get_xlim()
                ylim = self.ax.get_ylim()
                self.ax.set_xlim(xlim[0] - dx, xlim[1] - dx)
                self.ax.set_ylim(ylim[0] - dy, ylim[1] - dy)
                self.fig.canvas.draw()
            else:
                for ax_single in self.ax.flat:
                    # print("ax_sing:",ax_single)
                    ax_single.set_xlim(ax_single.get_xlim() - dx)
                    ax_single.set_ylim(ax_single.get_ylim() - dy)

                    self.canvas.draw()