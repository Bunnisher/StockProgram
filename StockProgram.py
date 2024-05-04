from tkinter import *
import sqlite3
from PIL import ImageTk, Image
import numpy as np
import pandas as pd
from pandas import *
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv
import yfinance as yf
yf.pdr_override()

root = Tk()
root.title("Bunnisher's Stock Engine")
root.geometry("300x400")
root.configure(background='gray23')

cap_image = ImageTk.PhotoImage(Image.open("bunny2.jpg"))
cap_image_label = Label(image=cap_image)
cap_image_label.grid(row=0, column=0)

stockChoice = Entry(root, width=50)
stockChoice.grid(row=2, column=0, pady=10, padx=10)


def startStockSearch():
    data = pdr.get_data_yahoo(
        stockChoice.get(), start="2021-01-01", stop="2021-05-13", interval='1d')
    '''
    with open('stockPrices.csv', 'w', newline='') as f:
        w = csv.writer(f, dialect='excel')
        for record in data:
            w.writerow(record)
    '''
    print(data)

    #Date, Close = np.loadtxt(data, delimiter=',', unpack=True)

    data['Adj Close'].plot()
    plt.xlabel('Date')
    plt.ylabel('Adjusted')
    plt.title('Bunnisherz Stock Graph')
    plt.style.use('dark_background')
    plt.grid(color='w', linestyle='solid')
    plt.legend()
    plt.show()


def write_it():
    data = pdr.get_data_yahoo(
        stockChoice.get(), start="2020-11-20", stop="2020-11-20", interval='1m')
    df = pd.DataFrame(data)

    df2 = df['Adj Close']

    df2.to_csv('Stocky.csv')


startIt = Button(root, text="Start Program", bg='yellow2',
                 command=lambda: startStockSearch())
startIt.grid(row=1, column=0, pady=10)

writeIt = Button(root, text="Write it", command=lambda: write_it())
writeIt.grid(row=3, column=0, pady=10)

button4 = Button(root, text="By Rick", bg='goldenrod2', command=root.destroy)
button4.grid(row=15, column=0, pady=10)


root.mainloop()
