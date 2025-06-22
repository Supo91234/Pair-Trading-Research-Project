import tkinter as tk
import tkinter.ttk as ttk
import pygame

class StocksWithNookGUI:
    def __init__(self, StockOneInfo):
        # Variables
        self.StockOneInformation = StockOneInfo

        # Background Music
        pygame.mixer.init()

        pygame.mixer.music.load('ProgramFeatures/Track1.mp3')
        pygame.mixer.music.play(loops=-1)

        # Creates Interface
        self.MainProgram = tk.Tk()
        self.MainProgram.title("Stocks with Tom Nook")
        self.MainProgram.configure(bg="#11835f")
        self.MainProgram.geometry("500x500")

        self.CreateInterface()

    def CreateInterface(self):
        StockOneButton = tk.Button(self.MainProgram, text="Stock 1", bg="Brown", fg="White", command=self.DisplayStockOne)
        StockOneButton.pack(side='left', anchor='nw', padx=1, pady=20)

        StockTwoButton = tk.Button(self.MainProgram, text="Stock 2", bg="Brown", fg="White")
        StockTwoButton.pack(side='left', anchor='nw', padx=1, pady=20)

        StockCompareButton = tk.Button(self.MainProgram, text="Compare Stocks", bg="Brown", fg="White")
        StockCompareButton.pack(side='left', anchor='nw', padx=1, pady=20)

        # SeparatorTop = tk.Frame(self.MainProgram)
        # SeparatorTop.pack()

        # Add Image of the stock ? and extra stuff below

        # SeparatorBottom = ttk.Separator(self.MainProgram)
        # SeparatorMain.place(relx=.01, rely=.75, relwidth=.98, relheight=.0025, anchor='center')

    def DisplayStockOne(self):
        print(self.StockOneInformation[0])
        print(self.StockOneInformation[1])

    def CalculateMean(self):
        print("e")
