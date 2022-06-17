from datetime import datetime
from stock_class import Stock, DailyData
from os import path
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, simpledialog, filedialog
import csv
import matplotlib.pyplot as plt
import json


class InvestmentView:
    def __init__(self):
        self.stock_list = []

        # Create Window
        self.root = Tk()
        self.root.title("Investment Comparison")
      
        # Add Menu
        self.menubar = Menu(self.root)

        self.filemenu = Menu(self.menubar, tearoff=0)

        
        self.webmenu = Menu(self.menubar, tearoff=0)
        self.webmenu.add_command(label = "Import CSV from Yahoo! Finance...", command=self.importCSV_web_data)
        self.menubar.add_cascade(label="Web",menu=self.webmenu)

        self.chartmenu = Menu(self.menubar,tearoff=0)
        self.chartmenu.add_command(label="Display Stock Chart", command=self.display_chart)
        self.menubar.add_cascade(label="Chart",menu=self.chartmenu)


        self.root.config(menu=self.menubar)

        # Add heading information
        self.headingLabel = Label(self.root,text="No Stock Selected")
        self.headingLabel.grid(column=0,row=0,columnspan=3,padx = 5, pady = 10)
        

        # Add stock list
        self.stockLabel = Label(self.root,text="Stocks")
        self.stockLabel.grid(column=0,row=1,padx = 5, pady = 10,sticky=(N))

        self.stockList = Listbox(self.root)
        self.stockList.grid(column=0,row=2,padx = 5, pady = 5,sticky=(N,S))
        self.stockList.bind('<<ListboxSelect>>',self.update_data)
        
        
        # Add Tabs
        self.notebook = ttk.Notebook(self.root,padding="5 5 5 5")
       
        self.notebook.grid(column=2,row=2,sticky=(N,W,E,S))
        self.mainFrame = ttk.Frame(self.notebook)
        self.stockDataFrame = ttk.Frame(self.notebook)
        self.reportFrame = ttk.Frame(self.notebook)
        self.chartFrame = ttk.Frame(self.notebook)
        self.notebook.add(self.mainFrame,text='Manage')
        self.notebook.add(self.stockDataFrame,text='History')
        self.notebook.add(self.reportFrame,text = 'Report')
        

        # Set Up Main Tab
        self.addStockGroup = LabelFrame(self.mainFrame,text="Add Stock",padx=5,pady=5)
        self.addStockGroup.grid(column=0,row=0,padx=5,pady=5,sticky=(W,E))
     
        self.addSymbolLabel = Label(self.addStockGroup,text = "Symbol")
        self.addSymbolLabel.grid(column=0,row=0,padx = 5, pady = 5,sticky=(W))
        self.addSymbolEntry = Entry(self.addStockGroup)
        self.addSymbolEntry.grid(column=1,row=0,padx=5,pady=5)

        self.addNameLabel = Label(self.addStockGroup,text = "Name")
        self.addNameLabel.grid(column=0,row=1,padx = 5, pady = 5,sticky=(W))
        self.addNameEntry = Entry(self.addStockGroup)
        self.addNameEntry.grid(column=1,row=1,padx=5,pady=5)

        self.addSharesLabel = Label(self.addStockGroup,text = "Shares")
        self.addSharesLabel.grid(column=0,row=2,padx = 5, pady = 5,sticky=(W))
        self.addSharesEntry = Entry(self.addStockGroup)
        self.addSharesEntry.grid(column=1,row=2,padx=5,pady=5)

        self.addStockButton = Button(self.addStockGroup,text = "New Stock",command=self.add_stock)
        self.addStockButton.grid(column=0,row=3,columnspan = 2, padx = 5, pady = 5)


        self.deleteGroup = LabelFrame(self.mainFrame,text="Delete Stock",padx=5,pady=5)
        self.deleteGroup.grid(column=0,row=2,padx=5,pady=5,sticky=(W,E))

        self.deleteStockButton = Button(self.deleteGroup,text="Delete Selected Stock",command=self.delete_stock)
        self.deleteStockButton.grid(column=0,row=0,padx=5,pady=5)



        # Setup History Tab
        self.dailyDataList = Text(self.stockDataFrame,width=40)
        self.dailyDataList.grid(column=0,row=0,padx = 5, pady = 5)
        
        


        # Setup Report Tab
        self.stockReport = Text(self.reportFrame,width=40)
        self.stockReport.grid(column=0,row=0,padx=5,pady=5)

        self.root.mainloop()

 

    # Refresh history and report tabs
    def update_data(self, evt):
        self.display_stock_data()

    # Display stock price and volume history.
    def display_stock_data(self):
        if (self.stockList.curselection()):
            symbol = self.stockList.get(self.stockList.curselection())
            
            for stock in self.stock_list:
                if stock.symbol == symbol:
                    self.headingLabel['text'] = stock.name + " - " + str(stock.shares) + " Shares"
                    self.dailyDataList.delete("1.0",END)
                    self.stockReport.delete("1.0",END)
                    self.dailyDataList.insert(END,"- Date -   - Price -   - Volume -\n")
                    self.dailyDataList.insert(END,"=================================\n")
                    for daily_data in stock.DataList:
                        row = daily_data.date + "   " +  '${:0,.2f}'.format(daily_data.close) + "   " + str(daily_data.volume) + "\n"
                        self.dailyDataList.insert(END,row)
                    #display report
                    count = 0
                    price_total = 0.00
                    volume_total = 0
                    lowPrice = 999999.99
                    highPrice = 0.00
                    lowVolume = 999999999999
                    highVolume = 0
    
                    for daily_data in stock.DataList:
                        count = count + 1
                        price_total = price_total + daily_data.close
                        volume_total = volume_total + daily_data.volume
                        if daily_data.close < lowPrice:
                            lowPrice = daily_data.close
                        if daily_data.close > highPrice:
                            highPrice = daily_data.close
                        if daily_data.volume < lowVolume:
                            lowVolume = daily_data.volume
                        if daily_data.volume > highVolume:
                            highVolume = daily_data.volume
     
                        priceChange = lowPrice-highPrice
                        
                    if count > 0:
                        self.stockReport.insert(END,"Summary Data--\n\n")
                        self.stockReport.insert(END,"Low Price: " + "${:,.2f}".format(lowPrice) + "\n")
                        self.stockReport.insert(END,"High Price: " + "${:,.2f}".format(highPrice) + "\n")
                        self.stockReport.insert(END,"Average Price: " + "${:,.2f}".format(price_total/count) + "\n\n")
                        self.stockReport.insert(END,"Low Volume: " + str(lowVolume) + "\n")
                        self.stockReport.insert(END,"High Volume: " + str(highVolume) + "\n")
                        self.stockReport.insert(END,"Average Volume: " + "${:,.2f}".format(volume_total/count) + "\n\n")
                        self.stockReport.insert(END,"Change in Price: " + "${:,.2f}".format(priceChange) + "\n")
                        self.stockReport.insert(END,"Profit/Loss: " + "${:,.2f}".format(priceChange * stock.shares) + "\n")
                    else:
                        self.stockReport.insert(END,"*** No daily history.")

    
    # Add new stock to track.
    def add_stock(self):
        new_stock = Stock(self.addSymbolEntry.get(), self.addNameEntry.get(), float(self.addSharesEntry.get()))
        self.stock_list.append(new_stock)
        self.stockList.insert(END, self.addSymbolEntry.get())
        self.addSymbolEntry.delete(0, END)
        self.addNameEntry.delete(0, END)
        self.addSharesEntry.delete(0, END)


    # Remove stock and all history from being tracked.
    def delete_stock(self):
        symbol = self.stock_list.get(self.stockList.curselection())
        i = 0
        for stock in self.stock_list:
            if stock.symbol == symbol:
                self.stock_list.pop(i)
            i = i + 1
        self.display_stock_data()
        self.stockList.delete(0, END)
        for stock in self.stock_list:
            self.stockList.insert(END, stock.symbol)
        messagebox.showinfo("Stock Deleted", symbol, " Removed")




      # Get price and volume history from Yahoo! Finance using CSV import.
    def import_stock_csv(self,stock_list,symbol,filename):
        for stock in stock_list:
                if stock.symbol == symbol:
                    with open(filename, newline='') as stockdata:
                        datareader = csv.reader(stockdata,delimiter=',')
                        next(datareader)
                        for row in datareader:
                            daily_data = DailyData(str(row[0]),float(row[4]),float(row[6]))
                            stock.add_data(daily_data)   

    # Import CSV stock history file.
    def importCSV_web_data(self):
        symbol = self.stockList.get(self.stockList.curselection())
        filename = filedialog.askopenfilename(title="Select " + symbol + " File to Import",filetypes=[('Yahoo Finance! CSV','*.csv')])
        if filename != "":
            self.import_stock_csv(self.stock_list,symbol,filename)
            self.display_stock_data()
            messagebox.showinfo("Import Complete",symbol + "Import Complete")   
    
    # Display stock price chart.
    def display_chart(self):
        if (self.stockList.curselection()):
            symbol = self.stockList.get(self.stockList.curselection())
            
            for stock in self.stock_list:
                if stock.symbol == symbol:
                    self.headingLabel['text'] = stock.name + " - " + str(stock.shares) + " Shares"
                    self.dailyDataList.delete("1.0",END)
                    self.stockReport.delete("1.0",END)
                    self.dailyDataList.insert(END,"- Date -   - Price -   - Volume -\n")
                    self.dailyDataList.insert(END,"=================================\n")
                    for daily_data in stock.DataList:
                        row = daily_data.date + "   " +  '${:0,.2f}'.format(daily_data.close) + "   " + str(daily_data.volume) + "\n"
                        self.dailyDataList.insert(END,row)
                    #display report
                    count = 0
                    price_total = 0.00
                    volume_total = 0
                    lowPrice = 999999.99
                    highPrice = 0.00
                    lowVolume = 999999999999
                    highVolume = 0
    
                    for daily_data in stock.DataList:
                        count = count + 1
                        price_total = price_total + daily_data.close
                        volume_total = volume_total + daily_data.volume
                        if daily_data.close < lowPrice:
                            lowPrice = daily_data.close
                        if daily_data.close > highPrice:
                            highPrice = daily_data.close
                        if daily_data.volume < lowVolume:
                            lowVolume = daily_data.volume
                        if daily_data.volume > highVolume:
                            highVolume = daily_data.volume
     
                        priceChange = lowPrice-highPrice
                        
                    if count > 0:
                        self.stockReport.insert(END,"Summary Data--\n\n")
                        self.stockReport.insert(END,"Low Price: " + "${:,.2f}".format(lowPrice) + "\n")
                        self.stockReport.insert(END,"High Price: " + "${:,.2f}".format(highPrice) + "\n")
                        self.stockReport.insert(END,"Average Price: " + "${:,.2f}".format(price_total/count) + "\n\n")
                        self.stockReport.insert(END,"Low Volume: " + str(lowVolume) + "\n")
                        self.stockReport.insert(END,"High Volume: " + str(highVolume) + "\n")
                        self.stockReport.insert(END,"Average Volume: " + "${:,.2f}".format(volume_total/count) + "\n\n")
                        self.stockReport.insert(END,"Change in Price: " + "${:,.2f}".format(priceChange) + "\n")
                        self.stockReport.insert(END,"Profit/Loss: " + "${:,.2f}".format(priceChange * stock.shares) + "\n")
                    else:
                        self.stockReport.insert(END,"*** No daily history.")




        
    
    

def main():
        app = InvestmentView()
        

if __name__ == "__main__":
    # execute only if run as a script
    main()