import gdax
import time
import tkinter
from tkinter import *
from threading import Thread
import time


class Data():

    def __init__(self):
        self.public_client = gdax.PublicClient()

    def get_tick(self):
        return self.public_client.get_product_ticker(product_id="ETH-USD")["price"]

class View(Frame):
   
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.create_window()


    def create_window(self):
        self.data = Data()
        self.price = DoubleVar()
        self.current = DoubleVar()
        self.final = DoubleVar()

        eth = Label(self.master, text="ETH-USD Last Trade Price:")
        eth.pack()

        display = Label(self.master, textvariable=self.price)
        display.pack()

        lel2 = Label(self.master, text="")
        lel2.pack()

        lel = Label(self.master, text="Current Holding Value (USD):")
        lel.pack()

        display_3 = Label(self.master, textvariable=self.final)
        display_3.pack()

        lel3 = Label(self.master, text="")
        lel3.pack()

        lel4 = Label(self.master, text="Enter current holding volume:")
        lel4.pack()

        display2 = Entry(self.master, textvariable=self.current)       
        display2.pack()

        self.update_thread = Thread(target=self.update_price)
        self.update_thread.start()

        self.volume_thread = Thread(target=self.update_volume_t)
        self.volume_thread.start()

    def update_price(self):
        while(1):
            self.price.set(self.data.get_tick())
            time.sleep(0.1)

    def update_volume_t(self):

        while(1):
            try:
                self.final.set(self.price.get() * self.current.get())
                time.sleep(0.1)
            except tkinter.TclError:
                pass


root = Tk()
root.geometry("200x200")
app = View(root)

root.mainloop()